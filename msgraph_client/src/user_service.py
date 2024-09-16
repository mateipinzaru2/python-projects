from msgraph.generated.users.users_request_builder import UsersRequestBuilder
from graph_client import client
from kiota_abstractions.api_error import APIError


user_query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(
    filter="accountEnabled eq true",
    select=["userPrincipalName", "id", "signInActivity"],
    expand=["transitiveMemberOf"],
    top=999,
)
user_request_config = UsersRequestBuilder.UsersRequestBuilderGetRequestConfiguration(
    query_parameters=user_query_params
)


async def get_user_pages():
    user_pages = []
    try:
        page = await client.users.get(request_configuration=user_request_config)
        user_pages.append(page)

        while page and page.odata_next_link:
            page = await client.users.with_url(page.odata_next_link).get(
                request_configuration=user_request_config
            )
            user_pages.append(page)

    except APIError as e:
        print(f"Error: {e.message}")

    return user_pages
