# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "EmailAccountListResponse",
    "EmailAccount",
    "EmailAccountDeliverabilityScore",
    "EmailAccountTrueWarmupThresholds",
]


class EmailAccountDeliverabilityScore(BaseModel):
    id: Optional[str] = None

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    avg_click_rate: Optional[int] = None

    avg_daily_sent: Optional[int] = None

    avg_delivered_rate: Optional[int] = None

    avg_hard_bounce_rate: Optional[int] = None

    avg_open_rate: Optional[int] = None

    avg_reply_rate: Optional[int] = None

    avg_spam_block_rate: Optional[int] = None

    avg_unsubscribe_rate: Optional[int] = None

    click_rate_score: Optional[int] = None

    concurrency_locks: Optional[object] = None

    created_at: Optional[str] = None

    daily_email_sent_score: Optional[int] = None

    date_from: Optional[str] = None

    date_to: Optional[str] = None

    deliverability_score: Optional[int] = None

    domain_health_score: Optional[int] = None

    email_account_domain_age_score: Optional[int] = None

    email_account_id: Optional[str] = None

    hard_bounce_score: Optional[int] = None

    key: Optional[str] = None

    open_rate_score: Optional[int] = None

    random: Optional[float] = None

    reply_rate_score: Optional[int] = None

    spam_block_score: Optional[int] = None

    sum_clicked_count: Optional[int] = None

    sum_delivered_count: Optional[int] = None

    sum_hard_bounced_count: Optional[int] = None

    sum_opened_count: Optional[int] = None

    sum_replied_count: Optional[int] = None

    sum_sent_count: Optional[int] = None

    sum_spam_blocked_count: Optional[int] = None

    sum_unsubscribed_count: Optional[int] = None

    team_id: Optional[str] = None

    unsubscribe_rate_score: Optional[int] = None

    updated_at: Optional[str] = None

    user_id: Optional[str] = None


class EmailAccountTrueWarmupThresholds(BaseModel):
    bounce_rate: Optional[int] = None

    open_rate: Optional[int] = None

    reply_rate: Optional[int] = None

    spam_block_rate: Optional[int] = None


class EmailAccount(BaseModel):
    id: Optional[str] = None

    active: Optional[bool] = None

    active_campaigns_count: Optional[int] = None

    aliases: Optional[List[str]] = None

    created_at: Optional[str] = None

    default: Optional[bool] = None

    deliverability_score: Optional[EmailAccountDeliverabilityScore] = None

    email: Optional[str] = None

    email_daily_threshold: Optional[int] = None

    email_sending_policy_cd: Optional[str] = None

    fields_fully_loaded: Optional[bool] = None

    inactive_reason: Optional[object] = None

    is_opted_in_mailwarming: Optional[object] = None

    last_synced_at: Optional[str] = None

    limits_editable: Optional[bool] = None

    mailgun_domains: Optional[object] = None

    mailwarming_eta: Optional[object] = None

    mailwarming_max: Optional[int] = None

    mailwarming_on_weekdays_only: Optional[bool] = None

    mailwarming_score: Optional[int] = None

    mailwarming_score_banner: Optional[str] = None

    mailwarming_status: Optional[str] = None

    mailwarming_subject_token: Optional[object] = None

    mailwarming_to_send_daily: Optional[int] = None

    mailwarming_to_send_incrementor: Optional[int] = None

    max_outbound_emails_per_hour: Optional[int] = None

    nudge_user_to_send_mails: Optional[bool] = None

    nylas_api_version: Optional[object] = None

    nylas_provider: Optional[object] = None

    provider_display_name: Optional[str] = None

    revoked_at: Optional[object] = None

    seconds_delay_between_emails: Optional[int] = None

    sendgrid_api_key_v3: Optional[object] = None

    sendgrid_api_user: Optional[object] = None

    signature_edit_disabled: Optional[bool] = None

    signature_html: Optional[str] = None

    true_warmup_approximate_end_date: Optional[object] = None

    true_warmup_daily_limit: Optional[int] = None

    true_warmup_enable_thresholds: Optional[bool] = None

    true_warmup_enabled: Optional[bool] = None

    true_warmup_last_throttled_at: Optional[object] = None

    true_warmup_progress: Optional[int] = None

    true_warmup_status: Optional[object] = None

    true_warmup_thresholds: Optional[EmailAccountTrueWarmupThresholds] = None

    type: Optional[str] = None

    user_id: Optional[str] = None


class EmailAccountListResponse(BaseModel):
    email_accounts: Optional[List[EmailAccount]] = None
