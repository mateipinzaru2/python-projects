import os
import random
import requests
import csv
import urllib.parse
import time
import datetime


# Implement a retry mechanism for API calls
def get_response_with_retry(url, headers, max_retries=5):
    retry_count = 0
    while retry_count < max_retries:
        response = requests.get(url, headers=headers)
        if (
            response.status_code != 429
        ):  # 429 is the status code for "Too Many Requests"
            return response
        wait_time = (2**retry_count) + (random.randint(0, 1000) / 1000)
        print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
        time.sleep(wait_time)
        retry_count += 1
    raise Exception("Error fetching data: " + response.text)


# Function to get access token
def get_access_token():
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://graph.microsoft.com/.default",
    }
    print("Requesting access token...")
    response = requests.post(url, data=data)
    access_token = response.json()["access_token"]
    print("Access token received.")
    return access_token


# Azure AD app registration details
tenant_id = os.getenv("TENANT_ID")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Check that all environment variables are set
if tenant_id is None:
    raise Exception("Please set the TENANT_ID environment variable")
if client_id is None:
    raise Exception("Please set the CLIENT_ID environment variable")
if client_secret is None:
    raise Exception("Please set the CLIENT_SECRET environment variable")

# Get access token
url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": "https://graph.microsoft.com/.default",
}
access_token = get_access_token()
token_time = datetime.datetime.now()

# Define the API endpoint
api_endpoint = (
    "https://graph.microsoft.com/v1.0/users?$filter=accountEnabled eq true&$top=999"
)
print(f"API endpoint defined: {api_endpoint}")

# Initialize the CSV file
csv_file = open("active_users.csv", "w")
csv_writer = csv.writer(csv_file)
print("CSV file initialized.")

# Write the header row
csv_writer.writerow(["UserPrincipalName", "LastSignInDate", "GroupMembership"])
print("Header row written to CSV file.")

# Process each page of users
print(f"Fetching users from {api_endpoint}")
while api_endpoint is not None:
    # Before each request
    if datetime.datetime.now() - token_time > datetime.timedelta(minutes=20):
        access_token = get_access_token()
        token_time = datetime.datetime.now()
    response = get_response_with_retry(
        api_endpoint, headers={"Authorization": f"Bearer {access_token}"}
    )

    # Check the status code of the response
    if response.status_code != 200:
        raise Exception("Error fetching user list: " + response.text)

    # Parse the JSON response
    data = response.json()
    users = data["value"]

    # Process each user
    for user in users:
        user_principal_name = user["userPrincipalName"]

        # URL-encode the userPrincipalName
        encoded_user_principal_name = urllib.parse.quote(user_principal_name)

        # Get the last sign-in date for the user
        sign_in_endpoint = f"https://graph.microsoft.com/v1.0/auditLogs/signIns?$filter=userPrincipalName eq '{encoded_user_principal_name}'&$orderby=createdDateTime desc&$top=1"
        # Before each request
        if datetime.datetime.now() - token_time > datetime.timedelta(minutes=20):
            access_token = get_access_token()
            token_time = datetime.datetime.now()
        sign_in_response = get_response_with_retry(
            sign_in_endpoint, headers={"Authorization": f"Bearer {access_token}"}
        )
        if sign_in_response.status_code != 200:
            raise Exception("Error fetching sign-in activity: " + sign_in_response.text)
        sign_in_data = sign_in_response.json()
        last_sign_in_date = (
            sign_in_data["value"][0]["createdDateTime"] if sign_in_data["value"] else ""
        )

        # Convert LastSignInDate to a human-readable format
        if last_sign_in_date:
            last_sign_in_date = last_sign_in_date[:10]  # Extract the date part

        # Get the group membership for the user
        group_membership_endpoint = f"https://graph.microsoft.com/v1.0/users/{encoded_user_principal_name}/memberOf"
        # Before each request
        if datetime.datetime.now() - token_time > datetime.timedelta(minutes=20):
            access_token = get_access_token()
            token_time = datetime.datetime.now()
        group_response = get_response_with_retry(
            group_membership_endpoint,
            headers={"Authorization": f"Bearer {access_token}"},
        )
        if group_response.status_code != 200:
            raise Exception("Error fetching group membership: " + group_response.text)
        group_membership = [
            group["displayName"] for group in group_response.json()["value"]
        ]

        # Write the user data to the CSV file
        print(f"Writing user data to CSV file: {user_principal_name}")
        csv_writer.writerow(
            [user_principal_name, last_sign_in_date, ",".join(group_membership)]
        )

        # Get the next page URL
        api_endpoint = data.get("@odata.nextLink")

# Close the CSV file
csv_file.close()

print("Finished writing to CSV file.")
