# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AccountSearchResponse", "Account", "Breadcrumb", "Pagination"]


class Account(BaseModel):
    id: Optional[str] = None

    account_playbook_statuses: Optional[List[object]] = None

    account_rule_config_statuses: Optional[List[object]] = None

    account_stage_id: Optional[str] = None

    contact_campaign_status_tally: Optional[object] = None

    contact_emailer_campaign_ids: Optional[List[object]] = None

    created_at: Optional[str] = None

    creator_id: Optional[object] = None

    crm_owner_id: Optional[object] = None

    crm_record_url: Optional[object] = None

    custom_field_errors: Optional[object] = None

    domain: Optional[str] = None

    existence_level: Optional[str] = None

    has_intent_signal_account: Optional[bool] = None

    hubspot_id: Optional[object] = None

    intent_signal_account: Optional[object] = None

    intent_strength: Optional[object] = None

    label_ids: Optional[List[object]] = None

    last_activity_date: Optional[object] = None

    linkedin_url: Optional[object] = None

    modality: Optional[str] = None

    name: Optional[str] = None

    num_contacts: Optional[int] = None

    organization_id: Optional[object] = None

    original_source: Optional[str] = None

    owner_id: Optional[str] = None

    parent_account_id: Optional[object] = None

    phone: Optional[str] = None

    phone_status: Optional[str] = None

    salesforce_id: Optional[object] = None

    sanitized_phone: Optional[str] = None

    show_intent: Optional[bool] = None

    source: Optional[str] = None

    source_display_name: Optional[str] = None

    team_id: Optional[str] = None

    typed_custom_fields: Optional[object] = None


class Breadcrumb(BaseModel):
    display_name: Optional[str] = None

    label: Optional[str] = None

    signal_field_name: Optional[str] = None

    value: Optional[str] = None


class Pagination(BaseModel):
    page: Optional[int] = None

    per_page: Optional[int] = None

    total_entries: Optional[int] = None

    total_pages: Optional[int] = None


class AccountSearchResponse(BaseModel):
    accounts: Optional[List[Account]] = None

    breadcrumbs: Optional[List[Breadcrumb]] = None

    disable_eu_prospecting: Optional[bool] = None

    has_join: Optional[bool] = None

    num_fetch_result: Optional[object] = None

    pagination: Optional[Pagination] = None

    partial_results_limit: Optional[int] = None

    partial_results_only: Optional[bool] = None
