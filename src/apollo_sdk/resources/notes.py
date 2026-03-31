# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import note_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.note_list_response import NoteListResponse

__all__ = ["NotesResource", "AsyncNotesResource"]


class NotesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return NotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return NotesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        calendar_event_id: str | Omit = omit,
        contact_id: str | Omit = omit,
        contact_ids: SequenceNotStr[str] | Omit = omit,
        conversation_id: str | Omit = omit,
        conversation_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        opportunity_id: str | Omit = omit,
        skip: int | Omit = omit,
        sort_by_field: Literal["created_at", "updated_at"] | Omit = omit,
        sort_direction: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NoteListResponse:
        """
        The Get a List of Notes endpoint retrieves notes associated with a specific
        contact, account, opportunity, calendar event, or conversation in your Apollo
        account.

        **Required:** You must provide at least one of the following relation
        parameters: `account_id`, `contact_id`, `contact_ids`, `opportunity_id`,
        `calendar_event_id`, `conversation_id`, or `conversation_ids`. If none of these
        are provided, the API returns a `400` error.

        Use the `sort_by_field` and `sort_direction` parameters to control the order of
        the results. Use `skip` and `limit` for pagination.

        Args:
          account_id: The ID of the account whose notes you want to retrieve.

              Example: `60a5c0b8e4b0c7001c4f5678`

          calendar_event_id: The ID of the calendar event whose notes you want to retrieve.

              Example: `60a5c0b8e4b0c7001c4f3456`

          contact_id: The ID of the contact whose notes you want to retrieve.

              Example: `60a5c0b8e4b0c7001c4f1234`

          contact_ids: An array of contact IDs to filter notes by multiple contacts.

          conversation_id: The ID of the conversation whose notes you want to retrieve.

              Example: `60a5c0b8e4b0c7001c4f7890`

          conversation_ids: An array of conversation IDs to filter notes by multiple conversations.

          limit: The maximum number of notes to return per request. Defaults to `25`. Maximum
              value is `100`.

          opportunity_id: The ID of the opportunity whose notes you want to retrieve.

              Example: `60a5c0b8e4b0c7001c4f9012`

          skip: The number of notes to skip for pagination. Must be a non-negative integer.
              Defaults to `0`.

          sort_by_field: The field to sort results by. Defaults to `created_at`.

          sort_direction: The direction to sort results. Defaults to `desc`.

          start_date: Filter notes created on or after this date. Must be a valid date string.

              Example: `2024-01-01`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/notes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "calendar_event_id": calendar_event_id,
                        "contact_id": contact_id,
                        "contact_ids": contact_ids,
                        "conversation_id": conversation_id,
                        "conversation_ids": conversation_ids,
                        "limit": limit,
                        "opportunity_id": opportunity_id,
                        "skip": skip,
                        "sort_by_field": sort_by_field,
                        "sort_direction": sort_direction,
                        "start_date": start_date,
                    },
                    note_list_params.NoteListParams,
                ),
            ),
            cast_to=NoteListResponse,
        )


class AsyncNotesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncNotesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        calendar_event_id: str | Omit = omit,
        contact_id: str | Omit = omit,
        contact_ids: SequenceNotStr[str] | Omit = omit,
        conversation_id: str | Omit = omit,
        conversation_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        opportunity_id: str | Omit = omit,
        skip: int | Omit = omit,
        sort_by_field: Literal["created_at", "updated_at"] | Omit = omit,
        sort_direction: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NoteListResponse:
        """
        The Get a List of Notes endpoint retrieves notes associated with a specific
        contact, account, opportunity, calendar event, or conversation in your Apollo
        account.

        **Required:** You must provide at least one of the following relation
        parameters: `account_id`, `contact_id`, `contact_ids`, `opportunity_id`,
        `calendar_event_id`, `conversation_id`, or `conversation_ids`. If none of these
        are provided, the API returns a `400` error.

        Use the `sort_by_field` and `sort_direction` parameters to control the order of
        the results. Use `skip` and `limit` for pagination.

        Args:
          account_id: The ID of the account whose notes you want to retrieve.

              Example: `60a5c0b8e4b0c7001c4f5678`

          calendar_event_id: The ID of the calendar event whose notes you want to retrieve.

              Example: `60a5c0b8e4b0c7001c4f3456`

          contact_id: The ID of the contact whose notes you want to retrieve.

              Example: `60a5c0b8e4b0c7001c4f1234`

          contact_ids: An array of contact IDs to filter notes by multiple contacts.

          conversation_id: The ID of the conversation whose notes you want to retrieve.

              Example: `60a5c0b8e4b0c7001c4f7890`

          conversation_ids: An array of conversation IDs to filter notes by multiple conversations.

          limit: The maximum number of notes to return per request. Defaults to `25`. Maximum
              value is `100`.

          opportunity_id: The ID of the opportunity whose notes you want to retrieve.

              Example: `60a5c0b8e4b0c7001c4f9012`

          skip: The number of notes to skip for pagination. Must be a non-negative integer.
              Defaults to `0`.

          sort_by_field: The field to sort results by. Defaults to `created_at`.

          sort_direction: The direction to sort results. Defaults to `desc`.

          start_date: Filter notes created on or after this date. Must be a valid date string.

              Example: `2024-01-01`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/notes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "calendar_event_id": calendar_event_id,
                        "contact_id": contact_id,
                        "contact_ids": contact_ids,
                        "conversation_id": conversation_id,
                        "conversation_ids": conversation_ids,
                        "limit": limit,
                        "opportunity_id": opportunity_id,
                        "skip": skip,
                        "sort_by_field": sort_by_field,
                        "sort_direction": sort_direction,
                        "start_date": start_date,
                    },
                    note_list_params.NoteListParams,
                ),
            ),
            cast_to=NoteListResponse,
        )


class NotesResourceWithRawResponse:
    def __init__(self, notes: NotesResource) -> None:
        self._notes = notes

        self.list = to_raw_response_wrapper(
            notes.list,
        )


class AsyncNotesResourceWithRawResponse:
    def __init__(self, notes: AsyncNotesResource) -> None:
        self._notes = notes

        self.list = async_to_raw_response_wrapper(
            notes.list,
        )


class NotesResourceWithStreamingResponse:
    def __init__(self, notes: NotesResource) -> None:
        self._notes = notes

        self.list = to_streamed_response_wrapper(
            notes.list,
        )


class AsyncNotesResourceWithStreamingResponse:
    def __init__(self, notes: AsyncNotesResource) -> None:
        self._notes = notes

        self.list = async_to_streamed_response_wrapper(
            notes.list,
        )
