# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ContactCreateResponse", "Contact", "ContactContactCampaignStatus", "ContactPhoneNumber", "Label"]


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


class ContactPhoneNumber(BaseModel):
    dialer_flags: Optional[object] = None

    dnc_other_info: Optional[object] = None

    dnc_status: Optional[object] = None

    position: Optional[int] = None

    raw_number: Optional[str] = None

    sanitized_number: Optional[str] = None

    status: Optional[str] = None

    type: Optional[str] = None


class Contact(BaseModel):
    id: Optional[str] = None

    account_id: Optional[str] = None

    account_phone_note: Optional[object] = None

    city: Optional[str] = None

    contact_campaign_statuses: Optional[List[ContactContactCampaignStatus]] = None
    """
    Array of campaign statuses for the contact, showing their participation in
    various email sequences
    """

    contact_emails: Optional[List[object]] = None

    contact_roles: Optional[List[object]] = None

    contact_rule_config_statuses: Optional[List[object]] = None

    contact_stage_id: Optional[str] = None

    country: Optional[str] = None

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

    label_ids: Optional[List[str]] = None

    last_activity_date: Optional[object] = None

    last_name: Optional[str] = None

    linkedin_uid: Optional[object] = None

    linkedin_url: Optional[object] = None

    merged_crm_ids: Optional[object] = None

    name: Optional[str] = None

    next_contact_id: Optional[object] = None

    organization_id: Optional[str] = None

    organization_name: Optional[str] = None

    original_source: Optional[str] = None

    owner_id: Optional[str] = None

    person_id: Optional[object] = None

    phone_numbers: Optional[List[ContactPhoneNumber]] = None

    photo_url: Optional[object] = None

    present_raw_address: Optional[str] = None

    queued_for_crm_push: Optional[bool] = None

    salesforce_account_id: Optional[object] = None

    salesforce_contact_id: Optional[object] = None

    salesforce_id: Optional[object] = None

    salesforce_lead_id: Optional[object] = None

    sanitized_phone: Optional[str] = None

    show_intent: Optional[bool] = None

    source: Optional[str] = None

    source_display_name: Optional[str] = None

    state: Optional[str] = None

    suggested_from_rule_engine_config_id: Optional[object] = None

    time_zone: Optional[str] = None

    title: Optional[str] = None

    twitter_url: Optional[object] = None

    typed_custom_fields: Optional[object] = None

    updated_at: Optional[str] = None

    updated_email_true_status: Optional[bool] = None


class Label(BaseModel):
    id: Optional[str] = None

    cached_count: Optional[int] = None

    created_at: Optional[str] = None

    modality: Optional[str] = None

    name: Optional[str] = None

    updated_at: Optional[str] = None

    user_id: Optional[str] = None


class ContactCreateResponse(BaseModel):
    contact: Optional[Contact] = None

    labels: Optional[List[Label]] = None
