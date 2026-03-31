# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "OrganizationEnrichResponse",
    "Organization",
    "OrganizationAccount",
    "OrganizationCurrentTechnology",
    "OrganizationDepartmentalHeadCount",
    "OrganizationFundingEvent",
    "OrganizationIndustryTagHash",
]


class OrganizationAccount(BaseModel):
    id: Optional[str] = None

    account_playbook_statuses: Optional[List[object]] = None

    account_rule_config_statuses: Optional[List[object]] = None

    account_stage_id: Optional[object] = None

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

    label_ids: Optional[List[str]] = None

    linkedin_url: Optional[object] = None

    modality: Optional[str] = None

    name: Optional[str] = None

    organization_id: Optional[str] = None

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


class OrganizationCurrentTechnology(BaseModel):
    category: Optional[str] = None

    name: Optional[str] = None

    uid: Optional[str] = None


class OrganizationDepartmentalHeadCount(BaseModel):
    accounting: Optional[int] = None

    administrative: Optional[int] = None

    arts_and_design: Optional[int] = None

    business_development: Optional[int] = None

    consulting: Optional[int] = None

    data_science: Optional[int] = None

    education: Optional[int] = None

    engineering: Optional[int] = None

    entrepreneurship: Optional[int] = None

    finance: Optional[int] = None

    human_resources: Optional[int] = None

    information_technology: Optional[int] = None

    legal: Optional[int] = None

    marketing: Optional[int] = None

    media_and_commmunication: Optional[int] = None

    operations: Optional[int] = None

    product_management: Optional[int] = None

    sales: Optional[int] = None

    support: Optional[int] = None


class OrganizationFundingEvent(BaseModel):
    id: Optional[str] = None

    amount: Optional[str] = None

    currency: Optional[str] = None

    date: Optional[str] = None

    investors: Optional[str] = None

    news_url: Optional[object] = None

    type: Optional[str] = None


class OrganizationIndustryTagHash(BaseModel):
    information_technology_services: Optional[str] = FieldInfo(alias="information technology & services", default=None)


class Organization(BaseModel):
    id: Optional[str] = None

    account: Optional[OrganizationAccount] = None

    account_id: Optional[str] = None

    alexa_ranking: Optional[int] = None

    angellist_url: Optional[object] = None

    annual_revenue: Optional[int] = None

    annual_revenue_printed: Optional[str] = None

    blog_url: Optional[object] = None

    city: Optional[str] = None

    country: Optional[str] = None

    crunchbase_url: Optional[object] = None

    current_technologies: Optional[List[OrganizationCurrentTechnology]] = None

    departmental_head_count: Optional[OrganizationDepartmentalHeadCount] = None

    estimated_num_employees: Optional[int] = None

    facebook_url: Optional[str] = None

    founded_year: Optional[int] = None

    funding_events: Optional[List[OrganizationFundingEvent]] = None

    industries: Optional[List[str]] = None

    industry: Optional[str] = None

    industry_tag_hash: Optional[OrganizationIndustryTagHash] = None

    industry_tag_id: Optional[str] = None

    keywords: Optional[List[str]] = None

    languages: Optional[List[object]] = None

    latest_funding_round_date: Optional[str] = None

    latest_funding_stage: Optional[str] = None

    linkedin_uid: Optional[str] = None

    linkedin_url: Optional[str] = None

    logo_url: Optional[str] = None

    name: Optional[str] = None

    num_suborganizations: Optional[int] = None

    org_chart_removed: Optional[bool] = None

    org_chart_root_people_ids: Optional[List[str]] = None

    org_chart_sector: Optional[str] = None

    org_chart_show_department_filter: Optional[bool] = None

    owned_by_organization_id: Optional[object] = None

    phone: Optional[object] = None

    postal_code: Optional[str] = None

    primary_domain: Optional[str] = None

    primary_phone: Optional[object] = None

    publicly_traded_exchange: Optional[object] = None

    publicly_traded_symbol: Optional[object] = None

    raw_address: Optional[str] = None

    retail_location_count: Optional[int] = None

    secondary_industries: Optional[List[object]] = None

    seo_description: Optional[str] = None

    short_description: Optional[str] = None

    snippets_loaded: Optional[bool] = None

    state: Optional[str] = None

    street_address: Optional[str] = None

    suborganizations: Optional[List[object]] = None

    technology_names: Optional[List[str]] = None

    total_funding: Optional[int] = None

    total_funding_printed: Optional[str] = None

    twitter_url: Optional[str] = None

    website_url: Optional[str] = None


class OrganizationEnrichResponse(BaseModel):
    organization: Optional[Organization] = None
