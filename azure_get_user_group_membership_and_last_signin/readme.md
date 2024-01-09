# Azure Graph API Client
This is a client for the Azure Graph API. It fetches all users from the API and for each user, it fetches the last sign-in activity and the group membership. It then stores the data in a CSV file.

## Pre-requisites
- Azure App Registration with:
  - `User.Read.All` permission
  - `Group.Read.All` permission
  - `AuditLog.Read.All` permission
- 3 ENV variables:
  - `AZURE_CLIENT_ID`
  - `AZURE_CLIENT_SECRET`
  - `AZURE_TENANT_ID`

## Setup
- `brew install poetry`
- `cd` to where **pyproject.toml** is
- `poetry shell` to enter virtual environment
- `python <file.py>` to run the file
- `exit` to exit the virtual environment

## Performance
The main loop of the program fetches users from the API and processes each user individually. For each user, it makes two additional API calls: one to fetch the last sign-in activity and another to fetch the group membership. Therefore, if `n` is the ***number of users*** and `m` is the ***average number of groups a user is a part of***, the `time complexity` would be `O(n + nm)`, which simplifies to `O(nm)` *if `m` is large*.

Due to the API rate limit, there isn't much of a difference between the single-threaded and multithreaded versions of the program. The multithreaded version is only slightly faster because it can make more requests in parallel, but it still has to wait for the API to respond.

### Single Threaded Stats
For ***3005*** users **->** ***6h 11m 46s*** execution time

### Multithreaded Stats
For ***3005*** users **->** ***N/A*** execution time