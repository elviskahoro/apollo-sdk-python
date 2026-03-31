# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

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
from ..types.typed_custom_field_list_response import TypedCustomFieldListResponse

__all__ = ["TypedCustomFieldsResource", "AsyncTypedCustomFieldsResource"]


class TypedCustomFieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TypedCustomFieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TypedCustomFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TypedCustomFieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return TypedCustomFieldsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypedCustomFieldListResponse:
        """This endpoint is deprecated.

        To achieve the same result, use the
        <a href="https://docs.apollo.io/reference/get-a-list-of-fields" target="_blank">Fields
        endpoint</a> (use `source: custom` to get custom fields only)

        Use the Get a List of Custom Fields endpoint to retrieve information about all
        of the custom fields that have been created in your Apollo account.

        This endpoint does not require any parameters.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.
        """
        return self._get(
            "/typed_custom_fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypedCustomFieldListResponse,
        )


class AsyncTypedCustomFieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTypedCustomFieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTypedCustomFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTypedCustomFieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncTypedCustomFieldsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypedCustomFieldListResponse:
        """This endpoint is deprecated.

        To achieve the same result, use the
        <a href="https://docs.apollo.io/reference/get-a-list-of-fields" target="_blank">Fields
        endpoint</a> (use `source: custom` to get custom fields only)

        Use the Get a List of Custom Fields endpoint to retrieve information about all
        of the custom fields that have been created in your Apollo account.

        This endpoint does not require any parameters.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.
        """
        return await self._get(
            "/typed_custom_fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypedCustomFieldListResponse,
        )


class TypedCustomFieldsResourceWithRawResponse:
    def __init__(self, typed_custom_fields: TypedCustomFieldsResource) -> None:
        self._typed_custom_fields = typed_custom_fields

        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                typed_custom_fields.list,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncTypedCustomFieldsResourceWithRawResponse:
    def __init__(self, typed_custom_fields: AsyncTypedCustomFieldsResource) -> None:
        self._typed_custom_fields = typed_custom_fields

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                typed_custom_fields.list,  # pyright: ignore[reportDeprecated],
            )
        )


class TypedCustomFieldsResourceWithStreamingResponse:
    def __init__(self, typed_custom_fields: TypedCustomFieldsResource) -> None:
        self._typed_custom_fields = typed_custom_fields

        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                typed_custom_fields.list,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncTypedCustomFieldsResourceWithStreamingResponse:
    def __init__(self, typed_custom_fields: AsyncTypedCustomFieldsResource) -> None:
        self._typed_custom_fields = typed_custom_fields

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                typed_custom_fields.list,  # pyright: ignore[reportDeprecated],
            )
        )
