# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime

import httpx

from ..types import phone_call_create_params, phone_call_search_params, phone_call_update_params
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

__all__ = ["PhoneCallsResource", "AsyncPhoneCallsResource"]


class PhoneCallsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PhoneCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return PhoneCallsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str | Omit = omit,
        contact_id: str | Omit = omit,
        duration: int | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        from_number: str | Omit = omit,
        logged: bool | Omit = omit,
        note: str | Omit = omit,
        phone_call_outcome_id: str | Omit = omit,
        phone_call_purpose_id: str | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        status: str | Omit = omit,
        to_number: str | Omit = omit,
        user_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        phonecalls_create

        Args:
          account_id: Associate the call with an account.

              Use the
              <a href="https://docs.apollo.io/reference/search-for-accounts#/" target="_blank">Search
              for Accounts endpoint</a> to retrieve IDs for all of the accounts within your
              Apollo account.

              Example: `66e9abf95ac32901b20d1a0d`

          contact_id: Designate the contact that was called.

              Use the
              <a href="https://docs.apollo.io/reference/search-for-contacts#/" target="_blank">Search
              for Contacts endpoint</a> to retrieve IDs for all of the contacts within your
              Apollo account.

              Example: `66e34b81740c50074e3d1bd4`

          duration: The duration of the call in seconds. Do not enter minutes.

              Examples: `120`; `205`

          end_time: The time when the call ended.

              Your entry should adhere to the ISO 8601 date-time format. Apollo uses Greenwich
              Mean Time (GMT) by default. If you do not account for time zone differences, you
              could add a end time that falls on a different day than you intended.

              The value you enter can either adhere to GMT, or you can adjust the time
              manually by specifiying in hours and minutes how much you want to offset GMT.

              Example: `2025-05-15T08:10:30Z`; `2025-05-25T10:15:30+05:00Z`

          from_number: The phone number that dialed you.

              Example: `5551234567`

          logged: Set to `true` if you want to create an individual record for the phone call in
              Apollo.

          note: Add a note to the call record.

              Example: `This lead is interested in learning more about our new product line.`

          phone_call_outcome_id: Assign a call outcome to the record.

              Call outcomes are unique to your team's Apollo account. When you use the
              <b>Disposition</b> search filter for calls in the Apollo product, you can find
              the corresponding call outcome ID in the URL.

              Examples: `6095a710bd01d100a506d4c5`

          phone_call_purpose_id: Assign a call purpose to the record.

              Call purposes are unique to your team's Apollo account. When you use the
              <b>Purpose</b> search filter for calls in the Apollo product, you can find the
              corresponding call purpose ID in the URL.

              Examples: `6095a710bd01d100a506d4cd`

          start_time: The time when the call started.

              Your entry should adhere to the ISO 8601 date-time format. Apollo uses Greenwich
              Mean Time (GMT) by default. If you do not account for time zone differences, you
              could add a start time that falls on a different day than you intended.

              The value you enter can either adhere to GMT, or you can adjust the time
              manually by specifiying in hours and minutes how much you want to offset GMT.

              Example: `2025-02-15T08:10:30Z`; `2025-03-25T10:15:30+05:00Z`

          status: The status of the phone call. Possible values include: <ul> <li>`queued`</li>
              <li>`ringing`</li> <li>`in-progress`</li> <li>`completed`</li>
              <li>`no_answer`</li> <li>`failed`</li> <li>`busy`</li></ul>

          to_number: The phone number that you dialed.

              Example: `5551234567`

          user_id: Designate the caller in your team's Apollo account.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `67e33d527de088000daa60c4`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/phone_calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "contact_id": contact_id,
                        "duration": duration,
                        "end_time": end_time,
                        "from_number": from_number,
                        "logged": logged,
                        "note": note,
                        "phone_call_outcome_id": phone_call_outcome_id,
                        "phone_call_purpose_id": phone_call_purpose_id,
                        "start_time": start_time,
                        "status": status,
                        "to_number": to_number,
                        "user_id": user_id,
                    },
                    phone_call_create_params.PhoneCallCreateParams,
                ),
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        id: str,
        *,
        account_id: str | Omit = omit,
        contact_id: str | Omit = omit,
        duration: int | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        from_number: str | Omit = omit,
        logged: bool | Omit = omit,
        note: str | Omit = omit,
        phone_call_outcome_id: str | Omit = omit,
        phone_call_purpose_id: str | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        status: str | Omit = omit,
        to_number: str | Omit = omit,
        user_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        put_phone_callsupdate

        Args:
          account_id: Associate the call with an account.

              Use the
              <a href="https://docs.apollo.io/reference/search-for-accounts#/" target="_blank">Search
              for Accounts endpoint</a> to retrieve IDs for all of the accounts within your
              Apollo account.

              Example: `66e9abf95ac32901b20d1a0d`

          contact_id: Designate the contact that was called.

              Use the
              <a href="https://docs.apollo.io/reference/search-for-contacts#/" target="_blank">Search
              for Contacts endpoint</a> to retrieve IDs for all of the contacts within your
              Apollo account.

              Example: `66e34b81740c50074e3d1bd4`

          duration: The duration of the call in seconds. Do not enter minutes.

              Examples: `120`; `205`

          end_time: The time when the call ended.

              Your entry should adhere to the ISO 8601 date-time format. Apollo uses Greenwich
              Mean Time (GMT) by default. If you do not account for time zone differences, you
              could add a end time that falls on a different day than you intended.

              The value you enter can either adhere to GMT, or you can adjust the time
              manually by specifiying in hours and minutes how much you want to offset GMT.

              Example: `2025-05-15T08:10:30Z`; `2025-05-25T10:15:30+05:00Z`

          from_number: The phone number that dialed you.

              Example: `5551234567`

          logged: Set to `true` if you want to create an individual record for the phone call in
              Apollo.

          note: Add a note to the call record.

              Example: `This lead is interested in learning more about our new product line.`

          phone_call_outcome_id: Assign a call outcome to the record.

              Call outcomes are unique to your team's Apollo account. When you use the
              <b>Disposition</b> search filter for calls in the Apollo product, you can find
              the corresponding call outcome ID in the URL.

              Examples: `6095a710bd01d100a506d4c5`

          phone_call_purpose_id: Assign a call purpose to the record.

              Call purposes are unique to your team's Apollo account. When you use the
              <b>Purpose</b> search filter for calls in the Apollo product, you can find the
              corresponding call purpose ID in the URL.

              Examples: `6095a710bd01d100a506d4cd`

          start_time: The time when the call started.

              Your entry should adhere to the ISO 8601 date-time format. Apollo uses Greenwich
              Mean Time (GMT) by default. If you do not account for time zone differences, you
              could add a start time that falls on a different day than you intended.

              The value you enter can either adhere to GMT, or you can adjust the time
              manually by specifiying in hours and minutes how much you want to offset GMT.

              Example: `2025-02-15T08:10:30Z`; `2025-03-25T10:15:30+05:00Z`

          status: The status of the phone call. Possible values include: <ul> <li>`queued`</li>
              <li>`ringing`</li> <li>`in-progress`</li> <li>`completed`</li>
              <li>`no_answer`</li> <li>`failed`</li> <li>`busy`</li></ul>

          to_number: The phone number that you dialed.

              Example: `5551234567`

          user_id: Designate the caller in your team's Apollo account.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `67e33d527de088000daa60c4`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template("/phone_calls/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "contact_id": contact_id,
                        "duration": duration,
                        "end_time": end_time,
                        "from_number": from_number,
                        "logged": logged,
                        "note": note,
                        "phone_call_outcome_id": phone_call_outcome_id,
                        "phone_call_purpose_id": phone_call_purpose_id,
                        "start_time": start_time,
                        "status": status,
                        "to_number": to_number,
                        "user_id": user_id,
                    },
                    phone_call_update_params.PhoneCallUpdateParams,
                ),
            ),
            cast_to=NoneType,
        )

    def search(
        self,
        *,
        contact_label_ids: SequenceNotStr[str] | Omit = omit,
        date_range_max: Union[str, date] | Omit = omit,
        date_range_min: Union[str, date] | Omit = omit,
        duration_max: int | Omit = omit,
        duration_min: int | Omit = omit,
        inbound: str | Omit = omit,
        page: str | Omit = omit,
        per_page: str | Omit = omit,
        phone_call_outcome_ids: SequenceNotStr[str] | Omit = omit,
        phone_call_purpose_ids: SequenceNotStr[str] | Omit = omit,
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
        get_phone_callssearch

        Args:
          contact_label_ids: Find calls that included specific contacts. You can add multiple contacts.

              In Apollo terminology, a contact is a person that your team has explicitly added
              to your database.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `67e33d527de088000daa60c4` 6708415f59d9c70001b2f852

          date_range_max: Set the upper bound of the date range you want to search.

              Use this parameter in combination with the `date_range[min]` parameter. This
              date should fall after the `date_range[min]` date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-06-12`

          date_range_min: Set the lower bound of the date range you want to search.

              Use this parameter in combination with the `date_range[max]` parameter. This
              date should fall before the `date_range[max]` date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-04-01`

          duration_max: Set the upper bound for the call duration you want to search. The duration
              should be seconds, not minutes or hours.

              Use this parameter in combination with the `duration[min]` parameter. This
              number should be larger than `duration[min]`.

              Example: `180`

          duration_min: Set the lower bound for the call duration you want to search. The duration
              should be seconds, not minutes or hours.

              Use this parameter in combination with the `duration[max]` parameter. This
              number should be smallerr than `duration[min]`.

              Example: `30`

          inbound: Search for calls based on whether they were `incoming` (the prospect called your
              team) or `outgoing` (your team called the prospect).

          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the page parameter to search the different pages of data.

              Example: `10`

          phone_call_outcome_ids: Filter calls based on their outcome.

              Call outcomes are unique to your team's Apollo account. When you use the
              <b>Disposition</b> search filter for calls in the Apollo product, you can find
              the corresponding call outcome ID in the URL.

              Example: `6095a710bd01d100a506d4c5`

          phone_call_purpose_ids: Filter calls based on their purpose.

              Call purposes are unique to your team's Apollo account. When you use the
              <b>Purpose</b> search filter for calls in the Apollo product, you can find the
              corresponding call purpose ID in the URL.

              Example: `6095a710bd01d100a506d4cf`

          q_keywords: Add keywords to narrow the search of the calls in your team's Apollo account.

              Example: `marketing conference attendees`

          user_ids: Find calls that included specific users in your team's Apollo account. You can
              add multiple users.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `67e33d527de088000daa60c4`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/phone_calls/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "contact_label_ids": contact_label_ids,
                        "date_range_max": date_range_max,
                        "date_range_min": date_range_min,
                        "duration_max": duration_max,
                        "duration_min": duration_min,
                        "inbound": inbound,
                        "page": page,
                        "per_page": per_page,
                        "phone_call_outcome_ids": phone_call_outcome_ids,
                        "phone_call_purpose_ids": phone_call_purpose_ids,
                        "q_keywords": q_keywords,
                        "user_ids": user_ids,
                    },
                    phone_call_search_params.PhoneCallSearchParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncPhoneCallsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncPhoneCallsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str | Omit = omit,
        contact_id: str | Omit = omit,
        duration: int | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        from_number: str | Omit = omit,
        logged: bool | Omit = omit,
        note: str | Omit = omit,
        phone_call_outcome_id: str | Omit = omit,
        phone_call_purpose_id: str | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        status: str | Omit = omit,
        to_number: str | Omit = omit,
        user_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        phonecalls_create

        Args:
          account_id: Associate the call with an account.

              Use the
              <a href="https://docs.apollo.io/reference/search-for-accounts#/" target="_blank">Search
              for Accounts endpoint</a> to retrieve IDs for all of the accounts within your
              Apollo account.

              Example: `66e9abf95ac32901b20d1a0d`

          contact_id: Designate the contact that was called.

              Use the
              <a href="https://docs.apollo.io/reference/search-for-contacts#/" target="_blank">Search
              for Contacts endpoint</a> to retrieve IDs for all of the contacts within your
              Apollo account.

              Example: `66e34b81740c50074e3d1bd4`

          duration: The duration of the call in seconds. Do not enter minutes.

              Examples: `120`; `205`

          end_time: The time when the call ended.

              Your entry should adhere to the ISO 8601 date-time format. Apollo uses Greenwich
              Mean Time (GMT) by default. If you do not account for time zone differences, you
              could add a end time that falls on a different day than you intended.

              The value you enter can either adhere to GMT, or you can adjust the time
              manually by specifiying in hours and minutes how much you want to offset GMT.

              Example: `2025-05-15T08:10:30Z`; `2025-05-25T10:15:30+05:00Z`

          from_number: The phone number that dialed you.

              Example: `5551234567`

          logged: Set to `true` if you want to create an individual record for the phone call in
              Apollo.

          note: Add a note to the call record.

              Example: `This lead is interested in learning more about our new product line.`

          phone_call_outcome_id: Assign a call outcome to the record.

              Call outcomes are unique to your team's Apollo account. When you use the
              <b>Disposition</b> search filter for calls in the Apollo product, you can find
              the corresponding call outcome ID in the URL.

              Examples: `6095a710bd01d100a506d4c5`

          phone_call_purpose_id: Assign a call purpose to the record.

              Call purposes are unique to your team's Apollo account. When you use the
              <b>Purpose</b> search filter for calls in the Apollo product, you can find the
              corresponding call purpose ID in the URL.

              Examples: `6095a710bd01d100a506d4cd`

          start_time: The time when the call started.

              Your entry should adhere to the ISO 8601 date-time format. Apollo uses Greenwich
              Mean Time (GMT) by default. If you do not account for time zone differences, you
              could add a start time that falls on a different day than you intended.

              The value you enter can either adhere to GMT, or you can adjust the time
              manually by specifiying in hours and minutes how much you want to offset GMT.

              Example: `2025-02-15T08:10:30Z`; `2025-03-25T10:15:30+05:00Z`

          status: The status of the phone call. Possible values include: <ul> <li>`queued`</li>
              <li>`ringing`</li> <li>`in-progress`</li> <li>`completed`</li>
              <li>`no_answer`</li> <li>`failed`</li> <li>`busy`</li></ul>

          to_number: The phone number that you dialed.

              Example: `5551234567`

          user_id: Designate the caller in your team's Apollo account.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `67e33d527de088000daa60c4`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/phone_calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "contact_id": contact_id,
                        "duration": duration,
                        "end_time": end_time,
                        "from_number": from_number,
                        "logged": logged,
                        "note": note,
                        "phone_call_outcome_id": phone_call_outcome_id,
                        "phone_call_purpose_id": phone_call_purpose_id,
                        "start_time": start_time,
                        "status": status,
                        "to_number": to_number,
                        "user_id": user_id,
                    },
                    phone_call_create_params.PhoneCallCreateParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        id: str,
        *,
        account_id: str | Omit = omit,
        contact_id: str | Omit = omit,
        duration: int | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        from_number: str | Omit = omit,
        logged: bool | Omit = omit,
        note: str | Omit = omit,
        phone_call_outcome_id: str | Omit = omit,
        phone_call_purpose_id: str | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        status: str | Omit = omit,
        to_number: str | Omit = omit,
        user_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        put_phone_callsupdate

        Args:
          account_id: Associate the call with an account.

              Use the
              <a href="https://docs.apollo.io/reference/search-for-accounts#/" target="_blank">Search
              for Accounts endpoint</a> to retrieve IDs for all of the accounts within your
              Apollo account.

              Example: `66e9abf95ac32901b20d1a0d`

          contact_id: Designate the contact that was called.

              Use the
              <a href="https://docs.apollo.io/reference/search-for-contacts#/" target="_blank">Search
              for Contacts endpoint</a> to retrieve IDs for all of the contacts within your
              Apollo account.

              Example: `66e34b81740c50074e3d1bd4`

          duration: The duration of the call in seconds. Do not enter minutes.

              Examples: `120`; `205`

          end_time: The time when the call ended.

              Your entry should adhere to the ISO 8601 date-time format. Apollo uses Greenwich
              Mean Time (GMT) by default. If you do not account for time zone differences, you
              could add a end time that falls on a different day than you intended.

              The value you enter can either adhere to GMT, or you can adjust the time
              manually by specifiying in hours and minutes how much you want to offset GMT.

              Example: `2025-05-15T08:10:30Z`; `2025-05-25T10:15:30+05:00Z`

          from_number: The phone number that dialed you.

              Example: `5551234567`

          logged: Set to `true` if you want to create an individual record for the phone call in
              Apollo.

          note: Add a note to the call record.

              Example: `This lead is interested in learning more about our new product line.`

          phone_call_outcome_id: Assign a call outcome to the record.

              Call outcomes are unique to your team's Apollo account. When you use the
              <b>Disposition</b> search filter for calls in the Apollo product, you can find
              the corresponding call outcome ID in the URL.

              Examples: `6095a710bd01d100a506d4c5`

          phone_call_purpose_id: Assign a call purpose to the record.

              Call purposes are unique to your team's Apollo account. When you use the
              <b>Purpose</b> search filter for calls in the Apollo product, you can find the
              corresponding call purpose ID in the URL.

              Examples: `6095a710bd01d100a506d4cd`

          start_time: The time when the call started.

              Your entry should adhere to the ISO 8601 date-time format. Apollo uses Greenwich
              Mean Time (GMT) by default. If you do not account for time zone differences, you
              could add a start time that falls on a different day than you intended.

              The value you enter can either adhere to GMT, or you can adjust the time
              manually by specifiying in hours and minutes how much you want to offset GMT.

              Example: `2025-02-15T08:10:30Z`; `2025-03-25T10:15:30+05:00Z`

          status: The status of the phone call. Possible values include: <ul> <li>`queued`</li>
              <li>`ringing`</li> <li>`in-progress`</li> <li>`completed`</li>
              <li>`no_answer`</li> <li>`failed`</li> <li>`busy`</li></ul>

          to_number: The phone number that you dialed.

              Example: `5551234567`

          user_id: Designate the caller in your team's Apollo account.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `67e33d527de088000daa60c4`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template("/phone_calls/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "contact_id": contact_id,
                        "duration": duration,
                        "end_time": end_time,
                        "from_number": from_number,
                        "logged": logged,
                        "note": note,
                        "phone_call_outcome_id": phone_call_outcome_id,
                        "phone_call_purpose_id": phone_call_purpose_id,
                        "start_time": start_time,
                        "status": status,
                        "to_number": to_number,
                        "user_id": user_id,
                    },
                    phone_call_update_params.PhoneCallUpdateParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def search(
        self,
        *,
        contact_label_ids: SequenceNotStr[str] | Omit = omit,
        date_range_max: Union[str, date] | Omit = omit,
        date_range_min: Union[str, date] | Omit = omit,
        duration_max: int | Omit = omit,
        duration_min: int | Omit = omit,
        inbound: str | Omit = omit,
        page: str | Omit = omit,
        per_page: str | Omit = omit,
        phone_call_outcome_ids: SequenceNotStr[str] | Omit = omit,
        phone_call_purpose_ids: SequenceNotStr[str] | Omit = omit,
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
        get_phone_callssearch

        Args:
          contact_label_ids: Find calls that included specific contacts. You can add multiple contacts.

              In Apollo terminology, a contact is a person that your team has explicitly added
              to your database.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `67e33d527de088000daa60c4` 6708415f59d9c70001b2f852

          date_range_max: Set the upper bound of the date range you want to search.

              Use this parameter in combination with the `date_range[min]` parameter. This
              date should fall after the `date_range[min]` date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-06-12`

          date_range_min: Set the lower bound of the date range you want to search.

              Use this parameter in combination with the `date_range[max]` parameter. This
              date should fall before the `date_range[max]` date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-04-01`

          duration_max: Set the upper bound for the call duration you want to search. The duration
              should be seconds, not minutes or hours.

              Use this parameter in combination with the `duration[min]` parameter. This
              number should be larger than `duration[min]`.

              Example: `180`

          duration_min: Set the lower bound for the call duration you want to search. The duration
              should be seconds, not minutes or hours.

              Use this parameter in combination with the `duration[max]` parameter. This
              number should be smallerr than `duration[min]`.

              Example: `30`

          inbound: Search for calls based on whether they were `incoming` (the prospect called your
              team) or `outgoing` (your team called the prospect).

          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the page parameter to search the different pages of data.

              Example: `10`

          phone_call_outcome_ids: Filter calls based on their outcome.

              Call outcomes are unique to your team's Apollo account. When you use the
              <b>Disposition</b> search filter for calls in the Apollo product, you can find
              the corresponding call outcome ID in the URL.

              Example: `6095a710bd01d100a506d4c5`

          phone_call_purpose_ids: Filter calls based on their purpose.

              Call purposes are unique to your team's Apollo account. When you use the
              <b>Purpose</b> search filter for calls in the Apollo product, you can find the
              corresponding call purpose ID in the URL.

              Example: `6095a710bd01d100a506d4cf`

          q_keywords: Add keywords to narrow the search of the calls in your team's Apollo account.

              Example: `marketing conference attendees`

          user_ids: Find calls that included specific users in your team's Apollo account. You can
              add multiple users.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `67e33d527de088000daa60c4`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/phone_calls/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "contact_label_ids": contact_label_ids,
                        "date_range_max": date_range_max,
                        "date_range_min": date_range_min,
                        "duration_max": duration_max,
                        "duration_min": duration_min,
                        "inbound": inbound,
                        "page": page,
                        "per_page": per_page,
                        "phone_call_outcome_ids": phone_call_outcome_ids,
                        "phone_call_purpose_ids": phone_call_purpose_ids,
                        "q_keywords": q_keywords,
                        "user_ids": user_ids,
                    },
                    phone_call_search_params.PhoneCallSearchParams,
                ),
            ),
            cast_to=NoneType,
        )


class PhoneCallsResourceWithRawResponse:
    def __init__(self, phone_calls: PhoneCallsResource) -> None:
        self._phone_calls = phone_calls

        self.create = to_raw_response_wrapper(
            phone_calls.create,
        )
        self.update = to_raw_response_wrapper(
            phone_calls.update,
        )
        self.search = to_raw_response_wrapper(
            phone_calls.search,
        )


class AsyncPhoneCallsResourceWithRawResponse:
    def __init__(self, phone_calls: AsyncPhoneCallsResource) -> None:
        self._phone_calls = phone_calls

        self.create = async_to_raw_response_wrapper(
            phone_calls.create,
        )
        self.update = async_to_raw_response_wrapper(
            phone_calls.update,
        )
        self.search = async_to_raw_response_wrapper(
            phone_calls.search,
        )


class PhoneCallsResourceWithStreamingResponse:
    def __init__(self, phone_calls: PhoneCallsResource) -> None:
        self._phone_calls = phone_calls

        self.create = to_streamed_response_wrapper(
            phone_calls.create,
        )
        self.update = to_streamed_response_wrapper(
            phone_calls.update,
        )
        self.search = to_streamed_response_wrapper(
            phone_calls.search,
        )


class AsyncPhoneCallsResourceWithStreamingResponse:
    def __init__(self, phone_calls: AsyncPhoneCallsResource) -> None:
        self._phone_calls = phone_calls

        self.create = async_to_streamed_response_wrapper(
            phone_calls.create,
        )
        self.update = async_to_streamed_response_wrapper(
            phone_calls.update,
        )
        self.search = async_to_streamed_response_wrapper(
            phone_calls.search,
        )
