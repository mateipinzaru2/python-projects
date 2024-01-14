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
  TENANT_ID=your_tenant_id
  CLIENT_ID=your_client_id
  CLIENT_SECRET=your_client_secret
  ```

## Setup
- `brew install poetry` to install [Poetry](https://python-poetry.org/)
- `poetry install` to install dependencies
- `poetry shell` to enter virtual environment
- `python src/main.py` to run the program
- `exit` to exit the virtual environment

## Performance
The app makes use of the [Python Microsoft Graph SDK](https://github.com/microsoftgraph/msgraph-sdk-python) to fetch batches of ***999*** users, and expanding the response to include **Last sign-in Date**, **Entra Role Assignments**, and **Group Membership** in a single API call. This is possible via [query parameters](https://learn.microsoft.com/en-us/graph/query-parameters?tabs=http#expand-parameter).

Since the First API call can't be expanded to include the MFA details, the app makes a second API call to fetch the **MFA Registration Status** for each user.

Both API calls are recursive, and loop until all available user and MFA data is fetched. Once all data is fetched, the main loop of the program processes each user individually and stores the data in a CSV file.

Since the API calls are batched and async, the time complexity of the app is given by the main loop, which needs to process each user individually and write it to file. Therefore, if `n` is the ***number of users***, the `time complexity` would be `O(n)`.

### Performance Stats
For ***3015*** users **->** ***1m 10s*** execution time.