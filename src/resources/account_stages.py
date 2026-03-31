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
from ..types.account_stage_list_response import AccountStageListResponse

__all__ = ["AccountStagesResource", "AsyncAccountStagesResource"]


class AccountStagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountStagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AccountStagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountStagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AccountStagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountStageListResponse:
        """
        Use the List Accounts Stages endpoint to retrieve the IDs for the available
        account stages in your team's Apollo account. This endpoint does not require
        parameters.

        Account stage IDs can be used to
        <a href="https://docs.apollo.io/reference/update-an-account" target="_blank">update
        individual accounts</a> and
        <a href="https://docs.apollo.io/reference/update-account-stage" target="_blank">update
        the account stages for multiple accounts</a> via the Apollo API.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.
        """
        return self._get(
            "/account_stages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountStageListResponse,
        )


class AsyncAccountStagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountStagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountStagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountStagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncAccountStagesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountStageListResponse:
        """
        Use the List Accounts Stages endpoint to retrieve the IDs for the available
        account stages in your team's Apollo account. This endpoint does not require
        parameters.

        Account stage IDs can be used to
        <a href="https://docs.apollo.io/reference/update-an-account" target="_blank">update
        individual accounts</a> and
        <a href="https://docs.apollo.io/reference/update-account-stage" target="_blank">update
        the account stages for multiple accounts</a> via the Apollo API.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.
        """
        return await self._get(
            "/account_stages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountStageListResponse,
        )


class AccountStagesResourceWithRawResponse:
    def __init__(self, account_stages: AccountStagesResource) -> None:
        self._account_stages = account_stages

        self.list = to_raw_response_wrapper(
            account_stages.list,
        )


class AsyncAccountStagesResourceWithRawResponse:
    def __init__(self, account_stages: AsyncAccountStagesResource) -> None:
        self._account_stages = account_stages

        self.list = async_to_raw_response_wrapper(
            account_stages.list,
        )


class AccountStagesResourceWithStreamingResponse:
    def __init__(self, account_stages: AccountStagesResource) -> None:
        self._account_stages = account_stages

        self.list = to_streamed_response_wrapper(
            account_stages.list,
        )


class AsyncAccountStagesResourceWithStreamingResponse:
    def __init__(self, account_stages: AsyncAccountStagesResource) -> None:
        self._account_stages = account_stages

        self.list = async_to_streamed_response_wrapper(
            account_stages.list,
        )
