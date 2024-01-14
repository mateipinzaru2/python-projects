from decouple import config

TENANT_ID = config("TENANT_ID")
CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")

if TENANT_ID is None:
    raise Exception("Please set the TENANT_ID variable")
if CLIENT_ID is None:
    raise Exception("Please set the CLIENT_ID variable")
if CLIENT_SECRET is None:
    raise Exception("Please set the CLIENT_SECRET variable")
