# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EmailerMessageSearchParams"]


class EmailerMessageSearchParams(TypedDict, total=False):
    email_account_id_and_aliases: str

    emailer_campaign_ids: SequenceNotStr[str]
    """Search for emails that are included in specific sequences in your Apollo
    account.

    You can search multiple sequences. Any sequence not included in this parameter
    will be exclude from search results.

    To find sequence IDs, call the
    <a href="https://docs.apollo.io/reference/search-for-sequences" target="_blank">Search
    for Sequences endpoint</a> and identify the `id` value for the sequence.

    Example: `66e9e215ece19801b219997f`
    """

    emailer_message_date_range_mode: str
    """
    Use this parameter in combination with the `emailer_message_date_range[max]` and
    `emailer_message_date_range[min]` parameters. Find emails based on 1 of the
    following options: <ul> <li> `due_at`: When emails are scheduled to be
    delivered. </li> <li> `completed_at`: When emails were delivered. </li> </ul>
    """

    emailer_message_date_range_max: Annotated[
        Union[str, date], PropertyInfo(alias="emailer_message_date_range[max]", format="iso8601")
    ]
    """Set the upper bound of the date range you want to search.

    Use this parameter in combination with the `emailer_message_date_range[min]` and
    `emailer_message_date_range_mode` parameters. This date should fall after the
    `emailer_message_date_range[min]` date.

    The date should be formatted as `YYYY-MM-DD`.

    Example: `2025-10-30`
    """

    emailer_message_date_range_min: Annotated[
        Union[str, date], PropertyInfo(alias="emailer_message_date_range[min]", format="iso8601")
    ]
    """Set the lower bound of the date range you want to search.

    Use this parameter in combination with the `emailer_message_date_range[max]` and
    `emailer_message_date_range_mode` parameters. This date should fall before the
    `emailer_message_date_range[max]` date.

    The date should be formatted as `YYYY-MM-DD`.

    Example: `2025-10-30`
    """

    emailer_message_reply_classes: SequenceNotStr[str]
    """Find emails based on the response sentiment of the recipient.

    This can include the recipient expressing interest in meeting or having a
    follow-up question. You can add multiple values.

    Possible values include: <ul> <li> `willing_to_meet` </li> <li>
    `follow_up_question` </li> <li> `person_referral` </li> <li> `out_of_office`
    </li> <li> `already_left_company_or_not_right_person` </li> <li>
    `not_interested` </li> <li> `unsubscribe` </li> <li> `none_of_the_above` </li>
    </ul>
    """

    emailer_message_stats: SequenceNotStr[str]
    """
    Find emails based on their current status, such as whether they were delivered
    or opened. You can add multiple statuses.

    Possible values include: <ul> <li> `delivered` </li> <li> `scheduled` </li> <li>
    `drafted` </li> <li> `not_opened` </li> <li> `opened` </li> <li> `clicked` </li>
    <li> `unsubscribed` </li> <li> `demoed` </li> <li> `bounced` </li> <li>
    `spam_blocked` </li> <li> `failed_other` </li> </ul>
    """

    not_emailer_campaign_ids: SequenceNotStr[str]
    """Exclude emails from specific sequences in your Apollo account.

    You can exclude multiple sequences. Any sequence not excluded using this
    parameter will be included in search results.

    To find sequence IDs, call the
    <a href="https://docs.apollo.io/reference/search-for-sequences" target="_blank">Search
    for Sequences endpoint</a> and identify the `id` value for the sequence.

    Example: `66e9e215ece19801b219997f`
    """

    not_sent_reason_cds: SequenceNotStr[str]
    """Find emails based on the reason they were not sent. You can add multiple values.

    Possible values include: <ul> <li> `contact_stage_safeguard` </li> <li>
    `same_account_reply` </li> <li> `account_stage_safeguard` </li> <li>
    `email_unverified` </li> <li> `snippets_missing` </li> <li>
    `personalized_opener_missing` </li> <li> `thread_reply_original_email_missing`
    </li> <li> `no_active_email_account` </li> <li> `email_format_invalid` </li>
    <li> `ownership_permission` </li> <li> `email_service_provider_delivery_failure`
    </li> <li> `sendgrid_dropped_email` </li> <li> `mailgun_dropped_email` </li>
    <li> `gdpr_compliance` </li> <li> `not_valid_hard_bounce_detected` <li>
    `other_safeguard` </li> <li> `new_job_change_detected` </li> <li>
    `email_on_global_bounce_list` </li> </ul>
    """

    page: int
    """The page number of the Apollo data that you want to retrieve.

    Use this parameter in combination with the `per_page` parameter to make search
    results for navigable and improve the performance of the endpoint.

    Example: `4`
    """

    per_page: int
    """The number of search results that should be returned for each page.

    Limiting the number of results per page improves the endpoint's performance.

    Use the `page` parameter to search the different pages of data.

    Example: `10`
    """

    q_keywords: str
    """Add keywords to narrow the search of the emails in your team's Apollo account.

    Keywords should directly match at least part of an email's content. For example,
    searching the keyword `James` might return emails that were sent by
    `James Smith`.

    Example: `Jane`
    """

    user_ids: SequenceNotStr[str]
    """Find emails sent by specific users in your team's Apollo account.

    You can add multiple users.

    Use the
    <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
    a List of Users endpoint</a> to retrieve IDs for all of the users within your
    Apollo account.

    Example: `66302798d03b9601c7934ebf`
    """
