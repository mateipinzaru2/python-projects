import os
import asyncio
import csv

from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder
from kiota_abstractions.api_error import APIError


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


credential = ClientSecretCredential(tenant_id, client_id, client_secret)
scopes = ["https://graph.microsoft.com/.default"]
client = GraphServiceClient(
    credentials=credential,
    scopes=scopes,
)


query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(
    filter="accountEnabled eq true",
    select=["userPrincipalName", "signInActivity"],
    expand=["memberOf"],
    top=999,
)
request_config = UsersRequestBuilder.UsersRequestBuilderGetRequestConfiguration(
    query_parameters=query_params
)


async def get_user_pages():
    try:
        user_pages = []
        page = await client.users.get(request_configuration=request_config)
        user_pages.append(page)

        while page.odata_next_link:
            page = await client.users.with_url(page.odata_next_link).get(
                request_configuration=request_config
            )
            user_pages.append(page)

    except APIError as e:
        print(f"Error: {e.error.message}")

    return user_pages


async def process_users():
    users_pages = await get_user_pages()
    if users_pages:
        with open("graphsdk_output.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["User", "Sign in date", "Groups"])
            for users in users_pages:
                if users and users.value:
                    for user in users.value:
                        groups = (
                            ", ".join(
                                group.display_name for group in user.member_of or []
                            )
                            if user.member_of
                            else "N/A"
                        )
                        sign_in_date = (
                            user.sign_in_activity.last_sign_in_date_time
                            if user.sign_in_activity
                            else "N/A"
                        )
                        writer.writerow(
                            [user.user_principal_name, sign_in_date, groups]
                        )


asyncio.run(process_users())
