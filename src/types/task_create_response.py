# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "TaskCreateResponse",
    "Task",
    "TaskOpportunity",
    "TaskOpportunityAccount",
    "TaskOpportunityAccountAccountRuleConfigStatus",
    "TaskOpportunityCurrency",
    "TaskOpportunityOpportunityContactRole",
    "TaskOpportunityOpportunityContactRoleRole",
    "TaskOpportunityTypedCustomFields",
]


class TaskOpportunityAccountAccountRuleConfigStatus(BaseModel):
    id: Optional[str] = None

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    created_at: Optional[object] = None

    key: Optional[str] = None

    rule_action_config_id: Optional[str] = None

    rule_config_id: Optional[str] = None

    status_cd: Optional[str] = None

    updated_at: Optional[object] = None


class TaskOpportunityAccount(BaseModel):
    id: Optional[str] = None

    account_playbook_statuses: Optional[List[object]] = None

    account_rule_config_statuses: Optional[List[TaskOpportunityAccountAccountRuleConfigStatus]] = None

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

    hubspot_id: Optional[object] = None

    label_ids: Optional[List[str]] = None

    last_activity_date: Optional[object] = None

    linkedin_url: Optional[object] = None

    modality: Optional[str] = None

    name: Optional[str] = None

    num_contacts: Optional[int] = None

    organization_id: Optional[str] = None

    original_source: Optional[str] = None

    owner_id: Optional[object] = None

    parent_account_id: Optional[object] = None

    phone: Optional[object] = None

    phone_status: Optional[str] = None

    salesforce_id: Optional[object] = None

    source: Optional[str] = None

    source_display_name: Optional[str] = None

    team_id: Optional[str] = None

    typed_custom_fields: Optional[object] = None


class TaskOpportunityCurrency(BaseModel):
    iso_code: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class TaskOpportunityOpportunityContactRoleRole(BaseModel):
    crm_id: Optional[object] = None

    crm_role_id: Optional[object] = None

    is_primary: Optional[bool] = None

    opportunity_contact_role_type_id: Optional[str] = None


class TaskOpportunityOpportunityContactRole(BaseModel):
    id: Optional[str] = None

    contact_id: Optional[str] = None

    created_at: Optional[str] = None

    is_primary: Optional[bool] = None

    role: Optional[List[TaskOpportunityOpportunityContactRoleRole]] = None

    updated_at: Optional[str] = None


class TaskOpportunityTypedCustomFields(BaseModel):
    api_6095a711bd01d100a506d4da: Optional[List[str]] = FieldInfo(alias="6095a711bd01d100a506d4da", default=None)

    api_6095a711bd01d100a506d4dc: Optional[List[str]] = FieldInfo(alias="6095a711bd01d100a506d4dc", default=None)

    api_66e4ba346fe95a073461e00e: Optional[List[str]] = FieldInfo(alias="66e4ba346fe95a073461e00e", default=None)


class TaskOpportunity(BaseModel):
    id: Optional[str] = None

    account: Optional[TaskOpportunityAccount] = None

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

    currency: Optional[TaskOpportunityCurrency] = None

    current_solutions: Optional[object] = None

    deal_probability: Optional[int] = None

    deal_source: Optional[object] = None

    description: Optional[object] = None

    exchange_rate_code: Optional[str] = None

    exchange_rate_value: Optional[int] = None

    existence_level: Optional[str] = None

    forecast_category: Optional[str] = None

    forecasted_revenue: Optional[int] = None

    is_closed: Optional[bool] = None

    is_won: Optional[object] = None

    last_activity_date: Optional[str] = None

    manually_updated_forecast: Optional[object] = None

    manually_updated_probability: Optional[object] = None

    name: Optional[str] = None

    next_step: Optional[str] = None

    next_step_date: Optional[object] = None

    next_step_last_updated_at: Optional[str] = None

    opportunity_contact_roles: Optional[List[TaskOpportunityOpportunityContactRole]] = None

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

    typed_custom_fields: Optional[TaskOpportunityTypedCustomFields] = None


class Task(BaseModel):
    id: Optional[str] = None

    account_id: Optional[object] = None

    answered: Optional[object] = None

    completed_at: Optional[object] = None

    contact_id: Optional[object] = None

    created_at: Optional[str] = None

    created_from: Optional[object] = None

    creator_id: Optional[str] = None

    due_at: Optional[str] = None

    emailer_campaign_id: Optional[object] = None

    hubspot_id: Optional[object] = None

    needs_playbook_autoprospecting: Optional[object] = None

    note: Optional[object] = None

    opportunity: Optional[TaskOpportunity] = None

    opportunity_id: Optional[str] = None

    organization_id: Optional[object] = None

    person_id: Optional[object] = None

    persona_ids: Optional[List[object]] = None

    playbook_id: Optional[object] = None

    playbook_step_ids: Optional[List[object]] = None

    priority: Optional[str] = None

    rule_config_id: Optional[object] = None

    salesforce_id: Optional[object] = None

    salesforce_type: Optional[object] = None

    skipped_at: Optional[object] = None

    starred_by_user_ids: Optional[List[object]] = None

    status: Optional[str] = None

    subject: Optional[object] = None

    title: Optional[str] = None

    type: Optional[str] = None

    user_id: Optional[str] = None


class TaskCreateResponse(BaseModel):
    task: Optional[Task] = None
