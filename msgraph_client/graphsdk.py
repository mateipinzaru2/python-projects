import os
import datetime
import asyncio
import csv

from decouple import Config

from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder
from msgraph.generated.reports.authentication_methods.user_registration_details.user_registration_details_request_builder import (
    UserRegistrationDetailsRequestBuilder,
)
from kiota_abstractions.api_error import APIError


config = Config(".env")

tenant_id = config("TENANT_ID")
client_id = config("CLIENT_ID")
client_secret = config("CLIENT_SECRET")

if tenant_id is None:
    raise Exception("Please set the TENANT_ID variable")
if client_id is None:
    raise Exception("Please set the CLIENT_ID variable")
if client_secret is None:
    raise Exception("Please set the CLIENT_SECRET variable")


credential = ClientSecretCredential(tenant_id, client_id, client_secret)
scopes = ["https://graph.microsoft.com/.default"]
client = GraphServiceClient(
    credentials=credential,
    scopes=scopes,
)


user_query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(
    filter="accountEnabled eq true",
    select=["userPrincipalName", "id", "signInActivity"],
    expand=["memberOf"],
    top=999,
)
user_request_config = UsersRequestBuilder.UsersRequestBuilderGetRequestConfiguration(
    query_parameters=user_query_params
)


mfa_query_params = UserRegistrationDetailsRequestBuilder.UserRegistrationDetailsRequestBuilderGetQueryParameters(
    filter="isMfaRegistered eq true",
    top=999,
)
mfa_request_config = UserRegistrationDetailsRequestBuilder.UserRegistrationDetailsRequestBuilderGetRequestConfiguration(
    query_parameters=mfa_query_params
)


os.makedirs("output", exist_ok=True)
now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"output/graphsdk_output_{now_str}.csv"


async def get_user_pages():
    try:
        user_pages = []
        page = await client.users.get(request_configuration=user_request_config)
        user_pages.append(page)

        while page.odata_next_link:
            page = await client.users.with_url(page.odata_next_link).get(
                request_configuration=user_request_config
            )
            user_pages.append(page)

    except APIError as e:
        print(f"Error: {e.error.message}")

    return user_pages


async def get_mfa_pages():
    try:
        mfa_pages = []
        page = (
            await client.reports.authentication_methods.user_registration_details.get(
                request_configuration=mfa_request_config
            )
        )
        mfa_pages.append(page)

        while page.odata_next_link:
            page = await client.reports.authentication_methods.user_registration_details.with_url(
                page.odata_next_link
            ).get(
                request_configuration=mfa_request_config
            )
            mfa_pages.append(page)

    except APIError as e:
        print(f"Error: {e.error.message}")

    return mfa_pages


async def process_users():
    users_pages = await get_user_pages()
    mfa_pages = await get_mfa_pages()
    mfa_dict = {}
    if mfa_pages:
        for mfas in mfa_pages:
            if mfas and mfas.value:
                for mfa in mfas.value:
                    mfa_dict[mfa.id] = "Yes" if mfa.is_mfa_registered else "No"
    if users_pages:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["User", "MFA Registered", "Sign in date", "Groups"])
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
                        mfa_registered = mfa_dict.get(user.id, "No")
                        writer.writerow(
                            [
                                user.user_principal_name,
                                mfa_registered,
                                sign_in_date,
                                groups,
                            ]
                        )


asyncio.run(process_users())
