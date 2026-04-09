# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OpportunityCreateResponse", "Opportunity", "OpportunityCurrency"]


class OpportunityCurrency(BaseModel):
    iso_code: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class Opportunity(BaseModel):
    id: Optional[str] = None

    account_id: Optional[str] = None

    actual_close_date: Optional[object] = None

    amount: Optional[int] = None

    amount_in_team_currency: Optional[int] = None

    closed_date: Optional[object] = None

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

    opportunity_pipeline_id: Optional[str] = None

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


class OpportunityCreateResponse(BaseModel):
    opportunity: Optional[Opportunity] = None
