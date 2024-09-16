from azure.identity import ClientSecretCredential
from msgraph.graph_service_client import GraphServiceClient
from config import TENANT_ID, CLIENT_ID, CLIENT_SECRET

credential = ClientSecretCredential(TENANT_ID, CLIENT_ID, CLIENT_SECRET)
scopes = ["https://graph.microsoft.com/.default"]
client = GraphServiceClient(credentials=credential, scopes=scopes)
