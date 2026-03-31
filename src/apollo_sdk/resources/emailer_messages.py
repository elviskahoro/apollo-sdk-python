# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import emailer_message_search_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["EmailerMessagesResource", "AsyncEmailerMessagesResource"]


class EmailerMessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailerMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EmailerMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailerMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return EmailerMessagesResourceWithStreamingResponse(self)

    def activities(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        get_emailstats

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/emailer_messages/{id}/activities", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def search(
        self,
        *,
        email_account_id_and_aliases: str | Omit = omit,
        emailer_campaign_ids: SequenceNotStr[str] | Omit = omit,
        emailer_message_date_range_mode: str | Omit = omit,
        emailer_message_date_range_max: Union[str, date] | Omit = omit,
        emailer_message_date_range_min: Union[str, date] | Omit = omit,
        emailer_message_reply_classes: SequenceNotStr[str] | Omit = omit,
        emailer_message_stats: SequenceNotStr[str] | Omit = omit,
        not_emailer_campaign_ids: SequenceNotStr[str] | Omit = omit,
        not_sent_reason_cds: SequenceNotStr[str] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        q_keywords: str | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        emailer_messages search

        Args:
          emailer_campaign_ids: Search for emails that are included in specific sequences in your Apollo
              account. You can search multiple sequences. Any sequence not included in this
              parameter will be exclude from search results.

              To find sequence IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-sequences" target="_blank">Search
              for Sequences endpoint</a> and identify the `id` value for the sequence.

              Example: `66e9e215ece19801b219997f`

          emailer_message_date_range_mode: Use this parameter in combination with the `emailer_message_date_range[max]` and
              `emailer_message_date_range[min]` parameters. Find emails based on 1 of the
              following options: <ul> <li> `due_at`: When emails are scheduled to be
              delivered. </li> <li> `completed_at`: When emails were delivered. </li> </ul>

          emailer_message_date_range_max: Set the upper bound of the date range you want to search.

              Use this parameter in combination with the `emailer_message_date_range[min]` and
              `emailer_message_date_range_mode` parameters. This date should fall after the
              `emailer_message_date_range[min]` date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-10-30`

          emailer_message_date_range_min: Set the lower bound of the date range you want to search.

              Use this parameter in combination with the `emailer_message_date_range[max]` and
              `emailer_message_date_range_mode` parameters. This date should fall before the
              `emailer_message_date_range[max]` date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-10-30`

          emailer_message_reply_classes: Find emails based on the response sentiment of the recipient. This can include
              the recipient expressing interest in meeting or having a follow-up question. You
              can add multiple values.

              Possible values include: <ul> <li> `willing_to_meet` </li> <li>
              `follow_up_question` </li> <li> `person_referral` </li> <li> `out_of_office`
              </li> <li> `already_left_company_or_not_right_person` </li> <li>
              `not_interested` </li> <li> `unsubscribe` </li> <li> `none_of_the_above` </li>
              </ul>

          emailer_message_stats: Find emails based on their current status, such as whether they were delivered
              or opened. You can add multiple statuses.

              Possible values include: <ul> <li> `delivered` </li> <li> `scheduled` </li> <li>
              `drafted` </li> <li> `not_opened` </li> <li> `opened` </li> <li> `clicked` </li>
              <li> `unsubscribed` </li> <li> `demoed` </li> <li> `bounced` </li> <li>
              `spam_blocked` </li> <li> `failed_other` </li> </ul>

          not_emailer_campaign_ids: Exclude emails from specific sequences in your Apollo account. You can exclude
              multiple sequences. Any sequence not excluded using this parameter will be
              included in search results.

              To find sequence IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-sequences" target="_blank">Search
              for Sequences endpoint</a> and identify the `id` value for the sequence.

              Example: `66e9e215ece19801b219997f`

          not_sent_reason_cds: Find emails based on the reason they were not sent. You can add multiple values.

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

          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          q_keywords: Add keywords to narrow the search of the emails in your team's Apollo account.

              Keywords should directly match at least part of an email's content. For example,
              searching the keyword `James` might return emails that were sent by
              `James Smith`.

              Example: `Jane`

          user_ids: Find emails sent by specific users in your team's Apollo account. You can add
              multiple users.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/emailer_messages/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email_account_id_and_aliases": email_account_id_and_aliases,
                        "emailer_campaign_ids": emailer_campaign_ids,
                        "emailer_message_date_range_mode": emailer_message_date_range_mode,
                        "emailer_message_date_range_max": emailer_message_date_range_max,
                        "emailer_message_date_range_min": emailer_message_date_range_min,
                        "emailer_message_reply_classes": emailer_message_reply_classes,
                        "emailer_message_stats": emailer_message_stats,
                        "not_emailer_campaign_ids": not_emailer_campaign_ids,
                        "not_sent_reason_cds": not_sent_reason_cds,
                        "page": page,
                        "per_page": per_page,
                        "q_keywords": q_keywords,
                        "user_ids": user_ids,
                    },
                    emailer_message_search_params.EmailerMessageSearchParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncEmailerMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailerMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailerMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailerMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncEmailerMessagesResourceWithStreamingResponse(self)

    async def activities(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        get_emailstats

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/emailer_messages/{id}/activities", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def search(
        self,
        *,
        email_account_id_and_aliases: str | Omit = omit,
        emailer_campaign_ids: SequenceNotStr[str] | Omit = omit,
        emailer_message_date_range_mode: str | Omit = omit,
        emailer_message_date_range_max: Union[str, date] | Omit = omit,
        emailer_message_date_range_min: Union[str, date] | Omit = omit,
        emailer_message_reply_classes: SequenceNotStr[str] | Omit = omit,
        emailer_message_stats: SequenceNotStr[str] | Omit = omit,
        not_emailer_campaign_ids: SequenceNotStr[str] | Omit = omit,
        not_sent_reason_cds: SequenceNotStr[str] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        q_keywords: str | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        emailer_messages search

        Args:
          emailer_campaign_ids: Search for emails that are included in specific sequences in your Apollo
              account. You can search multiple sequences. Any sequence not included in this
              parameter will be exclude from search results.

              To find sequence IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-sequences" target="_blank">Search
              for Sequences endpoint</a> and identify the `id` value for the sequence.

              Example: `66e9e215ece19801b219997f`

          emailer_message_date_range_mode: Use this parameter in combination with the `emailer_message_date_range[max]` and
              `emailer_message_date_range[min]` parameters. Find emails based on 1 of the
              following options: <ul> <li> `due_at`: When emails are scheduled to be
              delivered. </li> <li> `completed_at`: When emails were delivered. </li> </ul>

          emailer_message_date_range_max: Set the upper bound of the date range you want to search.

              Use this parameter in combination with the `emailer_message_date_range[min]` and
              `emailer_message_date_range_mode` parameters. This date should fall after the
              `emailer_message_date_range[min]` date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-10-30`

          emailer_message_date_range_min: Set the lower bound of the date range you want to search.

              Use this parameter in combination with the `emailer_message_date_range[max]` and
              `emailer_message_date_range_mode` parameters. This date should fall before the
              `emailer_message_date_range[max]` date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-10-30`

          emailer_message_reply_classes: Find emails based on the response sentiment of the recipient. This can include
              the recipient expressing interest in meeting or having a follow-up question. You
              can add multiple values.

              Possible values include: <ul> <li> `willing_to_meet` </li> <li>
              `follow_up_question` </li> <li> `person_referral` </li> <li> `out_of_office`
              </li> <li> `already_left_company_or_not_right_person` </li> <li>
              `not_interested` </li> <li> `unsubscribe` </li> <li> `none_of_the_above` </li>
              </ul>

          emailer_message_stats: Find emails based on their current status, such as whether they were delivered
              or opened. You can add multiple statuses.

              Possible values include: <ul> <li> `delivered` </li> <li> `scheduled` </li> <li>
              `drafted` </li> <li> `not_opened` </li> <li> `opened` </li> <li> `clicked` </li>
              <li> `unsubscribed` </li> <li> `demoed` </li> <li> `bounced` </li> <li>
              `spam_blocked` </li> <li> `failed_other` </li> </ul>

          not_emailer_campaign_ids: Exclude emails from specific sequences in your Apollo account. You can exclude
              multiple sequences. Any sequence not excluded using this parameter will be
              included in search results.

              To find sequence IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-sequences" target="_blank">Search
              for Sequences endpoint</a> and identify the `id` value for the sequence.

              Example: `66e9e215ece19801b219997f`

          not_sent_reason_cds: Find emails based on the reason they were not sent. You can add multiple values.

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

          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          q_keywords: Add keywords to narrow the search of the emails in your team's Apollo account.

              Keywords should directly match at least part of an email's content. For example,
              searching the keyword `James` might return emails that were sent by
              `James Smith`.

              Example: `Jane`

          user_ids: Find emails sent by specific users in your team's Apollo account. You can add
              multiple users.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/emailer_messages/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email_account_id_and_aliases": email_account_id_and_aliases,
                        "emailer_campaign_ids": emailer_campaign_ids,
                        "emailer_message_date_range_mode": emailer_message_date_range_mode,
                        "emailer_message_date_range_max": emailer_message_date_range_max,
                        "emailer_message_date_range_min": emailer_message_date_range_min,
                        "emailer_message_reply_classes": emailer_message_reply_classes,
                        "emailer_message_stats": emailer_message_stats,
                        "not_emailer_campaign_ids": not_emailer_campaign_ids,
                        "not_sent_reason_cds": not_sent_reason_cds,
                        "page": page,
                        "per_page": per_page,
                        "q_keywords": q_keywords,
                        "user_ids": user_ids,
                    },
                    emailer_message_search_params.EmailerMessageSearchParams,
                ),
            ),
            cast_to=NoneType,
        )


class EmailerMessagesResourceWithRawResponse:
    def __init__(self, emailer_messages: EmailerMessagesResource) -> None:
        self._emailer_messages = emailer_messages

        self.activities = to_raw_response_wrapper(
            emailer_messages.activities,
        )
        self.search = to_raw_response_wrapper(
            emailer_messages.search,
        )


class AsyncEmailerMessagesResourceWithRawResponse:
    def __init__(self, emailer_messages: AsyncEmailerMessagesResource) -> None:
        self._emailer_messages = emailer_messages

        self.activities = async_to_raw_response_wrapper(
            emailer_messages.activities,
        )
        self.search = async_to_raw_response_wrapper(
            emailer_messages.search,
        )


class EmailerMessagesResourceWithStreamingResponse:
    def __init__(self, emailer_messages: EmailerMessagesResource) -> None:
        self._emailer_messages = emailer_messages

        self.activities = to_streamed_response_wrapper(
            emailer_messages.activities,
        )
        self.search = to_streamed_response_wrapper(
            emailer_messages.search,
        )


class AsyncEmailerMessagesResourceWithStreamingResponse:
    def __init__(self, emailer_messages: AsyncEmailerMessagesResource) -> None:
        self._emailer_messages = emailer_messages

        self.activities = async_to_streamed_response_wrapper(
            emailer_messages.activities,
        )
        self.search = async_to_streamed_response_wrapper(
            emailer_messages.search,
        )
