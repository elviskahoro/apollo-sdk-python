# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ContactStagesResource", "AsyncContactStagesResource"]


class ContactStagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContactStagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ContactStagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactStagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return ContactStagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Use the List Contact Stages endpoint to retrieve the IDs for the available
        contact stages in your team's Apollo account.

        Contact stage IDs can be used to
        <a href="https://docs.apollo.io/reference/update-a-contact" target="_blank">update
        invidual contacts</a> and
        <a href="https://docs.apollo.io/reference/update-contact-stage" target="_blank">update
        the contact stages for multiple contacts</a> via the Apollo API.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/contact_stages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncContactStagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContactStagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContactStagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactStagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncContactStagesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Use the List Contact Stages endpoint to retrieve the IDs for the available
        contact stages in your team's Apollo account.

        Contact stage IDs can be used to
        <a href="https://docs.apollo.io/reference/update-a-contact" target="_blank">update
        invidual contacts</a> and
        <a href="https://docs.apollo.io/reference/update-contact-stage" target="_blank">update
        the contact stages for multiple contacts</a> via the Apollo API.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/contact_stages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ContactStagesResourceWithRawResponse:
    def __init__(self, contact_stages: ContactStagesResource) -> None:
        self._contact_stages = contact_stages

        self.list = to_raw_response_wrapper(
            contact_stages.list,
        )


class AsyncContactStagesResourceWithRawResponse:
    def __init__(self, contact_stages: AsyncContactStagesResource) -> None:
        self._contact_stages = contact_stages

        self.list = async_to_raw_response_wrapper(
            contact_stages.list,
        )


class ContactStagesResourceWithStreamingResponse:
    def __init__(self, contact_stages: ContactStagesResource) -> None:
        self._contact_stages = contact_stages

        self.list = to_streamed_response_wrapper(
            contact_stages.list,
        )


class AsyncContactStagesResourceWithStreamingResponse:
    def __init__(self, contact_stages: AsyncContactStagesResource) -> None:
        self._contact_stages = contact_stages

        self.list = async_to_streamed_response_wrapper(
            contact_stages.list,
        )
