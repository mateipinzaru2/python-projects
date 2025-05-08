# Azure Role Assignment Production Check Script

## How to Run the Script

1. Ensure you have logged in via Azure CLI or configured your environment for Azure authentication.
2. Create and activate a virtual environment:
### virtualenv
- `python3 -m venv .venv && source .venv/bin/activate` to create and activate a virtual environment
- `pip3 install -r requirements.txt` to install dependencies
- `python3 main.py` to run the program

### uv
- `uv init --bare` to create and activate a virtual environment
- `uv add -r requirements.txt` to install dependencies
- `uv run main.py` to run the program

## Overview

This Python script retrieves all Azure role assignments across every subscription in your tenant using the Azure Resource Manager (ARM) API. It then enriches each assignment by:
- Resolving a human-readable identity name using the Microsoft Graph API.
- Resolving the human‑readable role definition name via ARM.
- Filtering assignments that are scoped to production environments.

A production scope is determined by checking if the resource group's name (if available) or the subscription name itself includes a discrete token of "prod" or "prd" (while excluding false positives like "nonprod"). Additionally, the script looks for identities (service principals, groups, users) whose names include keywords such as `test`, `staging`, `stg`, or `tst` (case‑insensitive).

The final filtered assignments are saved in a CSV file with a filename timestamped with the execution date and time.

## Prerequisites

- **Python 3.6 or higher**
- **Required packages:**  
  - `azure-identity` (for authentication using `DefaultAzureCredential`)
  - `requests` (to make HTTP calls to ARM and Graph APIs)

## Authentication

The script uses `DefaultAzureCredential` from the `azure-identity` package to authenticate with:
- **ARM API** (for fetching subscriptions and role assignments)
- **Microsoft Graph API** (for resolving identity display names)

Ensure that you are logged in via the Azure CLI (`az login`) or have another supported authentication method configured so that `DefaultAzureCredential` can pick up your credentials.

## How the Script Works

### 1. Fetching Subscriptions

- Calls the ARM endpoint `/subscriptions?api-version=2020-01-01` to list all subscriptions available to the current identity.
- Each subscription's ID and name are recorded.

### 2. Fetching Role Assignments

- For every subscription, the script calls the ARM endpoint:
  ```
  /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/roleAssignments?api-version=2022-04-01
  ```
- It retrieves direct and inherited role assignments and handles pagination via the `nextLink` value.
- Each assignment is tagged with its corresponding subscription details.

### 3. Enriching Data

- **Identity Resolution:**  
  Uses Microsoft Graph to convert the identity's object ID (for service principals, groups, or users) into a human‑readable name.
- **Role Definition Resolution:**  
  Uses the ARM API to fetch a human‑readable role name from the `roleDefinitionId`.

### 4. Filtering Role Assignments

- **Production Scope Check:**  
  - If the scope contains a resource group (e.g., `/resourceGroups/rg-prod-example`), the script verifies that the resource group name includes "prod" or "prd" as a discrete token.
  - If the scope is at the subscription level or does not include a resource group, the subscription name is checked.
- **Identity Name Check:**  
  The script filters out assignments where the resolved identity name contains one of the keywords: `test`, `staging`, `stg`, or `tst`.

### 5. Output to CSV

- The filtered role assignments are written to a CSV file.
- The CSV filename is timestamped in the format:  
  `role_assignments_YYYYMMDD_HHMM.csv`
- The CSV includes the following fields:
  - Subscription ID and name
  - Assignment ID
  - Principal ID and resolved principal name
  - Principal type
  - Scope
  - Role definition ID and resolved role definition name
  - Created and updated timestamps

## Customization

- **Regex Patterns:**  
  Modify the regex patterns in `is_production_subscription` and `is_production_scope` functions to better align with your naming conventions.

- **API Versions:**  
  The script uses specific API versions for ARM and Microsoft Graph endpoints. Adjust these if needed.

## Troubleshooting

- **Authentication Errors:**  
  Ensure you are logged in via `az login` or have another valid authentication method configured.

- **Dependency Issues:**  
  Confirm that you have installed all required packages using the provided `requirements.txt`.

- **Unexpected Output:**  
  Check your resource and subscription naming conventions. You may need to adjust the filtering logic to reduce false positives.
