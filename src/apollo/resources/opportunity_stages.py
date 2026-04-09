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
from ..types.opportunity_stage_list_response import OpportunityStageListResponse

__all__ = ["OpportunityStagesResource", "AsyncOpportunityStagesResource"]


class OpportunityStagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpportunityStagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OpportunityStagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpportunityStagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return OpportunityStagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpportunityStageListResponse:
        """
        Use the List Deal Stages endpoint to retrieve information about every deal stage
        that is available in your team's Apollo account.

        The `id` value for each deal stage can be used to set the stage when
        <a href="https://docs.apollo.io/reference/create-deal" target="_blank">creating
        a deal</a> or
        <a href="https://docs.apollo.io/reference/update-deal" target="_blank">updating
        a deal</a> via the Apollo API.

        This endpoint also requires a master API key. If you attempt to call the
        endpoint without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.
        """
        return self._get(
            "/opportunity_stages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpportunityStageListResponse,
        )


class AsyncOpportunityStagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpportunityStagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOpportunityStagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpportunityStagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncOpportunityStagesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpportunityStageListResponse:
        """
        Use the List Deal Stages endpoint to retrieve information about every deal stage
        that is available in your team's Apollo account.

        The `id` value for each deal stage can be used to set the stage when
        <a href="https://docs.apollo.io/reference/create-deal" target="_blank">creating
        a deal</a> or
        <a href="https://docs.apollo.io/reference/update-deal" target="_blank">updating
        a deal</a> via the Apollo API.

        This endpoint also requires a master API key. If you attempt to call the
        endpoint without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.
        """
        return await self._get(
            "/opportunity_stages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpportunityStageListResponse,
        )


class OpportunityStagesResourceWithRawResponse:
    def __init__(self, opportunity_stages: OpportunityStagesResource) -> None:
        self._opportunity_stages = opportunity_stages

        self.list = to_raw_response_wrapper(
            opportunity_stages.list,
        )


class AsyncOpportunityStagesResourceWithRawResponse:
    def __init__(self, opportunity_stages: AsyncOpportunityStagesResource) -> None:
        self._opportunity_stages = opportunity_stages

        self.list = async_to_raw_response_wrapper(
            opportunity_stages.list,
        )


class OpportunityStagesResourceWithStreamingResponse:
    def __init__(self, opportunity_stages: OpportunityStagesResource) -> None:
        self._opportunity_stages = opportunity_stages

        self.list = to_streamed_response_wrapper(
            opportunity_stages.list,
        )


class AsyncOpportunityStagesResourceWithStreamingResponse:
    def __init__(self, opportunity_stages: AsyncOpportunityStagesResource) -> None:
        self._opportunity_stages = opportunity_stages

        self.list = async_to_streamed_response_wrapper(
            opportunity_stages.list,
        )
