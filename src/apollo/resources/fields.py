# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import field_list_params, field_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.field_list_response import FieldListResponse
from ..types.field_create_response import FieldCreateResponse

__all__ = ["FieldsResource", "AsyncFieldsResource"]


class FieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return FieldsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        label: str | Omit = omit,
        meta: field_create_params.Meta | Omit = omit,
        modality: Literal["contact", "account", "opportunity"] | Omit = omit,
        type: Literal["string", "textarea", "number", "date", "datetime", "boolean"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FieldCreateResponse:
        """
        The Create a Custom Field endpoint lets you add custom fields to your Apollo
        account, helping your team capture unique details about
        <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498825869-Create-Custom-Contact-Fields" target="_blank">contacts</a>,
        <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498754445-Create-Custom-Account-Fields" target="_blank">accounts</a>,
        or
        <a href="https://knowledge.apollo.io/hc/en-us/articles/4415062486669-Create-a-Deal" target="_blank">deals</a>.
        Use these fields to enhance your sequences and deliver more personalized,
        relevant outreach.

        Args:
          label: Name of the custom field you want to create. Example: `Test Name`

          modality: The modality of the custom field you want to create. Example: `contact`

          type: What kind of custom field you want to create. Example: `textarea`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fields",
            body=maybe_transform(
                {
                    "label": label,
                    "meta": meta,
                    "modality": modality,
                    "type": type,
                },
                field_create_params.FieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldCreateResponse,
        )

    def list(
        self,
        *,
        source: Literal["system", "custom", "crm_synced"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FieldListResponse:
        """
        Use the Get a List of Fields endpoint to retrieve information about all of the
        fields that exist in your Apollo account.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fields",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"source": source}, field_list_params.FieldListParams),
            ),
            cast_to=FieldListResponse,
        )


class AsyncFieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncFieldsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        label: str | Omit = omit,
        meta: field_create_params.Meta | Omit = omit,
        modality: Literal["contact", "account", "opportunity"] | Omit = omit,
        type: Literal["string", "textarea", "number", "date", "datetime", "boolean"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FieldCreateResponse:
        """
        The Create a Custom Field endpoint lets you add custom fields to your Apollo
        account, helping your team capture unique details about
        <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498825869-Create-Custom-Contact-Fields" target="_blank">contacts</a>,
        <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498754445-Create-Custom-Account-Fields" target="_blank">accounts</a>,
        or
        <a href="https://knowledge.apollo.io/hc/en-us/articles/4415062486669-Create-a-Deal" target="_blank">deals</a>.
        Use these fields to enhance your sequences and deliver more personalized,
        relevant outreach.

        Args:
          label: Name of the custom field you want to create. Example: `Test Name`

          modality: The modality of the custom field you want to create. Example: `contact`

          type: What kind of custom field you want to create. Example: `textarea`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fields",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "meta": meta,
                    "modality": modality,
                    "type": type,
                },
                field_create_params.FieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldCreateResponse,
        )

    async def list(
        self,
        *,
        source: Literal["system", "custom", "crm_synced"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FieldListResponse:
        """
        Use the Get a List of Fields endpoint to retrieve information about all of the
        fields that exist in your Apollo account.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fields",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"source": source}, field_list_params.FieldListParams),
            ),
            cast_to=FieldListResponse,
        )


class FieldsResourceWithRawResponse:
    def __init__(self, fields: FieldsResource) -> None:
        self._fields = fields

        self.create = to_raw_response_wrapper(
            fields.create,
        )
        self.list = to_raw_response_wrapper(
            fields.list,
        )


class AsyncFieldsResourceWithRawResponse:
    def __init__(self, fields: AsyncFieldsResource) -> None:
        self._fields = fields

        self.create = async_to_raw_response_wrapper(
            fields.create,
        )
        self.list = async_to_raw_response_wrapper(
            fields.list,
        )


class FieldsResourceWithStreamingResponse:
    def __init__(self, fields: FieldsResource) -> None:
        self._fields = fields

        self.create = to_streamed_response_wrapper(
            fields.create,
        )
        self.list = to_streamed_response_wrapper(
            fields.list,
        )


class AsyncFieldsResourceWithStreamingResponse:
    def __init__(self, fields: AsyncFieldsResource) -> None:
        self._fields = fields

        self.create = async_to_streamed_response_wrapper(
            fields.create,
        )
        self.list = async_to_streamed_response_wrapper(
            fields.list,
        )
