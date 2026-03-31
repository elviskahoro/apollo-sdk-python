# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AccountUpdateResponse", "Account"]


class Account(BaseModel):
    id: Optional[str] = None

    account_playbook_statuses: Optional[List[object]] = None

    account_rule_config_statuses: Optional[List[object]] = None

    account_stage_id: Optional[str] = None

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

    linkedin_url: Optional[object] = None

    modality: Optional[str] = None

    name: Optional[str] = None

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


class AccountUpdateResponse(BaseModel):
    account: Optional[Account] = None

    labels: Optional[List[object]] = None
