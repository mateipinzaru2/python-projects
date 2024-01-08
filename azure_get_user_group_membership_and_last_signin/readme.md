# Setup
- `brew install poetry`
- `cd` to where **pyproject.toml** is
- `poetry shell` to enter virtual environment
- `python <file.py>` to run the file
- `exit` to exit the virtual environment

# Performance
The main loop of the program fetches users from the API and processes each user individually. For each user, it makes two additional API calls: one to fetch the last sign-in activity and another to fetch the group membership. Therefore, if `n` is the ***number of users*** and `m` is the ***average number of groups a user is a part of***, the `time complexity` would be `O(n + nm)`, which simplifies to `O(nm)` *if `m` is large*.

## Stats
For aproximately ***27k*** requests **->** ***6h 11m 46s*** execution time