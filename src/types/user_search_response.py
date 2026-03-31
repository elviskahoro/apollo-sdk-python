# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserSearchResponse", "Pagination", "User", "UserAssistantSetting"]


class Pagination(BaseModel):
    page: Optional[str] = None

    per_page: Optional[str] = None

    total_entries: Optional[int] = None

    total_pages: Optional[int] = None


class UserAssistantSetting(BaseModel):
    id: Optional[str] = None

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    deal_size_metric: Optional[str] = None

    inactive_account_stage_ids: Optional[List[object]] = None

    inactive_contact_stage_ids: Optional[List[object]] = None

    insight_deal_size_signals: Optional[object] = None

    insight_sale_cycle_signals: Optional[object] = None

    insight_win_rate_signals: Optional[object] = None

    is_persona_recommendation_requested: Optional[bool] = None

    job_posting_locations: Optional[List[object]] = None

    job_posting_titles: Optional[List[object]] = None

    key: Optional[str] = None

    latest_funding_days: Optional[int] = None

    max_num_active_accounts: Optional[int] = None

    max_people_in_sequence_per_account: Optional[int] = None

    num_inactive_days_to_re_engage: Optional[int] = None

    persona_ids: Optional[List[str]] = None

    should_show_persona_banner: Optional[bool] = None

    success_case_account_stage_ids: Optional[List[object]] = None

    team_id: Optional[str] = None

    technology_uids: Optional[List[object]] = None

    territory_company_size_ranges: Optional[List[object]] = None

    territory_location_override: Optional[bool] = None

    territory_locations: Optional[List[str]] = None

    territory_person_locations: Optional[List[str]] = None

    user_id: Optional[str] = None


class User(BaseModel):
    id: Optional[str] = None

    ai_credit_limit: Optional[object] = None

    apollo_everywhere_search_count: Optional[int] = None

    assistant_setting: Optional[UserAssistantSetting] = None

    bridge_calls: Optional[bool] = None

    bridge_incoming_calls: Optional[bool] = None

    bridge_incoming_phone_number: Optional[object] = None

    bridge_phone_number: Optional[object] = None

    chrome_extension_auto_match_salesforce_opportunity: Optional[bool] = None

    chrome_extension_downloaded: Optional[bool] = None

    chrome_extension_enabled_features: Optional[List[str]] = None

    chrome_extension_everywhere_icon_horizontal_position: Optional[str] = None

    chrome_extension_everywhere_icon_vertical_position_in_vh: Optional[int] = None

    chrome_extension_exclude_from_websites: Optional[List[str]] = None

    chrome_extension_gmail_enable_crm_sidebar: Optional[bool] = None

    chrome_extension_gmail_enable_email_tools: Optional[bool] = None

    connected_to_slack: Optional[bool] = None

    conversation_is_private: Optional[object] = None

    created_at: Optional[str] = None

    credit_limit: Optional[object] = None

    crm_email: Optional[object] = None

    crm_requested_to_integrate: Optional[object] = None

    current_email_verified: Optional[bool] = None

    daily_data_request_email: Optional[bool] = None

    daily_task_email: Optional[bool] = None

    data_request_emails: Optional[bool] = None

    default_account_overview_layout_id: Optional[object] = None

    default_chrome_extension_enable_reminders: Optional[bool] = None

    default_chrome_extension_log_email_send_to_hubspot: Optional[bool] = None

    default_chrome_extension_log_email_send_to_salesforce: Optional[bool] = None

    default_cockpit_layout: Optional[object] = None

    default_contact_overview_layout_id: Optional[object] = None

    default_home_overview_layout_id: Optional[object] = None

    default_opportunity_overview_layout_id: Optional[object] = None

    default_organization_overview_layout_id: Optional[object] = None

    default_person_overview_layout_id: Optional[object] = None

    default_use_local_numbers: Optional[bool] = None

    deleted: Optional[bool] = None

    direct_dial_credit_limit: Optional[object] = None

    disable_email_linking: Optional[object] = None

    dismiss_new_team_suggestion: Optional[bool] = None

    email: Optional[str] = None

    email_oauth_signin_only: Optional[bool] = None

    enable_click_tracking: Optional[bool] = None

    enable_desktop_notifications: Optional[bool] = None

    enable_gmail_desktop_notifications: Optional[object] = None

    enable_one_click_unsubscribe: Optional[object] = None

    enable_open_tracking: Optional[bool] = None

    export_credit_limit: Optional[object] = None

    fields_fully_loaded: Optional[bool] = None

    first_name: Optional[object] = None

    free_data_credits_email: Optional[bool] = None

    has_conference_account: Optional[bool] = None

    has_hidden_onboarding: Optional[bool] = None

    has_invited_user: Optional[bool] = None

    has_uploaded_csv: Optional[bool] = None

    has_used_enrichment: Optional[bool] = None

    last_name: Optional[object] = None

    linked_bot_conference_account: Optional[bool] = None

    linked_bot_conference_account_platforms: Optional[List[str]] = None

    linked_crm_name: Optional[object] = None

    linked_hubspot: Optional[bool] = None

    linked_salesforce: Optional[object] = None

    linked_salesloft: Optional[bool] = None

    linked_zoom_conference_account: Optional[bool] = None

    name: Optional[str] = None

    notification_last_created_at: Optional[object] = None

    notification_last_read_at: Optional[object] = None

    opt_out_html_template: Optional[str] = None

    password_needs_reset: Optional[bool] = None

    permission_set_id: Optional[str] = None

    prospect_territory_ids: Optional[List[object]] = None

    record_calls: Optional[bool] = None

    referral_code: Optional[str] = None

    request_email_change_to: Optional[object] = None

    salesforce_account: Optional[object] = None

    salesforce_id: Optional[object] = None

    salesforce_instance_url: Optional[object] = None

    self_identified_persona: Optional[object] = None

    should_include_unsubscribe_link: Optional[bool] = None

    show_chrome_extension_buying_intent_promo: Optional[bool] = None

    show_deals_detail_page_updates_modal: Optional[bool] = None

    subteam_ids: Optional[List[object]] = None

    sync_crm_id: Optional[object] = None

    sync_salesforce_id: Optional[object] = None

    team_id: Optional[str] = None

    territory_is_active: Optional[bool] = None

    title: Optional[object] = None

    toggled_on_territory_ids: Optional[List[object]] = None

    triggered_referral_campaigns: Optional[List[object]] = None

    typed_custom_fields: Optional[object] = None

    zp_contact_id: Optional[str] = None

    zp_is_super_analytics_user: Optional[object] = None


class UserSearchResponse(BaseModel):
    num_fetch_result: Optional[object] = None

    pagination: Optional[Pagination] = None

    users: Optional[List[User]] = None
