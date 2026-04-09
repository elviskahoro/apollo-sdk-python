# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrganizationSearchResponse", "Breadcrumb", "Organization", "OrganizationPrimaryPhone", "Pagination"]


class Breadcrumb(BaseModel):
    display_name: Optional[str] = None

    label: Optional[str] = None

    signal_field_name: Optional[str] = None

    value: Optional[str] = None


class OrganizationPrimaryPhone(BaseModel):
    number: Optional[str] = None

    sanitized_number: Optional[str] = None

    source: Optional[str] = None


class Organization(BaseModel):
    id: Optional[str] = None

    alexa_ranking: Optional[int] = None

    angellist_url: Optional[object] = None

    blog_url: Optional[object] = None

    crunchbase_url: Optional[object] = None

    facebook_url: Optional[str] = None

    founded_year: Optional[int] = None

    has_intent_signal_account: Optional[bool] = None

    intent_signal_account: Optional[object] = None

    intent_strength: Optional[object] = None

    languages: Optional[List[str]] = None

    linkedin_uid: Optional[str] = None

    linkedin_url: Optional[str] = None

    logo_url: Optional[str] = None

    name: Optional[str] = None

    owned_by_organization_id: Optional[object] = None

    phone: Optional[str] = None

    primary_domain: Optional[str] = None

    primary_phone: Optional[OrganizationPrimaryPhone] = None

    publicly_traded_exchange: Optional[object] = None

    publicly_traded_symbol: Optional[object] = None

    sanitized_phone: Optional[str] = None

    show_intent: Optional[bool] = None

    twitter_url: Optional[str] = None

    website_url: Optional[str] = None


class Pagination(BaseModel):
    page: Optional[int] = None

    per_page: Optional[int] = None

    total_entries: Optional[int] = None

    total_pages: Optional[int] = None


class OrganizationSearchResponse(BaseModel):
    accounts: Optional[List[object]] = None

    breadcrumbs: Optional[List[Breadcrumb]] = None

    derived_params: Optional[object] = None

    disable_eu_prospecting: Optional[bool] = None

    has_join: Optional[bool] = None

    api_model_ids: Optional[List[str]] = FieldInfo(alias="model_ids", default=None)

    num_fetch_result: Optional[object] = None

    organizations: Optional[List[Organization]] = None

    pagination: Optional[Pagination] = None

    partial_results_limit: Optional[int] = None

    partial_results_only: Optional[bool] = None
