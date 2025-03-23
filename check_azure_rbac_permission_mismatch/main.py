import requests
import re
import sys
import csv
from datetime import datetime
from azure.identity import DefaultAzureCredential

# ---------------------------------------------------------------------
# Configuration & Credential Setup
# ---------------------------------------------------------------------
credential = DefaultAzureCredential()

# ARM API credentials
ARM_SCOPE = "https://management.azure.com/.default"
try:
    arm_token = credential.get_token(ARM_SCOPE).token
except Exception as e:
    print("Failed to acquire ARM token:", e)
    sys.exit(1)
arm_headers = {
    "Authorization": "Bearer " + arm_token,
    "Content-Type": "application/json"
}
ARM_BASE = "https://management.azure.com"

# Microsoft Graph credentials (for identity resolution)
GRAPH_SCOPE = "https://graph.microsoft.com/.default"
try:
    graph_token = credential.get_token(GRAPH_SCOPE).token
except Exception as e:
    print("Failed to acquire Graph token:", e)
    sys.exit(1)
graph_headers = {
    "Authorization": "Bearer " + graph_token,
    "Content-Type": "application/json"
}

# ---------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------
def fetch_subscriptions():
    """Fetch all subscriptions accessible to the current identity."""
    url = f"{ARM_BASE}/subscriptions?api-version=2020-01-01"
    response = requests.get(url, headers=arm_headers)
    if response.status_code != 200:
        print("Failed to fetch subscriptions:", response.status_code, response.text)
        sys.exit(1)
    return response.json().get("value", [])

def fetch_role_assignments(subscription_id):
    """
    Fetch all role assignments for a given subscription.
    Includes inherited assignments and handles pagination via 'nextLink'.
    """
    assignments = []
    url = f"{ARM_BASE}/subscriptions/{subscription_id}/providers/Microsoft.Authorization/roleAssignments?api-version=2022-04-01"
    while url:
        response = requests.get(url, headers=arm_headers)
        if response.status_code != 200:
            print(f"Failed to fetch role assignments for subscription {subscription_id}:",
                  response.status_code, response.text)
            break
        data = response.json()
        assignments.extend(data.get("value", []))
        url = data.get("nextLink")
    return assignments

# Caches to avoid duplicate API calls.
identity_cache = {}
role_def_cache = {}

def get_identity_name(principal_id, principal_type):
    """
    Resolve a human-readable display name for an identity via Microsoft Graph.
    Caches results to reduce duplicate API calls.
    """
    if principal_id in identity_cache:
        return identity_cache[principal_id]
    
    if principal_type.lower() == "serviceprincipal":
        url = f"https://graph.microsoft.com/v1.0/servicePrincipals/{principal_id}"
    elif principal_type.lower() == "group":
        url = f"https://graph.microsoft.com/v1.0/groups/{principal_id}"
    elif principal_type.lower() == "user":
        url = f"https://graph.microsoft.com/v1.0/users/{principal_id}"
    else:
        url = f"https://graph.microsoft.com/v1.0/servicePrincipals/{principal_id}"
    
    r = requests.get(url, headers=graph_headers)
    if r.status_code == 200:
        data = r.json()
        name = data.get("displayName") or data.get("userPrincipalName") or ""
    else:
        name = ""
    identity_cache[principal_id] = name
    return name

def get_role_definition_name(role_definition_id):
    """
    Resolve a human-readable role definition name using the ARM API.
    Caches the result to reduce duplicate calls.
    """
    if role_definition_id in role_def_cache:
        return role_def_cache[role_definition_id]
    
    url = f"{ARM_BASE}{role_definition_id}?api-version=2022-04-01"
    r = requests.get(url, headers=arm_headers)
    if r.status_code == 200:
        data = r.json()
        name = data.get("properties", {}).get("roleName", "")
    else:
        name = ""
    role_def_cache[role_definition_id] = name
    return name

def is_production_subscription(subscription_name):
    """
    Determine if the subscription name qualifies as production.
    Returns True if the subscription name contains 'prod' or 'prd'
    as a discrete token (e.g. '-prod-' or ending/starting with 'prod'),
    excluding names that contain 'nonprod'.
    """
    if re.search(r"nonprod", subscription_name, re.IGNORECASE):
        return False
    return (re.search(r"(^|[-\s])prod([-\s]|$)", subscription_name, re.IGNORECASE) is not None or
            re.search(r"(^|[-\s])prd([-\s]|$)", subscription_name, re.IGNORECASE) is not None)

def is_production_scope(scope, subscription_name):
    """
    Determines whether the scope qualifies as production.
    If the scope contains a resource group, it extracts the resource group name and checks
    that it contains 'prod' or 'prd' as a discrete segment.
    If the scope is at the subscription level (or lacks a resource group), then the subscription name
    is used to decide.
    """
    # If the scope is at the subscription level (e.g. "/subscriptions/<id>")
    if re.match(r"^/subscriptions/[^/]+$", scope):
        return is_production_subscription(subscription_name)
    
    rg_match = re.search(r"/resourceGroups/([^/]+)", scope, re.IGNORECASE)
    if rg_match:
        rg_name = rg_match.group(1)
        if (re.search(r"(^|-)prod(-|$)", rg_name, re.IGNORECASE) or
            re.search(r"(^|-)prd(-|$)", rg_name, re.IGNORECASE)):
            return True
        else:
            return False
    # Fallback: if no resource group is found, rely on the subscription name.
    return is_production_subscription(subscription_name)

# ---------------------------------------------------------------------
# Main Process
# ---------------------------------------------------------------------
def main():
    print("Fetching subscriptions...")
    subscriptions = fetch_subscriptions()
    print(f"Total subscriptions found: {len(subscriptions)}")

    all_assignments = []
    for sub in subscriptions:
        sub_id = sub.get("subscriptionId")
        sub_name = sub.get("displayName", sub_id)
        print(f"Fetching role assignments for subscription: {sub_name}")
        assignments = fetch_role_assignments(sub_id)
        print(f"  {len(assignments)} assignments found")
        for assignment in assignments:
            assignment["subscriptionId"] = sub_id
            assignment["subscriptionName"] = sub_name
        all_assignments.extend(assignments)
    
    print(f"\nTotal role assignments fetched across all subscriptions: {len(all_assignments)}")

    # Identity filter: names should contain one of these keywords.
    identity_pattern = re.compile(r"test|staging|stg|tst", re.IGNORECASE)
    
    filtered = []
    for assignment in all_assignments:
        props = assignment.get("properties", {})
        scope = props.get("scope", "")
        # Now check if the scope qualifies as production based on resource group or subscription name.
        if not is_production_scope(scope, assignment.get("subscriptionName", "")):
            continue
        
        principal_id = props.get("principalId", "")
        principal_type = props.get("principalType", "")
        identity_name = get_identity_name(principal_id, principal_type)
        
        if identity_pattern.search(identity_name):
            assignment["resolvedPrincipalName"] = identity_name
            role_def_id = props.get("roleDefinitionId", "")
            assignment["resolvedRoleDefinitionName"] = get_role_definition_name(role_def_id)
            filtered.append(assignment)
    
    print(f"\nFound {len(filtered)} role assignments matching the criteria.\n")

    # Prepare CSV output.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"role_assignments_{timestamp}.csv"
    fields = [
        "subscriptionId", 
        "subscriptionName",
        "assignmentId", 
        "principalId", 
        "resolvedPrincipalName", 
        "principalType", 
        "scope", 
        "roleDefinitionId", 
        "resolvedRoleDefinitionName", 
        "createdOn", 
        "updatedOn"
    ]

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for assignment in filtered:
            props = assignment.get("properties", {})
            row = {
                "subscriptionId": assignment.get("subscriptionId", ""),
                "subscriptionName": assignment.get("subscriptionName", ""),
                "assignmentId": assignment.get("id", ""),
                "principalId": props.get("principalId", ""),
                "resolvedPrincipalName": assignment.get("resolvedPrincipalName", ""),
                "principalType": props.get("principalType", ""),
                "scope": props.get("scope", ""),
                "roleDefinitionId": props.get("roleDefinitionId", ""),
                "resolvedRoleDefinitionName": assignment.get("resolvedRoleDefinitionName", ""),
                "createdOn": props.get("createdOn", ""),
                "updatedOn": props.get("updatedOn", "")
            }
            writer.writerow(row)
    
    print(f"Results saved to CSV file: {filename}")

if __name__ == "__main__":
    main()