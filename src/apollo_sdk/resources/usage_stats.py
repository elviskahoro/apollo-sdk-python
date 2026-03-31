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

__all__ = ["UsageStatsResource", "AsyncUsageStatsResource"]


class UsageStatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageStatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return UsageStatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageStatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return UsageStatsResourceWithStreamingResponse(self)

    def api_usage_stats(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """post_apiusage"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/usage_stats/api_usage_stats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUsageStatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageStatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageStatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageStatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncUsageStatsResourceWithStreamingResponse(self)

    async def api_usage_stats(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """post_apiusage"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/usage_stats/api_usage_stats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UsageStatsResourceWithRawResponse:
    def __init__(self, usage_stats: UsageStatsResource) -> None:
        self._usage_stats = usage_stats

        self.api_usage_stats = to_raw_response_wrapper(
            usage_stats.api_usage_stats,
        )


class AsyncUsageStatsResourceWithRawResponse:
    def __init__(self, usage_stats: AsyncUsageStatsResource) -> None:
        self._usage_stats = usage_stats

        self.api_usage_stats = async_to_raw_response_wrapper(
            usage_stats.api_usage_stats,
        )


class UsageStatsResourceWithStreamingResponse:
    def __init__(self, usage_stats: UsageStatsResource) -> None:
        self._usage_stats = usage_stats

        self.api_usage_stats = to_streamed_response_wrapper(
            usage_stats.api_usage_stats,
        )


class AsyncUsageStatsResourceWithStreamingResponse:
    def __init__(self, usage_stats: AsyncUsageStatsResource) -> None:
        self._usage_stats = usage_stats

        self.api_usage_stats = async_to_streamed_response_wrapper(
            usage_stats.api_usage_stats,
        )
