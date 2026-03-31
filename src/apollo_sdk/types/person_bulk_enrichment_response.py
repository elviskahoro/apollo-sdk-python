# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PersonBulkEnrichmentResponse",
    "Match",
    "MatchAccount",
    "MatchAccountAccountRuleConfigStatus",
    "MatchEmploymentHistory",
    "MatchOrganization",
    "MatchOrganizationIndustryTagHash",
]


class MatchAccountAccountRuleConfigStatus(BaseModel):
    id: Optional[str] = None

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    created_at: Optional[object] = None

    key: Optional[str] = None

    rule_action_config_id: Optional[str] = None

    rule_config_id: Optional[str] = None

    status_cd: Optional[str] = None

    updated_at: Optional[object] = None


class MatchAccount(BaseModel):
    id: Optional[str] = None

    account_playbook_statuses: Optional[List[object]] = None

    account_rule_config_statuses: Optional[List[MatchAccountAccountRuleConfigStatus]] = None

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

    hubspot_id: Optional[object] = None

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

    salesforce_id: Optional[str] = None

    salesforce_record_url: Optional[str] = None

    sanitized_phone: Optional[str] = None

    source: Optional[str] = None

    source_display_name: Optional[str] = None

    team_id: Optional[str] = None

    twitter_url: Optional[str] = None

    typed_custom_fields: Optional[object] = None

    website_url: Optional[str] = None


class MatchEmploymentHistory(BaseModel):
    id: Optional[str] = None

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    created_at: Optional[object] = None

    current: Optional[bool] = None

    degree: Optional[object] = None

    description: Optional[object] = None

    emails: Optional[object] = None

    end_date: Optional[object] = None

    grade_level: Optional[object] = None

    key: Optional[str] = None

    kind: Optional[object] = None

    major: Optional[object] = None

    organization_id: Optional[str] = None

    organization_name: Optional[str] = None

    raw_address: Optional[object] = None

    start_date: Optional[str] = None

    title: Optional[str] = None

    updated_at: Optional[object] = None


class MatchOrganizationIndustryTagHash(BaseModel):
    information_technology_services: Optional[str] = FieldInfo(alias="information technology & services", default=None)


class MatchOrganization(BaseModel):
    id: Optional[str] = None

    alexa_ranking: Optional[int] = None

    angellist_url: Optional[object] = None

    blog_url: Optional[object] = None

    city: Optional[str] = None

    country: Optional[str] = None

    crunchbase_url: Optional[object] = None

    estimated_num_employees: Optional[int] = None

    facebook_url: Optional[str] = None

    founded_year: Optional[int] = None

    industries: Optional[List[str]] = None

    industry: Optional[str] = None

    industry_tag_hash: Optional[MatchOrganizationIndustryTagHash] = None

    industry_tag_id: Optional[str] = None

    keywords: Optional[List[str]] = None

    languages: Optional[List[object]] = None

    linkedin_uid: Optional[str] = None

    linkedin_url: Optional[str] = None

    logo_url: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[object] = None

    postal_code: Optional[str] = None

    primary_domain: Optional[str] = None

    primary_phone: Optional[object] = None

    publicly_traded_exchange: Optional[object] = None

    publicly_traded_symbol: Optional[object] = None

    raw_address: Optional[str] = None

    retail_location_count: Optional[int] = None

    secondary_industries: Optional[List[object]] = None

    snippets_loaded: Optional[bool] = None

    state: Optional[str] = None

    street_address: Optional[str] = None

    twitter_url: Optional[str] = None

    website_url: Optional[str] = None


class Match(BaseModel):
    id: Optional[str] = None

    account: Optional[MatchAccount] = None

    account_id: Optional[str] = None

    city: Optional[str] = None

    country: Optional[str] = None

    departments: Optional[List[str]] = None

    email: Optional[str] = None

    email_status: Optional[str] = None

    employment_history: Optional[List[MatchEmploymentHistory]] = None

    extrapolated_email_confidence: Optional[object] = None

    facebook_url: Optional[object] = None

    first_name: Optional[str] = None

    functions: Optional[List[str]] = None

    github_url: Optional[object] = None

    headline: Optional[str] = None

    intent_strength: Optional[object] = None

    is_likely_to_engage: Optional[bool] = None

    last_name: Optional[str] = None

    linkedin_url: Optional[str] = None

    name: Optional[str] = None

    organization: Optional[MatchOrganization] = None

    organization_id: Optional[str] = None

    photo_url: Optional[str] = None

    revealed_for_current_team: Optional[bool] = None

    seniority: Optional[str] = None

    show_intent: Optional[bool] = None

    state: Optional[str] = None

    subdepartments: Optional[List[str]] = None

    title: Optional[str] = None

    twitter_url: Optional[object] = None


class PersonBulkEnrichmentResponse(BaseModel):
    credits_consumed: Optional[int] = None

    error_code: Optional[object] = None

    error_message: Optional[object] = None

    matches: Optional[List[Match]] = None

    missing_records: Optional[int] = None

    status: Optional[str] = None

    total_requested_enrichments: Optional[int] = None

    unique_enriched_records: Optional[int] = None
