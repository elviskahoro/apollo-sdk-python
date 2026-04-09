# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ContactUpdateResponse", "Contact", "ContactPhoneNumber", "Label"]


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


class ContactUpdateResponse(BaseModel):
    contact: Optional[Contact] = None

    labels: Optional[List[Label]] = None
