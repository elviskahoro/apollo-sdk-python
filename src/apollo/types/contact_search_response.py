# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ContactSearchResponse",
    "Breadcrumb",
    "Contact",
    "ContactAccount",
    "ContactAccountAccountRuleConfigStatus",
    "ContactContactCampaignStatus",
    "ContactOrganization",
    "Pagination",
]


class Breadcrumb(BaseModel):
    display_name: Optional[str] = None

    label: Optional[str] = None

    signal_field_name: Optional[str] = None

    value: Optional[str] = None


class ContactAccountAccountRuleConfigStatus(BaseModel):
    id: Optional[str] = None

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    created_at: Optional[object] = None

    key: Optional[str] = None

    rule_action_config_id: Optional[str] = None

    rule_config_id: Optional[str] = None

    status_cd: Optional[str] = None

    updated_at: Optional[object] = None


class ContactAccount(BaseModel):
    id: Optional[str] = None

    account_playbook_statuses: Optional[List[object]] = None

    account_rule_config_statuses: Optional[List[ContactAccountAccountRuleConfigStatus]] = None

    account_stage_id: Optional[object] = None

    alexa_ranking: Optional[int] = None

    angellist_url: Optional[object] = None

    blog_url: Optional[object] = None

    created_at: Optional[str] = None

    creator_id: Optional[object] = None

    crm_owner_id: Optional[str] = None

    crm_record_url: Optional[str] = None

    crunchbase_url: Optional[object] = None

    custom_field_errors: Optional[object] = None

    domain: Optional[str] = None

    existence_level: Optional[str] = None

    facebook_url: Optional[str] = None

    founded_year: Optional[int] = None

    hubspot_id: Optional[str] = None

    label_ids: Optional[List[str]] = None

    languages: Optional[List[object]] = None

    linkedin_uid: Optional[str] = None

    linkedin_url: Optional[str] = None

    logo_url: Optional[str] = None

    modality: Optional[str] = None

    name: Optional[str] = None

    organization_id: Optional[str] = None

    original_source: Optional[str] = None

    owner_id: Optional[str] = None

    parent_account_id: Optional[object] = None

    phone: Optional[str] = None

    phone_status: Optional[str] = None

    primary_domain: Optional[str] = None

    primary_phone: Optional[object] = None

    publicly_traded_exchange: Optional[object] = None

    publicly_traded_symbol: Optional[object] = None

    salesforce_id: Optional[object] = None

    sanitized_phone: Optional[str] = None

    source: Optional[str] = None

    source_display_name: Optional[str] = None

    team_id: Optional[str] = None

    twitter_url: Optional[str] = None

    typed_custom_fields: Optional[object] = None

    website_url: Optional[str] = None


class ContactContactCampaignStatus(BaseModel):
    """
    Contact campaign status object representing the contact's current state in a specific email sequence
    """

    id: str
    """Unique identifier for this contact campaign status record"""

    added_at: datetime
    """Timestamp when the contact was added to this sequence"""

    added_by_user_id: str
    """ID of the user who added this contact to the sequence"""

    emailer_campaign_id: str
    """ID of the email sequence (emailer campaign) this status belongs to"""

    send_email_from_email_account_id: str
    """ID of the email account used to send emails to this contact"""

    send_email_from_user_id: str
    """ID of the user who is sending emails for this contact in the sequence"""

    status: Literal["active", "failed", "paused", "finished"]
    """Current status of the contact in this email sequence"""

    auto_unpause_at: Optional[datetime] = None
    """Scheduled timestamp for automatically unpausing the contact"""

    bcc_emails: Optional[List[str]] = None
    """Email addresses to BCC when sending emails to this contact"""

    cc_emails: Optional[List[str]] = None
    """Email addresses to CC when sending emails to this contact"""

    current_step_id: Optional[str] = None
    """ID of the current step in the sequence that the contact is on"""

    current_step_position: Optional[int] = None
    """Position number of the current step in the sequence (1-based indexing)"""

    failure_reason: Optional[Literal["hard_bounced", "spam_blocked", "bounced", "past_date_failure"]] = None
    """Specific reason for failure if status is 'failed'"""

    finished_at: Optional[datetime] = None
    """Timestamp when the contact finished/completed the sequence"""

    in_response_to_emailer_message_id: Optional[str] = None
    """ID of the emailer message this campaign status is in response to"""

    inactive_reason: Optional[str] = None
    """Reason why the contact is inactive in this sequence, if applicable"""

    manually_set_unpause: Optional[bool] = None
    """Whether the unpause was manually set by a user"""

    paused_at: Optional[datetime] = None
    """Timestamp when the contact was paused in the sequence"""

    send_email_from_email_address: Optional[str] = None
    """Specific email address used to send emails to this contact"""

    to_emails: Optional[List[str]] = None
    """Additional email addresses to include in TO field when sending emails"""


class ContactOrganization(BaseModel):
    id: Optional[str] = None

    alexa_ranking: Optional[int] = None

    angellist_url: Optional[object] = None

    blog_url: Optional[object] = None

    crunchbase_url: Optional[object] = None

    facebook_url: Optional[str] = None

    founded_year: Optional[int] = None

    languages: Optional[List[object]] = None

    linkedin_uid: Optional[str] = None

    linkedin_url: Optional[str] = None

    logo_url: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[object] = None

    primary_domain: Optional[str] = None

    primary_phone: Optional[object] = None

    publicly_traded_exchange: Optional[object] = None

    publicly_traded_symbol: Optional[object] = None

    twitter_url: Optional[str] = None

    website_url: Optional[str] = None


class Contact(BaseModel):
    id: Optional[str] = None

    account: Optional[ContactAccount] = None

    account_id: Optional[str] = None

    account_phone_note: Optional[object] = None

    contact_campaign_statuses: Optional[List[ContactContactCampaignStatus]] = None
    """
    Array of campaign statuses for the contact, showing their participation in
    various email sequences
    """

    contact_emails: Optional[List[object]] = None

    contact_job_change_event: Optional[object] = None

    contact_roles: Optional[List[object]] = None

    contact_rule_config_statuses: Optional[List[object]] = None

    contact_stage_id: Optional[str] = None

    created_at: Optional[str] = None

    creator_id: Optional[str] = None

    crm_id: Optional[object] = None

    crm_owner_id: Optional[object] = None

    crm_record_url: Optional[object] = None

    custom_field_errors: Optional[object] = None

    direct_dial_enrichment_failed_at: Optional[object] = None

    direct_dial_status: Optional[object] = None

    email: Optional[str] = None

    email_domain_catchall: Optional[bool] = None

    email_from_customer: Optional[bool] = None

    email_needs_tickling: Optional[object] = None

    email_source: Optional[object] = None

    email_status: Optional[str] = None

    email_status_unavailable_reason: Optional[object] = None

    email_true_status: Optional[str] = None

    email_unsubscribed: Optional[object] = None

    emailer_campaign_ids: Optional[List[object]] = None

    existence_level: Optional[str] = None

    extrapolated_email_confidence: Optional[object] = None

    first_name: Optional[str] = None

    free_domain: Optional[bool] = None

    has_email_arcgate_request: Optional[bool] = None

    has_pending_email_arcgate_request: Optional[bool] = None

    headline: Optional[object] = None

    hubspot_company_id: Optional[object] = None

    hubspot_vid: Optional[object] = None

    intent_strength: Optional[object] = None

    is_likely_to_engage: Optional[bool] = None

    label_ids: Optional[List[object]] = None

    last_activity_date: Optional[object] = None

    last_name: Optional[str] = None

    linkedin_uid: Optional[object] = None

    linkedin_url: Optional[object] = None

    merged_crm_ids: Optional[object] = None

    name: Optional[str] = None

    organization: Optional[ContactOrganization] = None

    organization_id: Optional[str] = None

    organization_name: Optional[str] = None

    original_source: Optional[str] = None

    owner_id: Optional[str] = None

    person_id: Optional[object] = None

    phone_numbers: Optional[List[object]] = None

    photo_url: Optional[object] = None

    present_raw_address: Optional[object] = None

    queued_for_crm_push: Optional[bool] = None

    salesforce_account_id: Optional[object] = None

    salesforce_contact_id: Optional[object] = None

    salesforce_id: Optional[object] = None

    salesforce_lead_id: Optional[object] = None

    sanitized_phone: Optional[object] = None

    show_intent: Optional[bool] = None

    source: Optional[str] = None

    source_display_name: Optional[str] = None

    suggested_from_rule_engine_config_id: Optional[object] = None

    title: Optional[str] = None

    twitter_url: Optional[object] = None

    typed_custom_fields: Optional[object] = None

    updated_at: Optional[str] = None

    updated_email_true_status: Optional[bool] = None


class Pagination(BaseModel):
    page: Optional[int] = None

    per_page: Optional[int] = None

    total_entries: Optional[int] = None

    total_pages: Optional[int] = None


class ContactSearchResponse(BaseModel):
    breadcrumbs: Optional[List[Breadcrumb]] = None

    contacts: Optional[List[Contact]] = None

    disable_eu_prospecting: Optional[bool] = None

    has_join: Optional[bool] = None

    num_fetch_result: Optional[object] = None

    pagination: Optional[Pagination] = None

    partial_results_limit: Optional[int] = None

    partial_results_only: Optional[bool] = None
