# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.email_account_list_response import EmailAccountListResponse

__all__ = ["EmailAccountsResource", "AsyncEmailAccountsResource"]


class EmailAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EmailAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return EmailAccountsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailAccountListResponse:
        """
        Use the Get a List of Email Accounts endpoint to retrieve information about the
        linked email inboxes that your teammates use in your Apollo account.

        In particular, this endpoint returns IDs for each of your team's linked email
        accounts, which can be used with the
        <a href="https://docs.apollo.io/reference/add-contacts-to-sequence" target="_blank">Add
        Contacts to a Sequence endpoint</a>.

        This endpoint does not require any parameters.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.
        """
        return self._get(
            "/email_accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailAccountListResponse,
        )


class AsyncEmailAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncEmailAccountsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailAccountListResponse:
        """
        Use the Get a List of Email Accounts endpoint to retrieve information about the
        linked email inboxes that your teammates use in your Apollo account.

        In particular, this endpoint returns IDs for each of your team's linked email
        accounts, which can be used with the
        <a href="https://docs.apollo.io/reference/add-contacts-to-sequence" target="_blank">Add
        Contacts to a Sequence endpoint</a>.

        This endpoint does not require any parameters.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.
        """
        return await self._get(
            "/email_accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailAccountListResponse,
        )


class EmailAccountsResourceWithRawResponse:
    def __init__(self, email_accounts: EmailAccountsResource) -> None:
        self._email_accounts = email_accounts

        self.list = to_raw_response_wrapper(
            email_accounts.list,
        )


class AsyncEmailAccountsResourceWithRawResponse:
    def __init__(self, email_accounts: AsyncEmailAccountsResource) -> None:
        self._email_accounts = email_accounts

        self.list = async_to_raw_response_wrapper(
            email_accounts.list,
        )


class EmailAccountsResourceWithStreamingResponse:
    def __init__(self, email_accounts: EmailAccountsResource) -> None:
        self._email_accounts = email_accounts

        self.list = to_streamed_response_wrapper(
            email_accounts.list,
        )


class AsyncEmailAccountsResourceWithStreamingResponse:
    def __init__(self, email_accounts: AsyncEmailAccountsResource) -> None:
        self._email_accounts = email_accounts

        self.list = async_to_streamed_response_wrapper(
            email_accounts.list,
        )
