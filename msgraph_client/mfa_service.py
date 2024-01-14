from msgraph.generated.reports.authentication_methods.user_registration_details.user_registration_details_request_builder import (
    UserRegistrationDetailsRequestBuilder,
)
from graph_client import client
from kiota_abstractions.api_error import APIError


mfa_query_params = UserRegistrationDetailsRequestBuilder.UserRegistrationDetailsRequestBuilderGetQueryParameters(
    filter="isMfaRegistered eq true",
    top=999,
)
mfa_request_config = UserRegistrationDetailsRequestBuilder.UserRegistrationDetailsRequestBuilderGetRequestConfiguration(
    query_parameters=mfa_query_params
)


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
