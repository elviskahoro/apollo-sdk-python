# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ContactBulkCreateParams", "Contact", "ContactContactEmail", "ContactPhoneNumber"]


class ContactBulkCreateParams(TypedDict, total=False):
    contacts: Required[Iterable[Contact]]
    """Array of contact objects to create (maximum 100 contacts per request)"""

    append_label_names: SequenceNotStr[str]
    """Array of label names to add to ALL contacts in this request"""

    run_dedupe: bool
    """Enable full deduplication across all sources.

    When false (default), creates duplicates for non-email_import sources and merges
    with email_import placeholders only. When true, returns existing contacts
    without modifying them (except email_import placeholders which are still
    merged). Matches by email, CRM IDs, or name + organization
    """


class ContactContactEmail(TypedDict, total=False):
    email: str

    position: int


class ContactPhoneNumber(TypedDict, total=False):
    position: int

    raw_number: str


class Contact(TypedDict, total=False):
    account_id: str
    """Associated account ID"""

    contact_emails: Iterable[ContactContactEmail]
    """Array of email objects with position"""

    contact_role_type_ids: SequenceNotStr[str]
    """Array of contact role type IDs"""

    contact_stage_id: str
    """Contact stage ID"""

    email: str
    """Contact's email address"""

    facebook_url: str
    """Facebook profile URL"""

    first_name: str
    """Contact's first name"""

    hubspot_id: str
    """HubSpot ID for matching and deduplication"""

    last_name: str
    """Contact's last name"""

    linkedin_url: str
    """LinkedIn profile URL"""

    organization_id: str
    """Associated organization ID"""

    organization_name: str
    """Company/organization name"""

    outreach_id: str
    """Outreach.io ID"""

    owner_id: str
    """Contact owner user ID (defaults to current user if not provided)"""

    phone: str
    """Phone number"""

    phone_numbers: Iterable[ContactPhoneNumber]
    """Array of phone number objects"""

    phone_status_cd: str
    """Phone validation status"""

    photo_url: str
    """Profile photo URL"""

    present_raw_address: str
    """Physical address"""

    primary_title: str
    """Primary job title (takes precedence over title)"""

    salesforce_account_id: str
    """Salesforce Account ID"""

    salesforce_contact_id: str
    """Salesforce Contact ID for matching"""

    salesforce_id: str
    """Salesforce ID for matching and deduplication"""

    salesforce_lead_id: str
    """Salesforce Lead ID"""

    salesloft_id: str
    """SalesLoft ID"""

    title: str
    """Contact's job title"""

    twitter_url: str
    """Twitter profile URL"""

    typed_custom_fields: Dict[str, str]
    """
    Custom field values as key-value pairs where key is the field_id and value is
    the field_value
    """
