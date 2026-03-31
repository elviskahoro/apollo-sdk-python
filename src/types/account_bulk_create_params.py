# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AccountBulkCreateParams", "Account"]


class AccountBulkCreateParams(TypedDict, total=False):
    accounts: Required[Iterable[Account]]
    """Array of account attribute objects (maximum 100 accounts per request)"""

    append_label_names: SequenceNotStr[str]
    """Array of label names to add to ALL accounts in this request"""

    run_dedupe: bool
    """Enable aggressive deduplication by domain, organization_id, and name.

    When false (default), only matches by CRM IDs. When true, also matches by
    domain, organization_id, and name. Existing accounts are returned without
    modification in both modes
    """


class Account(TypedDict, total=False):
    account_stage_id: str
    """Account stage/pipeline stage ID (BSON::ObjectId format)"""

    domain: str
    """Company domain (e.g., 'example.com')"""

    facebook_url: str
    """Facebook page URL"""

    hubspot_id: str
    """HubSpot company ID for CRM integration"""

    linkedin_url: str
    """LinkedIn company page URL"""

    merged_crm_ids: SequenceNotStr[str]
    """Additional CRM IDs for deduplication"""

    name: str
    """Account name"""

    organization_id: str
    """Apollo organization ID"""

    owner_id: str
    """Account owner user ID (BSON::ObjectId format).

    Defaults to current user if not provided
    """

    parent_account_id: str
    """Parent account ID for account hierarchy (BSON::ObjectId format)"""

    phone: str
    """Company phone number"""

    phone_status_cd: str
    """Phone validation status"""

    raw_address: str
    """Company address"""

    salesforce_id: str
    """Salesforce account ID for CRM integration"""

    twitter_url: str
    """Twitter profile URL"""

    typed_custom_fields: Dict[str, str]
    """
    Custom field values as key-value pairs where key is the field_id and value is
    the field_value
    """
