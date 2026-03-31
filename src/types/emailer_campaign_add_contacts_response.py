# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "EmailerCampaignAddContactsResponse",
    "Contact",
    "ContactContactCampaignStatus",
    "ContactContactEmail",
    "ContactPhoneNumber",
    "EmailerCampaign",
    "EmailerCampaignContactStatuses",
    "EmailerCampaignSharingPermission",
    "EmailerCampaignSharingPermissionSharingAccess",
    "EmailerStep",
    "EmailerStepCounts",
    "EmailerTouch",
    "SkippedContactIDs",
    "Team",
]


class ContactContactCampaignStatus(BaseModel):
    id: Optional[str] = None

    added_at: Optional[datetime] = None

    emailer_campaign_id: Optional[str] = None

    inactive_reason: Optional[str] = None

    send_email_from_email_account_id: Optional[str] = None

    send_email_from_email_address: Optional[str] = None

    status: Optional[str] = None


class ContactContactEmail(BaseModel):
    email: Optional[str] = None

    email_md5: Optional[str] = None

    email_sha256: Optional[str] = None

    email_status: Optional[str] = None

    email_true_status: Optional[str] = None

    free_domain: Optional[bool] = None

    position: Optional[int] = None

    source: Optional[str] = None


class ContactPhoneNumber(BaseModel):
    position: Optional[int] = None

    raw_number: Optional[str] = None

    sanitized_number: Optional[str] = None

    source_name: Optional[str] = None

    status: Optional[str] = None

    type: Optional[str] = None


class Contact(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the contact"""

    account_id: Optional[str] = None

    city: Optional[str] = None

    contact_campaign_statuses: Optional[List[ContactContactCampaignStatus]] = None

    contact_emails: Optional[List[ContactContactEmail]] = None

    contact_stage_id: Optional[str] = None

    country: Optional[str] = None

    created_at: Optional[datetime] = None

    creator_id: Optional[str] = None

    email: Optional[str] = None

    email_domain_catchall: Optional[bool] = None

    email_status: Optional[str] = None

    emailer_campaign_ids: Optional[List[str]] = None

    first_name: Optional[str] = None

    free_domain: Optional[bool] = None

    label_ids: Optional[List[str]] = None

    last_name: Optional[str] = None

    linkedin_url: Optional[str] = None

    name: Optional[str] = None
    """Full name of the contact"""

    organization_id: Optional[str] = None

    organization_name: Optional[str] = None

    original_source: Optional[str] = None

    owner_id: Optional[str] = None

    person_id: Optional[str] = None

    phone_numbers: Optional[List[ContactPhoneNumber]] = None

    sanitized_phone: Optional[str] = None

    source: Optional[str] = None

    state: Optional[str] = None

    time_zone: Optional[str] = None

    title: Optional[str] = None

    typed_custom_fields: Optional[object] = None

    updated_at: Optional[datetime] = None


class EmailerCampaignContactStatuses(BaseModel):
    active: Union[int, Literal["loading"], None] = None

    bounced: Union[int, Literal["loading"], None] = None

    failed: Optional[int] = None

    finished: Union[int, Literal["loading"], None] = None

    paused: Union[int, Literal["loading"], None] = None


class EmailerCampaignSharingPermissionSharingAccess(BaseModel):
    id: Optional[str] = None

    access_type: Optional[str] = None

    object_id: Optional[str] = None

    object_type: Optional[str] = None

    shared_by: Optional[str] = None

    user_or_team_id: Optional[str] = None

    user_or_team_type: Optional[str] = None


class EmailerCampaignSharingPermission(BaseModel):
    access_type: Optional[str] = None

    is_owner: Optional[bool] = None

    object_id: Optional[str] = None

    object_type: Optional[str] = None

    owner_id: Optional[str] = None

    sharing_accesses: Optional[List[EmailerCampaignSharingPermissionSharingAccess]] = None

    visibility: Optional[str] = None


class EmailerCampaign(BaseModel):
    """Complete emailer campaign object with statistics"""

    id: Optional[str] = None

    active: Optional[bool] = None

    archived: Optional[bool] = None

    bounce_rate: Optional[float] = None

    contact_statuses: Optional[EmailerCampaignContactStatuses] = None

    created_at: Optional[datetime] = None

    emailer_schedule_id: Optional[str] = None

    excluded_account_stage_ids: Optional[List[str]] = None

    excluded_contact_stage_ids: Optional[List[str]] = None

    label_ids: Optional[List[str]] = None

    loaded_stats: Optional[bool] = None

    max_emails_per_day: Optional[int] = None

    name: Optional[str] = None

    open_rate: Optional[float] = None

    permissions: Optional[str] = None

    reply_rate: Optional[float] = None

    same_account_reply_policy_cd: Optional[str] = None

    sharing_permission: Optional[EmailerCampaignSharingPermission] = None

    unique_bounced: Optional[int] = None

    unique_delivered: Optional[int] = None

    unique_opened: Optional[int] = None

    unique_replied: Optional[int] = None

    unique_scheduled: Union[int, Literal["loading"], None] = None

    user_id: Optional[str] = None


class EmailerStepCounts(BaseModel):
    active: Optional[int] = None

    bounced: Optional[int] = None

    finished: Optional[int] = None

    paused: Optional[int] = None


class EmailerStep(BaseModel):
    id: Optional[str] = None

    counts: Optional[EmailerStepCounts] = None

    emailer_campaign_id: Optional[str] = None

    note: Optional[str] = None

    position: Optional[int] = None

    priority: Optional[Literal["high", "medium", "low"]] = None

    type: Optional[Literal["auto_email", "call", "action_item", "manual_email"]] = None

    unique_completed: Union[int, Literal["loading"], None] = None

    unique_scheduled: Union[int, Literal["loading"], None] = None

    unique_skipped: Union[int, Literal["loading"], None] = None

    wait_mode: Optional[Literal["hour", "day", "week"]] = None

    wait_time: Optional[int] = None


class EmailerTouch(BaseModel):
    id: Optional[str] = None

    bounce_rate: Optional[float] = None

    emailer_step_id: Optional[str] = None

    emailer_template_id: Optional[str] = None

    has_personalized_opener: Optional[bool] = None

    include_signature: Optional[bool] = None

    open_rate: Optional[float] = None

    reply_rate: Optional[float] = None

    status: Optional[Literal["approved", "pending", "draft"]] = None

    template_type: Optional[str] = None

    type: Optional[Literal["new_thread", "reply"]] = None

    unique_bounced: Optional[int] = None

    unique_delivered: Optional[int] = None

    unique_opened: Optional[int] = None

    unique_replied: Optional[int] = None

    unique_scheduled: Union[int, Literal["loading"], None] = None


class SkippedContactIDs(BaseModel):
    """
    Hash mapping contact IDs to reasons why they were skipped during the addition process. Each key is a contact ID and each value is a reason code.
    """

    contact_id: Optional[str] = FieldInfo(alias="<contact_id>", default=None)
    """Reason why this contact was skipped"""


class Team(BaseModel):
    id: Optional[str] = None

    sequences_finder_empty: Optional[bool] = None


class EmailerCampaignAddContactsResponse(BaseModel):
    contacts: List[Contact]
    """Array of contacts that were successfully added to the sequence"""

    emailer_campaign: EmailerCampaign
    """Complete emailer campaign object with statistics"""

    emailer_steps: List[EmailerStep]
    """Array of sequence steps"""

    emailer_touches: List[EmailerTouch]
    """Array of email templates/touches for the sequence"""

    skipped_contact_ids: SkippedContactIDs
    """
    Hash mapping contact IDs to reasons why they were skipped during the addition
    process. Each key is a contact ID and each value is a reason code.
    """

    team: Team

    signals_hash: Optional[object] = None
    """Optional signals data for play recommendations and analytics"""
