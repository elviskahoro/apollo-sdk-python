# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ContactBulkUpdateParams", "ContactAttribute"]


class ContactBulkUpdateParams(TypedDict, total=False):
    account_id: str
    """When using contact_ids, apply this account ID to all contacts"""

    async_: Annotated[bool, PropertyInfo(alias="async")]
    """Force asynchronous processing. Automatically enabled for >100 contacts."""

    contact_attributes: Iterable[ContactAttribute]
    """Array of contact objects with individual updates.

    Use this for applying different updates to each contact.
    """

    contact_ids: SequenceNotStr[str]
    """Array of contact IDs to update with the same values.

    Use this for applying the same updates to multiple contacts.
    """

    email: str
    """When using contact_ids, apply this email to all contacts"""

    first_name: str
    """When using contact_ids, apply this first name to all contacts"""

    last_name: str
    """When using contact_ids, apply this last name to all contacts"""

    linkedin_url: str
    """When using contact_ids, apply this LinkedIn URL to all contacts"""

    organization_name: str
    """When using contact_ids, apply this organization name to all contacts"""

    owner_id: str
    """When using contact_ids, apply this owner to all contacts"""

    present_raw_address: str
    """When using contact_ids, apply this address to all contacts"""

    title: str
    """When using contact_ids, apply this title to all contacts"""

    typed_custom_fields: Dict[str, str]
    """When using contact_ids, apply these custom fields to all contacts"""

    visible_entity_ids: SequenceNotStr[str]
    """Specific contact IDs to return in the response (for performance)"""


class ContactAttribute(TypedDict, total=False):
    id: Required[str]
    """The contact ID to update"""

    account_id: str
    """The Apollo account ID to associate with the contact"""

    email: str
    """The contact's email address"""

    first_name: str
    """The contact's first name"""

    last_name: str
    """The contact's last name"""

    linkedin_url: str
    """The contact's LinkedIn profile URL"""

    organization_name: str
    """The contact's organization name"""

    owner_id: str
    """The Apollo user ID to assign as owner"""

    present_raw_address: str
    """The contact's location"""

    title: str
    """The contact's job title"""

    typed_custom_fields: Dict[str, str]
    """Custom field values as key-value pairs"""
