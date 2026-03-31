# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "OpportunityListResponse",
    "Opportunity",
    "OpportunityAccount",
    "OpportunityAccountAccountRuleConfigStatus",
    "OpportunityAccountPrimaryPhone",
    "OpportunityCurrency",
    "Pagination",
]


class OpportunityAccountAccountRuleConfigStatus(BaseModel):
    id: Optional[str] = None

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    created_at: Optional[object] = None

    key: Optional[str] = None

    rule_action_config_id: Optional[str] = None

    rule_config_id: Optional[str] = None

    status_cd: Optional[str] = None

    updated_at: Optional[object] = None


class OpportunityAccountPrimaryPhone(BaseModel):
    number: Optional[str] = None

    sanitized_number: Optional[str] = None

    source: Optional[str] = None


class OpportunityAccount(BaseModel):
    id: Optional[str] = None

    account_playbook_statuses: Optional[List[object]] = None

    account_rule_config_statuses: Optional[List[OpportunityAccountAccountRuleConfigStatus]] = None

    account_stage_id: Optional[str] = None

    alexa_ranking: Optional[int] = None

    angellist_url: Optional[object] = None

    blog_url: Optional[object] = None

    contact_campaign_status_tally: Optional[object] = None

    contact_emailer_campaign_ids: Optional[List[object]] = None

    created_at: Optional[str] = None

    creator_id: Optional[object] = None

    crm_owner_id: Optional[object] = None

    crm_record_url: Optional[object] = None

    crunchbase_url: Optional[object] = None

    custom_field_errors: Optional[object] = None

    domain: Optional[str] = None

    existence_level: Optional[str] = None

    facebook_url: Optional[str] = None

    founded_year: Optional[int] = None

    hubspot_id: Optional[object] = None

    label_ids: Optional[List[str]] = None

    languages: Optional[List[str]] = None

    last_activity_date: Optional[object] = None

    linkedin_uid: Optional[str] = None

    linkedin_url: Optional[str] = None

    logo_url: Optional[str] = None

    modality: Optional[str] = None

    name: Optional[str] = None

    num_contacts: Optional[int] = None

    organization_id: Optional[str] = None

    original_source: Optional[str] = None

    owner_id: Optional[object] = None

    parent_account_id: Optional[object] = None

    phone: Optional[str] = None

    phone_status: Optional[str] = None

    primary_domain: Optional[str] = None

    primary_phone: Optional[OpportunityAccountPrimaryPhone] = None

    publicly_traded_exchange: Optional[str] = None

    publicly_traded_symbol: Optional[object] = None

    salesforce_id: Optional[object] = None

    sanitized_phone: Optional[str] = None

    source: Optional[str] = None

    source_display_name: Optional[str] = None

    team_id: Optional[str] = None

    twitter_url: Optional[str] = None

    typed_custom_fields: Optional[object] = None

    website_url: Optional[str] = None


class OpportunityCurrency(BaseModel):
    iso_code: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class Opportunity(BaseModel):
    id: Optional[str] = None

    account: Optional[OpportunityAccount] = None

    account_id: Optional[str] = None

    actual_close_date: Optional[object] = None

    amount: Optional[int] = None

    amount_in_team_currency: Optional[int] = None

    closed_date: Optional[str] = None

    closed_lost_reason: Optional[object] = None

    closed_won_reason: Optional[object] = None

    created_at: Optional[str] = None

    created_by_id: Optional[str] = None

    crm_id: Optional[object] = None

    crm_owner_id: Optional[object] = None

    crm_record_url: Optional[object] = None

    currency: Optional[OpportunityCurrency] = None

    current_solutions: Optional[object] = None

    deal_probability: Optional[int] = None

    deal_source: Optional[object] = None

    description: Optional[object] = None

    exchange_rate_code: Optional[str] = None

    exchange_rate_value: Optional[int] = None

    existence_level: Optional[str] = None

    forecast_category: Optional[str] = None

    forecasted_revenue: Optional[float] = None

    is_closed: Optional[bool] = None

    is_won: Optional[bool] = None

    last_activity_date: Optional[str] = None

    manually_updated_forecast: Optional[object] = None

    manually_updated_probability: Optional[object] = None

    name: Optional[str] = None

    next_step: Optional[object] = None

    next_step_date: Optional[object] = None

    next_step_last_updated_at: Optional[object] = None

    opportunity_contact_roles: Optional[List[object]] = None

    opportunity_pipeline_id: Optional[object] = None

    opportunity_rule_config_statuses: Optional[List[object]] = None

    opportunity_stage_id: Optional[str] = None

    owner_id: Optional[str] = None

    probability: Optional[object] = None

    salesforce_id: Optional[object] = None

    salesforce_owner_id: Optional[object] = None

    source: Optional[str] = None

    stage_name: Optional[object] = None

    stage_updated_at: Optional[str] = None

    team_id: Optional[str] = None

    typed_custom_fields: Optional[object] = None


class Pagination(BaseModel):
    page: Optional[int] = None

    per_page: Optional[int] = None

    total_entries: Optional[int] = None

    total_pages: Optional[int] = None


class OpportunityListResponse(BaseModel):
    breadcrumbs: Optional[List[object]] = None

    disable_eu_prospecting: Optional[bool] = None

    has_join: Optional[bool] = None

    num_fetch_result: Optional[object] = None

    opportunities: Optional[List[Opportunity]] = None

    pagination: Optional[Pagination] = None

    partial_results_limit: Optional[int] = None

    partial_results_only: Optional[bool] = None

    salesforce_users: Optional[List[object]] = None
