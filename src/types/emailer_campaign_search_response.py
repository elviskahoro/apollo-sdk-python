# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EmailerCampaignSearchResponse", "Breadcrumb", "EmailerCampaign", "Pagination"]


class Breadcrumb(BaseModel):
    display_name: Optional[str] = None

    label: Optional[str] = None

    signal_field_name: Optional[str] = None

    value: Optional[str] = None


class EmailerCampaign(BaseModel):
    id: Optional[str] = None

    ab_test_step_ids: Optional[List[object]] = None

    active: Optional[bool] = None

    archived: Optional[bool] = None

    bcc_emails: Optional[str] = None

    bounce_rate: Optional[int] = None

    cc_emails: Optional[str] = None

    click_rate: Optional[int] = None

    contact_email_event_to_stage_mapping: Optional[object] = None

    create_task_if_email_open: Optional[bool] = None

    created_at: Optional[str] = None

    creation_type: Optional[str] = None

    days_to_wait_before_mark_as_response: Optional[int] = None

    demo_rate: Optional[int] = None

    email_open_trigger_task_threshold: Optional[int] = None

    emailer_schedule_id: Optional[str] = None

    excluded_account_stage_ids: Optional[List[str]] = None

    excluded_contact_stage_ids: Optional[List[str]] = None

    folder_id: Optional[object] = None

    hard_bounce_rate: Optional[int] = None

    is_performing_poorly: Optional[bool] = None

    label_ids: Optional[List[str]] = None

    last_used_at: Optional[object] = None

    loaded_stats: Optional[bool] = None

    mark_finished_if_click: Optional[bool] = None

    mark_finished_if_interested: Optional[bool] = None

    mark_finished_if_reply: Optional[bool] = None

    mark_paused_if_ooo: Optional[bool] = None

    max_emails_per_day: Optional[object] = None

    name: Optional[str] = None

    num_contacts_email_status_extrapolated: Optional[int] = None

    num_steps: Optional[int] = None

    open_rate: Optional[int] = None

    opt_out_rate: Optional[int] = None

    permissions: Optional[str] = None

    prioritized_by_user: Optional[object] = None

    remind_ab_test_results: Optional[bool] = None

    reply_rate: Optional[int] = None

    same_account_reply_delay_days: Optional[int] = None

    same_account_reply_policy_cd: Optional[object] = None

    sequence_by_exact_daytime: Optional[object] = None

    sequence_ruleset_id: Optional[str] = None

    spam_block_rate: Optional[int] = None

    starred_by_user_ids: Optional[List[str]] = None

    underperforming_touches_count: Optional[int] = None

    unique_bounced: Optional[int] = None

    unique_clicked: Optional[int] = None

    unique_delivered: Optional[int] = None

    unique_demoed: Optional[int] = None

    unique_hard_bounced: Optional[int] = None

    unique_opened: Optional[int] = None

    unique_replied: Optional[int] = None

    unique_scheduled: Optional[int] = None

    unique_spam_blocked: Optional[int] = None

    unique_unsubscribed: Optional[int] = None

    user_id: Optional[str] = None


class Pagination(BaseModel):
    page: Optional[int] = None

    per_page: Optional[int] = None

    total_entries: Optional[int] = None

    total_pages: Optional[int] = None


class EmailerCampaignSearchResponse(BaseModel):
    breadcrumbs: Optional[List[Breadcrumb]] = None

    emailer_campaigns: Optional[List[EmailerCampaign]] = None

    num_fetch_result: Optional[object] = None

    pagination: Optional[Pagination] = None
