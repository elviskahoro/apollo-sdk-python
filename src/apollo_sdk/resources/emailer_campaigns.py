# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    emailer_campaign_search_params,
    emailer_campaign_add_contacts_params,
    emailer_campaign_update_contact_status_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.emailer_campaign_search_response import EmailerCampaignSearchResponse
from ..types.emailer_campaign_archive_response import EmailerCampaignArchiveResponse
from ..types.emailer_campaign_activate_response import EmailerCampaignActivateResponse
from ..types.emailer_campaign_deactivate_response import EmailerCampaignDeactivateResponse
from ..types.emailer_campaign_add_contacts_response import EmailerCampaignAddContactsResponse
from ..types.emailer_campaign_update_contact_status_response import EmailerCampaignUpdateContactStatusResponse

__all__ = ["EmailerCampaignsResource", "AsyncEmailerCampaignsResource"]


class EmailerCampaignsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailerCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EmailerCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailerCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return EmailerCampaignsResourceWithStreamingResponse(self)

    def activate(
        self,
        sequence_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailerCampaignActivateResponse:
        """Use the Activate a Sequence endpoint to start an inactive sequence.

        Once
        activated, the sequence begins sending emails to its contacts on the configured
        schedule.

        The sequence must have at least 1 step configured before it can be activated.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a <code>403</code> response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sequence_id:
            raise ValueError(f"Expected a non-empty value for `sequence_id` but received {sequence_id!r}")
        return self._post(
            path_template("/emailer_campaigns/{sequence_id}/approve", sequence_id=sequence_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailerCampaignActivateResponse,
        )

    def add_contacts(
        self,
        sequence_id: str,
        *,
        emailer_campaign_id: str,
        send_email_from_email_account_id: str,
        add_if_in_queue: bool | Omit = omit,
        auto_unpause_at: Union[str, datetime] | Omit = omit,
        contact_ids: SequenceNotStr[str] | Omit = omit,
        contact_verification_skipped: bool | Omit = omit,
        contacts_without_ownership_permission: bool | Omit = omit,
        label_names: SequenceNotStr[str] | Omit = omit,
        send_email_from_email_address: str | Omit = omit,
        sequence_active_in_other_campaigns: bool | Omit = omit,
        sequence_finished_in_other_campaigns: bool | Omit = omit,
        sequence_job_change: bool | Omit = omit,
        sequence_no_email: bool | Omit = omit,
        sequence_same_company_in_same_campaign: bool | Omit = omit,
        sequence_unverified_email: bool | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailerCampaignAddContactsResponse:
        """
        Use the Add Contacts to a Sequence endpoint to add contacts to the existing
        sequences in your team's Apollo account.

        In Apollo terminology, a contact is a person that your team has explicitly added
        to your database. Only contacts can be added to sequences. To enrich a person's
        data so that they become a contact, call the
        <a href="https://docs.apollo.io/reference/people-enrichment" target="_blank">People
        Enrichment endpoint</a>.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          emailer_campaign_id: The same ID as the `sequence_id`.

              Example: `66e9e215ece19801b219997f`

          send_email_from_email_account_id: The Apollo ID for the email account that you want to use to send emails to the
              contacts you are adding to the sequence.

              To find email account IDs, call the
              <a href="https://docs.apollo.io/reference/get-a-list-of-email-accounts" target="_blank">Get
              a List of Email Accounts endpoint</a> and identify the `id` value for the email
              account.

              Example: `6633baaece5fbd01c791d7ca`

          add_if_in_queue: Set to `true` if you want to add contacts even if they are currently in the
              queue for processing.

          auto_unpause_at: DateTime when paused contacts should be automatically unpaused. Must be used
              with `status=paused`. Format: ISO 8601 datetime string.

          contact_ids: The Apollo IDs for the contacts that you want to add to the sequence.

              To find contact IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
              for Contacts endpoint</a> and identify the `id` value for the contact.

              Example: `66e34b81740c50074e3d1bd4`

              Note: Either `contact_ids[]` or `label_names[]` must be provided.

          contact_verification_skipped: Set to `true` if you want to skip contact verification during the addition
              process.

          contacts_without_ownership_permission: Set to `true` if you want to add contacts even if you don't have ownership
              permission for them.

          label_names: Alternative to `contact_ids[]`. Array of label names to identify contacts to add
              to the sequence. Contacts with these labels will be added to the sequence.

              Note: Either `contact_ids[]` or `label_names[]` must be provided.

          send_email_from_email_address: Optional specific email address to send from within the email account.

          sequence_active_in_other_campaigns: Set to `true` if you want to add contacts to the sequence even if they have been
              added to other sequences. This parameter does not differentiate between active
              and paused sequences.

          sequence_finished_in_other_campaigns: Set to `true` if you want to add contacts to the sequence if they have been
              marked as `finished` in another sequence.

          sequence_job_change: Set to `true` if you want to add contacts to the sequence even if they have
              recently changed jobs.

          sequence_no_email: Set to `true` if you want to add contacts to the sequence even if they do not
              have an email address.

          sequence_same_company_in_same_campaign: Set to `true` if you want to add contacts to the sequence even if other contacts
              from the same company are already in the sequence.

          sequence_unverified_email: Set to `true` if you want to add contacts to the sequence if they have an
              unverified email address.

          status: Initial status for added contacts. When set to `paused` along with
              `auto_unpause_at`, enables scheduled addition of contacts.

          user_id: The ID for the user in your team's Apollo account.

              This is the user taking the action to add contacts to a sequence. When the
              sequence is updated, the activity log shows the user that added the contacts.

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
        if not sequence_id:
            raise ValueError(f"Expected a non-empty value for `sequence_id` but received {sequence_id!r}")
        return self._post(
            path_template("/emailer_campaigns/{sequence_id}/add_contact_ids", sequence_id=sequence_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "emailer_campaign_id": emailer_campaign_id,
                        "send_email_from_email_account_id": send_email_from_email_account_id,
                        "add_if_in_queue": add_if_in_queue,
                        "auto_unpause_at": auto_unpause_at,
                        "contact_ids": contact_ids,
                        "contact_verification_skipped": contact_verification_skipped,
                        "contacts_without_ownership_permission": contacts_without_ownership_permission,
                        "label_names": label_names,
                        "send_email_from_email_address": send_email_from_email_address,
                        "sequence_active_in_other_campaigns": sequence_active_in_other_campaigns,
                        "sequence_finished_in_other_campaigns": sequence_finished_in_other_campaigns,
                        "sequence_job_change": sequence_job_change,
                        "sequence_no_email": sequence_no_email,
                        "sequence_same_company_in_same_campaign": sequence_same_company_in_same_campaign,
                        "sequence_unverified_email": sequence_unverified_email,
                        "status": status,
                        "user_id": user_id,
                    },
                    emailer_campaign_add_contacts_params.EmailerCampaignAddContactsParams,
                ),
            ),
            cast_to=EmailerCampaignAddContactsResponse,
        )

    def archive(
        self,
        sequence_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailerCampaignArchiveResponse:
        """Use the Archive a Sequence endpoint to archive a sequence.

        Archiving a sequence
        marks it as inactive and finishes all contacts currently in the sequence.

        You must be the owner of the sequence or have full access sharing permissions to
        archive it.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a <code>403</code> response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sequence_id:
            raise ValueError(f"Expected a non-empty value for `sequence_id` but received {sequence_id!r}")
        return self._post(
            path_template("/emailer_campaigns/{sequence_id}/archive", sequence_id=sequence_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailerCampaignArchiveResponse,
        )

    def deactivate(
        self,
        sequence_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailerCampaignDeactivateResponse:
        """Use the Deactivate a Sequence endpoint to stop an active sequence.

        Once
        deactivated, the sequence pauses all contacts and stops sending emails.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a <code>403</code> response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sequence_id:
            raise ValueError(f"Expected a non-empty value for `sequence_id` but received {sequence_id!r}")
        return self._post(
            path_template("/emailer_campaigns/{sequence_id}/abort", sequence_id=sequence_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailerCampaignDeactivateResponse,
        )

    def search(
        self,
        *,
        page: str | Omit = omit,
        per_page: str | Omit = omit,
        q_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailerCampaignSearchResponse:
        """
        Use the Search for Sequences endpoint to search for the sequences that have been
        created for your team's Apollo account.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          q_name: Add keywords to narrow the search of the sequences in your team's Apollo
              account.

              Keywords should directly match at least part of a sequence's name. For example,
              searching the keyword `marketing` might return the result
              `NY Marketing Sequence`, but not `NY Marketer Conference 2025 attendees`.

              This parameter only searches sequence names, not other sequence fields.

              Example: `marketing conference attendees`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/emailer_campaigns/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "q_name": q_name,
                    },
                    emailer_campaign_search_params.EmailerCampaignSearchParams,
                ),
            ),
            cast_to=EmailerCampaignSearchResponse,
        )

    def update_contact_status(
        self,
        *,
        contact_ids: SequenceNotStr[str],
        emailer_campaign_ids: SequenceNotStr[str],
        mode: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailerCampaignUpdateContactStatusResponse:
        """
        Use the Update Contact Status in a Sequence endpoint to either mark contacts as
        having `finished` a sequence, or to remove them from a sequence entirely.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          contact_ids: The Apollo IDs for the contacts in the sequences. These are the contacts whose
              sequence status you want to update.

              To find contact IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
              for Contacts endpoint</a> and identify the `id` value for the contact.

              Example: `66e34b81740c50074e3d1bd4`

          emailer_campaign_ids: The Apollo IDs for the sequences that you want to update. If you add multiple
              sequences, you will update the status of the contacts across the chosen
              sequences.

              To find sequence IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-sequences" target="_blank">Search
              for Sequences endpoint</a> and identify the `id` value for the sequence.

              Example: `66e9e215ece19801b219997f`

          mode:
              Choose 1 of the following options to update the sequence status of the contacts:
              <ul> <li> `mark_as_finished`: Mark the contacts as having finished the sequence.
              </li> <li> `remove`: Remove the contacts from the sequence. </li> <li> `stop`:
              Indicate that the contacts progress in the sequence has halted. </li> </ul>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/emailer_campaigns/remove_or_stop_contact_ids",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "contact_ids": contact_ids,
                        "emailer_campaign_ids": emailer_campaign_ids,
                        "mode": mode,
                    },
                    emailer_campaign_update_contact_status_params.EmailerCampaignUpdateContactStatusParams,
                ),
            ),
            cast_to=EmailerCampaignUpdateContactStatusResponse,
        )


class AsyncEmailerCampaignsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailerCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailerCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailerCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncEmailerCampaignsResourceWithStreamingResponse(self)

    async def activate(
        self,
        sequence_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailerCampaignActivateResponse:
        """Use the Activate a Sequence endpoint to start an inactive sequence.

        Once
        activated, the sequence begins sending emails to its contacts on the configured
        schedule.

        The sequence must have at least 1 step configured before it can be activated.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a <code>403</code> response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sequence_id:
            raise ValueError(f"Expected a non-empty value for `sequence_id` but received {sequence_id!r}")
        return await self._post(
            path_template("/emailer_campaigns/{sequence_id}/approve", sequence_id=sequence_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailerCampaignActivateResponse,
        )

    async def add_contacts(
        self,
        sequence_id: str,
        *,
        emailer_campaign_id: str,
        send_email_from_email_account_id: str,
        add_if_in_queue: bool | Omit = omit,
        auto_unpause_at: Union[str, datetime] | Omit = omit,
        contact_ids: SequenceNotStr[str] | Omit = omit,
        contact_verification_skipped: bool | Omit = omit,
        contacts_without_ownership_permission: bool | Omit = omit,
        label_names: SequenceNotStr[str] | Omit = omit,
        send_email_from_email_address: str | Omit = omit,
        sequence_active_in_other_campaigns: bool | Omit = omit,
        sequence_finished_in_other_campaigns: bool | Omit = omit,
        sequence_job_change: bool | Omit = omit,
        sequence_no_email: bool | Omit = omit,
        sequence_same_company_in_same_campaign: bool | Omit = omit,
        sequence_unverified_email: bool | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailerCampaignAddContactsResponse:
        """
        Use the Add Contacts to a Sequence endpoint to add contacts to the existing
        sequences in your team's Apollo account.

        In Apollo terminology, a contact is a person that your team has explicitly added
        to your database. Only contacts can be added to sequences. To enrich a person's
        data so that they become a contact, call the
        <a href="https://docs.apollo.io/reference/people-enrichment" target="_blank">People
        Enrichment endpoint</a>.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          emailer_campaign_id: The same ID as the `sequence_id`.

              Example: `66e9e215ece19801b219997f`

          send_email_from_email_account_id: The Apollo ID for the email account that you want to use to send emails to the
              contacts you are adding to the sequence.

              To find email account IDs, call the
              <a href="https://docs.apollo.io/reference/get-a-list-of-email-accounts" target="_blank">Get
              a List of Email Accounts endpoint</a> and identify the `id` value for the email
              account.

              Example: `6633baaece5fbd01c791d7ca`

          add_if_in_queue: Set to `true` if you want to add contacts even if they are currently in the
              queue for processing.

          auto_unpause_at: DateTime when paused contacts should be automatically unpaused. Must be used
              with `status=paused`. Format: ISO 8601 datetime string.

          contact_ids: The Apollo IDs for the contacts that you want to add to the sequence.

              To find contact IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
              for Contacts endpoint</a> and identify the `id` value for the contact.

              Example: `66e34b81740c50074e3d1bd4`

              Note: Either `contact_ids[]` or `label_names[]` must be provided.

          contact_verification_skipped: Set to `true` if you want to skip contact verification during the addition
              process.

          contacts_without_ownership_permission: Set to `true` if you want to add contacts even if you don't have ownership
              permission for them.

          label_names: Alternative to `contact_ids[]`. Array of label names to identify contacts to add
              to the sequence. Contacts with these labels will be added to the sequence.

              Note: Either `contact_ids[]` or `label_names[]` must be provided.

          send_email_from_email_address: Optional specific email address to send from within the email account.

          sequence_active_in_other_campaigns: Set to `true` if you want to add contacts to the sequence even if they have been
              added to other sequences. This parameter does not differentiate between active
              and paused sequences.

          sequence_finished_in_other_campaigns: Set to `true` if you want to add contacts to the sequence if they have been
              marked as `finished` in another sequence.

          sequence_job_change: Set to `true` if you want to add contacts to the sequence even if they have
              recently changed jobs.

          sequence_no_email: Set to `true` if you want to add contacts to the sequence even if they do not
              have an email address.

          sequence_same_company_in_same_campaign: Set to `true` if you want to add contacts to the sequence even if other contacts
              from the same company are already in the sequence.

          sequence_unverified_email: Set to `true` if you want to add contacts to the sequence if they have an
              unverified email address.

          status: Initial status for added contacts. When set to `paused` along with
              `auto_unpause_at`, enables scheduled addition of contacts.

          user_id: The ID for the user in your team's Apollo account.

              This is the user taking the action to add contacts to a sequence. When the
              sequence is updated, the activity log shows the user that added the contacts.

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
        if not sequence_id:
            raise ValueError(f"Expected a non-empty value for `sequence_id` but received {sequence_id!r}")
        return await self._post(
            path_template("/emailer_campaigns/{sequence_id}/add_contact_ids", sequence_id=sequence_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "emailer_campaign_id": emailer_campaign_id,
                        "send_email_from_email_account_id": send_email_from_email_account_id,
                        "add_if_in_queue": add_if_in_queue,
                        "auto_unpause_at": auto_unpause_at,
                        "contact_ids": contact_ids,
                        "contact_verification_skipped": contact_verification_skipped,
                        "contacts_without_ownership_permission": contacts_without_ownership_permission,
                        "label_names": label_names,
                        "send_email_from_email_address": send_email_from_email_address,
                        "sequence_active_in_other_campaigns": sequence_active_in_other_campaigns,
                        "sequence_finished_in_other_campaigns": sequence_finished_in_other_campaigns,
                        "sequence_job_change": sequence_job_change,
                        "sequence_no_email": sequence_no_email,
                        "sequence_same_company_in_same_campaign": sequence_same_company_in_same_campaign,
                        "sequence_unverified_email": sequence_unverified_email,
                        "status": status,
                        "user_id": user_id,
                    },
                    emailer_campaign_add_contacts_params.EmailerCampaignAddContactsParams,
                ),
            ),
            cast_to=EmailerCampaignAddContactsResponse,
        )

    async def archive(
        self,
        sequence_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailerCampaignArchiveResponse:
        """Use the Archive a Sequence endpoint to archive a sequence.

        Archiving a sequence
        marks it as inactive and finishes all contacts currently in the sequence.

        You must be the owner of the sequence or have full access sharing permissions to
        archive it.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a <code>403</code> response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sequence_id:
            raise ValueError(f"Expected a non-empty value for `sequence_id` but received {sequence_id!r}")
        return await self._post(
            path_template("/emailer_campaigns/{sequence_id}/archive", sequence_id=sequence_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailerCampaignArchiveResponse,
        )

    async def deactivate(
        self,
        sequence_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailerCampaignDeactivateResponse:
        """Use the Deactivate a Sequence endpoint to stop an active sequence.

        Once
        deactivated, the sequence pauses all contacts and stops sending emails.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a <code>403</code> response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sequence_id:
            raise ValueError(f"Expected a non-empty value for `sequence_id` but received {sequence_id!r}")
        return await self._post(
            path_template("/emailer_campaigns/{sequence_id}/abort", sequence_id=sequence_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailerCampaignDeactivateResponse,
        )

    async def search(
        self,
        *,
        page: str | Omit = omit,
        per_page: str | Omit = omit,
        q_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailerCampaignSearchResponse:
        """
        Use the Search for Sequences endpoint to search for the sequences that have been
        created for your team's Apollo account.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          q_name: Add keywords to narrow the search of the sequences in your team's Apollo
              account.

              Keywords should directly match at least part of a sequence's name. For example,
              searching the keyword `marketing` might return the result
              `NY Marketing Sequence`, but not `NY Marketer Conference 2025 attendees`.

              This parameter only searches sequence names, not other sequence fields.

              Example: `marketing conference attendees`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/emailer_campaigns/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "q_name": q_name,
                    },
                    emailer_campaign_search_params.EmailerCampaignSearchParams,
                ),
            ),
            cast_to=EmailerCampaignSearchResponse,
        )

    async def update_contact_status(
        self,
        *,
        contact_ids: SequenceNotStr[str],
        emailer_campaign_ids: SequenceNotStr[str],
        mode: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailerCampaignUpdateContactStatusResponse:
        """
        Use the Update Contact Status in a Sequence endpoint to either mark contacts as
        having `finished` a sequence, or to remove them from a sequence entirely.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          contact_ids: The Apollo IDs for the contacts in the sequences. These are the contacts whose
              sequence status you want to update.

              To find contact IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
              for Contacts endpoint</a> and identify the `id` value for the contact.

              Example: `66e34b81740c50074e3d1bd4`

          emailer_campaign_ids: The Apollo IDs for the sequences that you want to update. If you add multiple
              sequences, you will update the status of the contacts across the chosen
              sequences.

              To find sequence IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-sequences" target="_blank">Search
              for Sequences endpoint</a> and identify the `id` value for the sequence.

              Example: `66e9e215ece19801b219997f`

          mode:
              Choose 1 of the following options to update the sequence status of the contacts:
              <ul> <li> `mark_as_finished`: Mark the contacts as having finished the sequence.
              </li> <li> `remove`: Remove the contacts from the sequence. </li> <li> `stop`:
              Indicate that the contacts progress in the sequence has halted. </li> </ul>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/emailer_campaigns/remove_or_stop_contact_ids",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "contact_ids": contact_ids,
                        "emailer_campaign_ids": emailer_campaign_ids,
                        "mode": mode,
                    },
                    emailer_campaign_update_contact_status_params.EmailerCampaignUpdateContactStatusParams,
                ),
            ),
            cast_to=EmailerCampaignUpdateContactStatusResponse,
        )


class EmailerCampaignsResourceWithRawResponse:
    def __init__(self, emailer_campaigns: EmailerCampaignsResource) -> None:
        self._emailer_campaigns = emailer_campaigns

        self.activate = to_raw_response_wrapper(
            emailer_campaigns.activate,
        )
        self.add_contacts = to_raw_response_wrapper(
            emailer_campaigns.add_contacts,
        )
        self.archive = to_raw_response_wrapper(
            emailer_campaigns.archive,
        )
        self.deactivate = to_raw_response_wrapper(
            emailer_campaigns.deactivate,
        )
        self.search = to_raw_response_wrapper(
            emailer_campaigns.search,
        )
        self.update_contact_status = to_raw_response_wrapper(
            emailer_campaigns.update_contact_status,
        )


class AsyncEmailerCampaignsResourceWithRawResponse:
    def __init__(self, emailer_campaigns: AsyncEmailerCampaignsResource) -> None:
        self._emailer_campaigns = emailer_campaigns

        self.activate = async_to_raw_response_wrapper(
            emailer_campaigns.activate,
        )
        self.add_contacts = async_to_raw_response_wrapper(
            emailer_campaigns.add_contacts,
        )
        self.archive = async_to_raw_response_wrapper(
            emailer_campaigns.archive,
        )
        self.deactivate = async_to_raw_response_wrapper(
            emailer_campaigns.deactivate,
        )
        self.search = async_to_raw_response_wrapper(
            emailer_campaigns.search,
        )
        self.update_contact_status = async_to_raw_response_wrapper(
            emailer_campaigns.update_contact_status,
        )


class EmailerCampaignsResourceWithStreamingResponse:
    def __init__(self, emailer_campaigns: EmailerCampaignsResource) -> None:
        self._emailer_campaigns = emailer_campaigns

        self.activate = to_streamed_response_wrapper(
            emailer_campaigns.activate,
        )
        self.add_contacts = to_streamed_response_wrapper(
            emailer_campaigns.add_contacts,
        )
        self.archive = to_streamed_response_wrapper(
            emailer_campaigns.archive,
        )
        self.deactivate = to_streamed_response_wrapper(
            emailer_campaigns.deactivate,
        )
        self.search = to_streamed_response_wrapper(
            emailer_campaigns.search,
        )
        self.update_contact_status = to_streamed_response_wrapper(
            emailer_campaigns.update_contact_status,
        )


class AsyncEmailerCampaignsResourceWithStreamingResponse:
    def __init__(self, emailer_campaigns: AsyncEmailerCampaignsResource) -> None:
        self._emailer_campaigns = emailer_campaigns

        self.activate = async_to_streamed_response_wrapper(
            emailer_campaigns.activate,
        )
        self.add_contacts = async_to_streamed_response_wrapper(
            emailer_campaigns.add_contacts,
        )
        self.archive = async_to_streamed_response_wrapper(
            emailer_campaigns.archive,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            emailer_campaigns.deactivate,
        )
        self.search = async_to_streamed_response_wrapper(
            emailer_campaigns.search,
        )
        self.update_contact_status = async_to_streamed_response_wrapper(
            emailer_campaigns.update_contact_status,
        )
