# Azure Graph API Client
This is a Python client for the `Microsoft Graph API`. 

It gets **all Entra `enabled` users** and for each user, it fetches the:

  - **Last sign-in activity**
  - **MFA Registration Status**
  - **Group Membership**
  - **Entra Role Assignments** 

It then stores the data in a CSV file. 

## Pre-requisites
- Azure App Registration with:
  - `User.Read.All` permission
  - `Group.Read.All` permission
  - `AuditLog.Read.All` permission

- Create a file called `.env` in the project root directory with the following information:
  ```conf
  TENANT_ID = 'your_tenant_id'
  CLIENT_ID = 'your_client_id'
  CLIENT_SECRET = 'your_client_secret'
  ```

## Setup
- `python3 -m venv .venv && source .venv/bin/activate` to create and activate a virtual environment
- `pip3 install -r requirements.txt` to install dependencies
- `python3 src/main.py` to run the program

### Performance Stats
For ***3015*** users **->** ***1m 10s*** execution time.