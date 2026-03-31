# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["NoteListParams"]


class NoteListParams(TypedDict, total=False):
    account_id: str
    """The ID of the account whose notes you want to retrieve.

    Example: `60a5c0b8e4b0c7001c4f5678`
    """

    calendar_event_id: str
    """The ID of the calendar event whose notes you want to retrieve.

    Example: `60a5c0b8e4b0c7001c4f3456`
    """

    contact_id: str
    """The ID of the contact whose notes you want to retrieve.

    Example: `60a5c0b8e4b0c7001c4f1234`
    """

    contact_ids: SequenceNotStr[str]
    """An array of contact IDs to filter notes by multiple contacts."""

    conversation_id: str
    """The ID of the conversation whose notes you want to retrieve.

    Example: `60a5c0b8e4b0c7001c4f7890`
    """

    conversation_ids: SequenceNotStr[str]
    """An array of conversation IDs to filter notes by multiple conversations."""

    limit: int
    """The maximum number of notes to return per request.

    Defaults to `25`. Maximum value is `100`.
    """

    opportunity_id: str
    """The ID of the opportunity whose notes you want to retrieve.

    Example: `60a5c0b8e4b0c7001c4f9012`
    """

    skip: int
    """The number of notes to skip for pagination.

    Must be a non-negative integer. Defaults to `0`.
    """

    sort_by_field: Literal["created_at", "updated_at"]
    """The field to sort results by. Defaults to `created_at`."""

    sort_direction: Literal["asc", "desc"]
    """The direction to sort results. Defaults to `desc`."""

    start_date: str
    """Filter notes created on or after this date. Must be a valid date string.

    Example: `2024-01-01`
    """
