# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["NoteListResponse", "Note"]


class Note(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the note."""

    account_id: Optional[str] = None
    """The ID of the associated account."""

    account_ids: Optional[List[str]] = None
    """Array of associated account IDs."""

    calendar_event_ids: Optional[List[str]] = None
    """Array of associated calendar event IDs."""

    contact_id: Optional[str] = None
    """The ID of the associated contact."""

    contact_ids: Optional[List[str]] = None
    """Array of associated contact IDs."""

    content: Optional[str] = None
    """The content of the note."""

    conversation_id: Optional[str] = None
    """The ID of the associated conversation."""

    conversation_ids: Optional[List[str]] = None
    """Array of associated conversation IDs."""

    created_at: Optional[str] = None
    """The timestamp when the note was created."""

    crm_notes: Optional[List[object]] = None
    """Array of associated CRM note records."""

    is_org_chart_note: Optional[bool] = None
    """Whether this note is an org chart note."""

    opportunity_id: Optional[str] = None
    """The ID of the associated opportunity."""

    opportunity_ids: Optional[List[str]] = None
    """Array of associated opportunity IDs."""

    pinned_to_top: Optional[bool] = None
    """Whether the note is pinned to the top."""

    system: Optional[bool] = None
    """Whether this is a system-generated note."""

    updated_at: Optional[str] = None
    """The timestamp when the note was last updated."""

    user_id: Optional[str] = None
    """The ID of the user who created the note."""


class NoteListResponse(BaseModel):
    notes: Optional[List[Note]] = None
