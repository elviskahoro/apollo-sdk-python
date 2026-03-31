# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PersonEnrichmentResponse",
    "Person",
    "PersonContact",
    "PersonContactContactEmail",
    "PersonContactPhoneNumber",
    "PersonEmploymentHistory",
    "PersonOrganization",
    "PersonOrganizationCurrentTechnology",
    "PersonOrganizationFundingEvent",
    "PersonOrganizationIndustryTagHash",
]


class PersonContactContactEmail(BaseModel):
    email: Optional[str] = None

    email_from_customer: Optional[object] = None

    email_md5: Optional[str] = None

    email_sha256: Optional[str] = None

    email_source: Optional[object] = None

    email_status: Optional[str] = None

    extrapolated_email_confidence: Optional[object] = None

    free_domain: Optional[bool] = None

    position: Optional[int] = None


class PersonContactPhoneNumber(BaseModel):
    dialer_flags: Optional[object] = None

    dnc_other_info: Optional[object] = None

    dnc_status: Optional[object] = None

    position: Optional[int] = None

    raw_number: Optional[str] = None

    sanitized_number: Optional[str] = None

    status: Optional[str] = None

    type: Optional[object] = None


class PersonContact(BaseModel):
    id: Optional[str] = None

    account_id: Optional[str] = None

    account_phone_note: Optional[object] = None

    contact_emails: Optional[List[PersonContactContactEmail]] = None

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

    headline: Optional[str] = None

    hubspot_company_id: Optional[object] = None

    hubspot_vid: Optional[object] = None

    is_likely_to_engage: Optional[bool] = None

    label_ids: Optional[List[object]] = None

    last_activity_date: Optional[object] = None

    last_name: Optional[str] = None

    linkedin_uid: Optional[object] = None

    linkedin_url: Optional[str] = None

    merged_crm_ids: Optional[object] = None

    name: Optional[str] = None

    organization_id: Optional[str] = None

    organization_name: Optional[str] = None

    original_source: Optional[str] = None

    owner_id: Optional[object] = None

    person_id: Optional[str] = None

    phone_numbers: Optional[List[PersonContactPhoneNumber]] = None

    photo_url: Optional[object] = None

    present_raw_address: Optional[str] = None

    queued_for_crm_push: Optional[object] = None

    salesforce_account_id: Optional[object] = None

    salesforce_contact_id: Optional[object] = None

    salesforce_id: Optional[object] = None

    salesforce_lead_id: Optional[object] = None

    sanitized_phone: Optional[str] = None

    source: Optional[str] = None

    source_display_name: Optional[str] = None

    suggested_from_rule_engine_config_id: Optional[object] = None

    time_zone: Optional[str] = None

    title: Optional[str] = None

    typed_custom_fields: Optional[object] = None

    updated_at: Optional[str] = None

    updated_email_true_status: Optional[bool] = None


class PersonEmploymentHistory(BaseModel):
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


class PersonOrganizationCurrentTechnology(BaseModel):
    category: Optional[str] = None

    name: Optional[str] = None

    uid: Optional[str] = None


class PersonOrganizationFundingEvent(BaseModel):
    id: Optional[str] = None

    amount: Optional[str] = None

    currency: Optional[str] = None

    date: Optional[str] = None

    investors: Optional[str] = None

    news_url: Optional[object] = None

    type: Optional[str] = None


class PersonOrganizationIndustryTagHash(BaseModel):
    information_technology_services: Optional[str] = FieldInfo(alias="information technology & services", default=None)


class PersonOrganization(BaseModel):
    id: Optional[str] = None

    alexa_ranking: Optional[int] = None

    angellist_url: Optional[object] = None

    annual_revenue: Optional[int] = None

    annual_revenue_printed: Optional[str] = None

    blog_url: Optional[object] = None

    city: Optional[str] = None

    country: Optional[str] = None

    crunchbase_url: Optional[object] = None

    current_technologies: Optional[List[PersonOrganizationCurrentTechnology]] = None

    estimated_num_employees: Optional[int] = None

    facebook_url: Optional[str] = None

    founded_year: Optional[int] = None

    funding_events: Optional[List[PersonOrganizationFundingEvent]] = None

    industries: Optional[List[str]] = None

    industry: Optional[str] = None

    industry_tag_hash: Optional[PersonOrganizationIndustryTagHash] = None

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


class Person(BaseModel):
    id: Optional[str] = None

    city: Optional[str] = None

    contact: Optional[PersonContact] = None

    contact_id: Optional[str] = None

    country: Optional[str] = None

    departments: Optional[List[str]] = None

    email: Optional[str] = None

    email_status: Optional[str] = None

    employment_history: Optional[List[PersonEmploymentHistory]] = None

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

    organization: Optional[PersonOrganization] = None

    organization_id: Optional[str] = None

    photo_url: Optional[str] = None

    revealed_for_current_team: Optional[bool] = None

    seniority: Optional[str] = None

    show_intent: Optional[bool] = None

    state: Optional[str] = None

    subdepartments: Optional[List[str]] = None

    title: Optional[str] = None

    twitter_url: Optional[object] = None


class PersonEnrichmentResponse(BaseModel):
    person: Optional[Person] = None
