# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    account_create_params,
    account_search_params,
    account_update_params,
    account_bulk_create_params,
    account_bulk_update_params,
    account_update_owners_params,
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
from ..types.account_create_response import AccountCreateResponse
from ..types.account_search_response import AccountSearchResponse
from ..types.account_update_response import AccountUpdateResponse
from ..types.account_retrieve_response import AccountRetrieveResponse
from ..types.account_bulk_create_response import AccountBulkCreateResponse
from ..types.account_bulk_update_response import AccountBulkUpdateResponse
from ..types.account_update_owners_response import AccountUpdateOwnersResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_stage_id: str | Omit = omit,
        domain: str | Omit = omit,
        name: str | Omit = omit,
        owner_id: str | Omit = omit,
        phone: str | Omit = omit,
        raw_address: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountCreateResponse:
        """
        Use the Create an Account endpoint to add a new account to your team's Apollo
        account.

        In Apollo terminology, an account is a company that your team has explicitly
        added to your database.

        Apollo does not apply deduplication processes when you create a new account via
        the API. If your entry has the same name, domain, or other details as an
        existing account, Apollo will create a new account instead of updating the
        existing account. To update an existing account, use the
        <a href="https://docs.apollo.io/reference/update-an-account" target="_blank">Update
        an Account endpoint</a> instead.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          account_stage_id: The Apollo ID for the account stage to which you want to assign the account.
              Call the
              <a href="https://docs.apollo.io/reference/list-account-stages" target="_blank">List
              Account Stages endpoint</a> to retrieve a list of all the account stage IDs
              available in your Apollo account.

              If you do not specify the account stage, Apollo automatically assigns the
              account to a stage as determined by your team's Apollo account. To change the
              order of account stages, launch the Apollo product and go to <b>Settings</b> >
              <b>Objects</b> >
              <a href="https://app.apollo.io/#/settings/accounts/stages" target="_blank"><b>Accounts</b></a>.
              Then, access the <b>Triggers</b> tab and change the stage for when an account is
              created.

              Example: `6095a710bd01d100a506d4b9`

          domain: The domain name for the account.

              Do not include `www.` or similar.

              Example: `apollo.io` or `microsoft.com`

          name: Name the account that you are creating. This should be a human-readable name.

              Example: `The Irish Copywriters`

          owner_id: The ID for the account owner within your team's Apollo account.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          phone: The primary phone number for the account.

              This can be the phone number for the corporate headquarters, a branch location,
              or a direct dial to the primary point of contact for the account.

              Apollo sanitizes phone numbers, so you can enter them in any format. The
              sanitized number can be viewed in the endpoint response.

              Examples: `555-303-1234`; `+44 7911 123456`

          raw_address: The corporate location for the account. This can include a city, US state, and
              country.

              Apollo matches the location you provide to the most applicable pre-defined
              location.

              Examples: `Belfield, Dublin 4, Ireland`; `Dallas, United States`

          typed_custom_fields: Add information to
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498754445-Create-Custom-Account-Fields" target="_blank">custom
              fields</a> in Apollo.

              <b>Your custom fields are unique to your team's Apollo account. This means that
              the examples in this documentation may not work for your testing purposes.</b>

              To utilize this parameter successfully, call the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint and identify the `id` value for the
              custom field, as well as the appropriate data type. For example, if a custom
              field accepts picklist entries, you need to pass the accompanying `id` value for
              the picklist entry that you want to use as the input value.

              <b>Example</b>: When the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint returns an `id` of field:

              - `"60c39ed82bd02f01154c470a"` (datetime)

              then the value passed should be:

              `{"60c39ed82bd02f01154c470a": "2025-08-07"}`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/accounts",
            body=maybe_transform(
                {
                    "account_stage_id": account_stage_id,
                    "domain": domain,
                    "name": name,
                    "owner_id": owner_id,
                    "phone": phone,
                    "raw_address": raw_address,
                    "typed_custom_fields": typed_custom_fields,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCreateResponse,
        )

    def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountRetrieveResponse:
        """
        Use the View an Account endpoint to retrieve complete details about an account
        in your team's Apollo account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveResponse,
        )

    def update(
        self,
        account_id: str,
        *,
        account_stage_id: str | Omit = omit,
        domain: str | Omit = omit,
        name: str | Omit = omit,
        owner_id: str | Omit = omit,
        phone: str | Omit = omit,
        raw_address: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountUpdateResponse:
        """
        Use the Update an Account endpoint to update existing accounts in your team's
        Apollo account.

        In Apollo terminology, an account is a company that your team has explicitly
        added to your database.

        To create a new account, use the
        <a href="https://docs.apollo.io/reference/create-an-account" target="_blank">Create
        an Account endpoint</a> instead. To update the account stage for multiple
        account, use the
        <a href="https://docs.apollo.io/reference/update-account-stage" target="_blank">Update
        Account Stage for Multiple Accounts endpoint</a>.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          account_stage_id: The Apollo ID for the account stage to which you want to assign the account.
              Enter a different ID to update the account stage.

              Call the
              <a href="https://docs.apollo.io/reference/list-account-stages" target="_blank">List
              Account Stages endpoint</a> to retrieve a list of all the account stage IDs
              available in your Apollo account.

              If you do not specify the account stage, Apollo automatically assigns the
              account to a stage as determined by your team's Apollo account. To change the
              order of account stages, launch the Apollo product and go to <b>Settings</b> >
              <b>Objects</b> >
              <a href="https://app.apollo.io/#/settings/accounts/stages" target="_blank"><b>Accounts</b></a>.
              Then, access the <b>Triggers</b> tab and change the stage for when an account is
              created.

              Example: `61b8e913e0f4d2012e3af74e`

          domain: Update the domain name for the account. Do not include `www.` or similar.

              Example: `apollo.io` or `microsoft.com`

          name: Update the account's name. This should be a human-readable name.

              Example: `The Fast Irish Copywriters`

          owner_id: The ID for the account owner within your team's Apollo account. Enter a
              different ID to update the owner of the account.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          phone: Update the primary phone number for the account.

              This can be the phone number for the corporate headquarters, a branch location,
              or a direct dial to the primary point of contact for the account.

              Apollo sanitizes phone numbers, so you can enter them in any format. The
              sanitized number can be viewed in the endpoint response.

              Examples: `555-303-1234`; `+44 7911 123456`

          raw_address: Update the corporate location for the account. This can include a city, US
              state, and country.

              Apollo matches the location you provide to the most applicable pre-defined
              location.

              Examples: `Belfield, Dublin 4, Ireland`; `Dallas, United States`

          typed_custom_fields: Add information to
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498754445-Create-Custom-Account-Fields" target="_blank">custom
              fields</a> in Apollo.

              <b>Your custom fields are unique to your team's Apollo account. This means that
              the examples in this documentation may not work for your testing purposes.</b>

              To utilize this parameter successfully, call the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint and identify the `id` value for the
              custom field, as well as the appropriate data type. For example, if a custom
              field accepts picklist entries, you need to pass the accompanying `id` value for
              the picklist entry that you want to use as the input value.

              <b>Example</b>: When the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint returns an `id` of field:

              - `"60c39ed82bd02f01154c470a"` (datetime)

              then the value passed should be:

              `{"60c39ed82bd02f01154c470a": "2025-08-07"}`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            path_template("/accounts/{account_id}", account_id=account_id),
            body=maybe_transform(
                {
                    "account_stage_id": account_stage_id,
                    "domain": domain,
                    "name": name,
                    "owner_id": owner_id,
                    "phone": phone,
                    "raw_address": raw_address,
                    "typed_custom_fields": typed_custom_fields,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUpdateResponse,
        )

    def bulk_create(
        self,
        *,
        accounts: Iterable[account_bulk_create_params.Account],
        append_label_names: SequenceNotStr[str] | Omit = omit,
        run_dedupe: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountBulkCreateResponse:
        """
        Use the Bulk Create Accounts endpoint to create multiple accounts in a single
        API request. This endpoint supports intelligent deduplication, CRM integration,
        and batch processing of up to 100 accounts per request.

        <strong>Important:</strong> This endpoint creates new accounts but does NOT
        update existing ones. Existing accounts that match the criteria will be returned
        in the existing_accounts array without modification. To update existing
        accounts, use the
        <a href="https://docs.apollo.io/reference/update-account-stage" target="_blank">Bulk
        Update Accounts endpoint</a>.

        The endpoint can operate in two modes: default mode (matches by CRM IDs only) or
        aggressive deduplication mode (matches by domain, organization_id, and name as
        well).

        For creating individual accounts, use the
        <a href="https://docs.apollo.io/reference/create-an-account" target="_blank">Create
        an Account endpoint</a> instead.

        Args:
          accounts: Array of account attribute objects (maximum 100 accounts per request)

          append_label_names: Array of label names to add to ALL accounts in this request

          run_dedupe: Enable aggressive deduplication by domain, organization_id, and name. When false
              (default), only matches by CRM IDs. When true, also matches by domain,
              organization_id, and name. Existing accounts are returned without modification
              in both modes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/accounts/bulk_create",
            body=maybe_transform(
                {
                    "accounts": accounts,
                    "append_label_names": append_label_names,
                    "run_dedupe": run_dedupe,
                },
                account_bulk_create_params.AccountBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountBulkCreateResponse,
        )

    def bulk_update(
        self,
        *,
        account_attributes: Iterable[account_bulk_update_params.AccountAttribute] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        account_stage_id: str | Omit = omit,
        async_: bool | Omit = omit,
        name: str | Omit = omit,
        owner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountBulkUpdateResponse:
        """
        Use the Bulk Update Accounts endpoint to update multiple accounts in your team's
        Apollo account simultaneously.

        This endpoint allows you to update common fields across multiple accounts
        efficiently, such as account stages, owners, names, and custom fields.

        You can update up to 1000 accounts per request.

        <strong>Important:</strong> Asynchronous processing (async parameter) is only
        supported when using account_ids to apply the same updates to all accounts. If
        you attempt to use async with account_attributes (individual updates per
        account), the request will fail with a 422 error.

        For updating individual accounts, use the
        <a href="https://docs.apollo.io/reference/update-an-account" target="_blank">Update
        an Account endpoint</a> instead.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          account_attributes: Array of account objects with individual updates. Use this for applying
              different updates to each account.

          account_ids: Array of account IDs to update with the same values. Use this for applying the
              same updates to multiple accounts.

          account_stage_id: When using account_ids, apply this account stage to all accounts

          async_: Set to true to process updates asynchronously. Only available when using
              account_ids. Not supported with account_attributes.

          name: When using account_ids, apply this name to all accounts

          owner_id: When using account_ids, apply this owner to all accounts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/accounts/bulk_update",
            body=maybe_transform(
                {
                    "account_attributes": account_attributes,
                    "account_ids": account_ids,
                    "account_stage_id": account_stage_id,
                    "async_": async_,
                    "name": name,
                    "owner_id": owner_id,
                },
                account_bulk_update_params.AccountBulkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountBulkUpdateResponse,
        )

    def search(
        self,
        *,
        account_label_ids: SequenceNotStr[str] | Omit = omit,
        account_stage_ids: SequenceNotStr[str] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        q_organization_name: str | Omit = omit,
        sort_ascending: bool | Omit = omit,
        sort_by_field: Literal["account_last_activity_date", "account_created_at", "account_updated_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountSearchResponse:
        """
        Use the Search for Accounts endpoint to search for the account that have been
        added to your team's Apollo account.

        In Apollo terminology, an account is a company that your team has explicitly
        added to your database.

        This endpoint only returns accounts in the search results. To search for
        companies in the Apollo database, call the
        <a href="https://docs.apollo.io/reference/organization-search" target="_blank">Organization
        Search endpoint</a>.

        To protect Apollo's performance for all users, this endpoint has a display limit
        of 50,000 records (100 records per page, up to 500 pages). Add more filters to
        narrow your search results as much as possible. This limitation does not
        restrict your access to Apollo's database; you just need to access the data in
        batches.

        Args:
          account_label_ids: The Apollo IDs for the labels that you want to include in your search results.
              If you add multiple labels, Apollo will include all accounts connected to any of
              the labels, along with the other parameters, in the search results. Example:
              `['6095a710bd01d100a506d4ae']`

          account_stage_ids: The Apollo IDs for the account stages that you want to include in your search
              results. If you add multiple account stages, Apollo will include all accounts
              that match any of the stages, along with the other parameters, in the search
              results. Call the
              [List Account Stages endpoint](https://docs.apollo.io/reference/list-account-stages)
              to retrieve a list of all the account stage IDs available in your Apollo
              account. Example: `61b8e913e0f4d2012e3af74e`

          page: The page number of the Apollo data that you want to retrieve. Use this parameter
              in combination with the `per_page` parameter to make search results navigable
              and improve the performance of the endpoint. Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance. Use the `page`
              parameter to navigate through the different pages of data. Example: `10`

          q_organization_name: Add keywords to narrow the search of the accounts in your team's Apollo account.
              Keywords should directly match at least part of an account's name. For example,
              searching the keyword `marketing` might return the result
              `NY Marketing Unlimited`, but not `NY Market Analysts`. This parameter only
              searches account names, not other account fields. Examples: `apollo`;
              `microsoft`; `marketing`

          sort_ascending: Set to `true` to sort the matching accounts in ascending order. This parameter
              must be used with `sort_by_field`. Otherwise, the sorting logic is not applied.
              Example: `true`

          sort_by_field:
              Sort the matching accounts by 1 of the following options:

              - `account_last_activity_date`: The most recent activity date recorded first.
              - `account_created_at`: The most recently created first.
              - `account_updated_at`: The most recently updated first.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/accounts/search",
            body=maybe_transform(
                {
                    "account_label_ids": account_label_ids,
                    "account_stage_ids": account_stage_ids,
                    "page": page,
                    "per_page": per_page,
                    "q_organization_name": q_organization_name,
                    "sort_ascending": sort_ascending,
                    "sort_by_field": sort_by_field,
                },
                account_search_params.AccountSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountSearchResponse,
        )

    def update_owners(
        self,
        *,
        account_ids: SequenceNotStr[str],
        owner_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountUpdateOwnersResponse:
        """
        Use the Update Account Owner for Multiple Accounts endpoint to assign multiple
        accounts to a different user in your team's Apollo account.

        To update more than the account owner, such as domains or phone numbers, use the
        <a href="https://docs.apollo.io/reference/update-an-account" target="_blank">Update
        an Account endpoint</a> instead.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          account_ids: The Apollo IDs for the account that you want to assign to an owner.

              To find account IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-accounts" target="_blank">Search
              for Accounts endpoint</a> and identify the `id` value for the account.

              Example: `66e9abf95ac32901b20d1a0d`

          owner_id: The ID for the account owner within your team's Apollo account. This user will
              be assigned ownership of the accounts.

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
        return self._post(
            "/accounts/update_owners",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query={
                    "account_ids%5B%5D": account_ids[0] if len(account_ids) == 1 else account_ids,
                    "owner_id": owner_id,
                },
            ),
            cast_to=AccountUpdateOwnersResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_stage_id: str | Omit = omit,
        domain: str | Omit = omit,
        name: str | Omit = omit,
        owner_id: str | Omit = omit,
        phone: str | Omit = omit,
        raw_address: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountCreateResponse:
        """
        Use the Create an Account endpoint to add a new account to your team's Apollo
        account.

        In Apollo terminology, an account is a company that your team has explicitly
        added to your database.

        Apollo does not apply deduplication processes when you create a new account via
        the API. If your entry has the same name, domain, or other details as an
        existing account, Apollo will create a new account instead of updating the
        existing account. To update an existing account, use the
        <a href="https://docs.apollo.io/reference/update-an-account" target="_blank">Update
        an Account endpoint</a> instead.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          account_stage_id: The Apollo ID for the account stage to which you want to assign the account.
              Call the
              <a href="https://docs.apollo.io/reference/list-account-stages" target="_blank">List
              Account Stages endpoint</a> to retrieve a list of all the account stage IDs
              available in your Apollo account.

              If you do not specify the account stage, Apollo automatically assigns the
              account to a stage as determined by your team's Apollo account. To change the
              order of account stages, launch the Apollo product and go to <b>Settings</b> >
              <b>Objects</b> >
              <a href="https://app.apollo.io/#/settings/accounts/stages" target="_blank"><b>Accounts</b></a>.
              Then, access the <b>Triggers</b> tab and change the stage for when an account is
              created.

              Example: `6095a710bd01d100a506d4b9`

          domain: The domain name for the account.

              Do not include `www.` or similar.

              Example: `apollo.io` or `microsoft.com`

          name: Name the account that you are creating. This should be a human-readable name.

              Example: `The Irish Copywriters`

          owner_id: The ID for the account owner within your team's Apollo account.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          phone: The primary phone number for the account.

              This can be the phone number for the corporate headquarters, a branch location,
              or a direct dial to the primary point of contact for the account.

              Apollo sanitizes phone numbers, so you can enter them in any format. The
              sanitized number can be viewed in the endpoint response.

              Examples: `555-303-1234`; `+44 7911 123456`

          raw_address: The corporate location for the account. This can include a city, US state, and
              country.

              Apollo matches the location you provide to the most applicable pre-defined
              location.

              Examples: `Belfield, Dublin 4, Ireland`; `Dallas, United States`

          typed_custom_fields: Add information to
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498754445-Create-Custom-Account-Fields" target="_blank">custom
              fields</a> in Apollo.

              <b>Your custom fields are unique to your team's Apollo account. This means that
              the examples in this documentation may not work for your testing purposes.</b>

              To utilize this parameter successfully, call the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint and identify the `id` value for the
              custom field, as well as the appropriate data type. For example, if a custom
              field accepts picklist entries, you need to pass the accompanying `id` value for
              the picklist entry that you want to use as the input value.

              <b>Example</b>: When the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint returns an `id` of field:

              - `"60c39ed82bd02f01154c470a"` (datetime)

              then the value passed should be:

              `{"60c39ed82bd02f01154c470a": "2025-08-07"}`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/accounts",
            body=await async_maybe_transform(
                {
                    "account_stage_id": account_stage_id,
                    "domain": domain,
                    "name": name,
                    "owner_id": owner_id,
                    "phone": phone,
                    "raw_address": raw_address,
                    "typed_custom_fields": typed_custom_fields,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCreateResponse,
        )

    async def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountRetrieveResponse:
        """
        Use the View an Account endpoint to retrieve complete details about an account
        in your team's Apollo account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveResponse,
        )

    async def update(
        self,
        account_id: str,
        *,
        account_stage_id: str | Omit = omit,
        domain: str | Omit = omit,
        name: str | Omit = omit,
        owner_id: str | Omit = omit,
        phone: str | Omit = omit,
        raw_address: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountUpdateResponse:
        """
        Use the Update an Account endpoint to update existing accounts in your team's
        Apollo account.

        In Apollo terminology, an account is a company that your team has explicitly
        added to your database.

        To create a new account, use the
        <a href="https://docs.apollo.io/reference/create-an-account" target="_blank">Create
        an Account endpoint</a> instead. To update the account stage for multiple
        account, use the
        <a href="https://docs.apollo.io/reference/update-account-stage" target="_blank">Update
        Account Stage for Multiple Accounts endpoint</a>.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          account_stage_id: The Apollo ID for the account stage to which you want to assign the account.
              Enter a different ID to update the account stage.

              Call the
              <a href="https://docs.apollo.io/reference/list-account-stages" target="_blank">List
              Account Stages endpoint</a> to retrieve a list of all the account stage IDs
              available in your Apollo account.

              If you do not specify the account stage, Apollo automatically assigns the
              account to a stage as determined by your team's Apollo account. To change the
              order of account stages, launch the Apollo product and go to <b>Settings</b> >
              <b>Objects</b> >
              <a href="https://app.apollo.io/#/settings/accounts/stages" target="_blank"><b>Accounts</b></a>.
              Then, access the <b>Triggers</b> tab and change the stage for when an account is
              created.

              Example: `61b8e913e0f4d2012e3af74e`

          domain: Update the domain name for the account. Do not include `www.` or similar.

              Example: `apollo.io` or `microsoft.com`

          name: Update the account's name. This should be a human-readable name.

              Example: `The Fast Irish Copywriters`

          owner_id: The ID for the account owner within your team's Apollo account. Enter a
              different ID to update the owner of the account.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          phone: Update the primary phone number for the account.

              This can be the phone number for the corporate headquarters, a branch location,
              or a direct dial to the primary point of contact for the account.

              Apollo sanitizes phone numbers, so you can enter them in any format. The
              sanitized number can be viewed in the endpoint response.

              Examples: `555-303-1234`; `+44 7911 123456`

          raw_address: Update the corporate location for the account. This can include a city, US
              state, and country.

              Apollo matches the location you provide to the most applicable pre-defined
              location.

              Examples: `Belfield, Dublin 4, Ireland`; `Dallas, United States`

          typed_custom_fields: Add information to
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498754445-Create-Custom-Account-Fields" target="_blank">custom
              fields</a> in Apollo.

              <b>Your custom fields are unique to your team's Apollo account. This means that
              the examples in this documentation may not work for your testing purposes.</b>

              To utilize this parameter successfully, call the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint and identify the `id` value for the
              custom field, as well as the appropriate data type. For example, if a custom
              field accepts picklist entries, you need to pass the accompanying `id` value for
              the picklist entry that you want to use as the input value.

              <b>Example</b>: When the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint returns an `id` of field:

              - `"60c39ed82bd02f01154c470a"` (datetime)

              then the value passed should be:

              `{"60c39ed82bd02f01154c470a": "2025-08-07"}`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            path_template("/accounts/{account_id}", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "account_stage_id": account_stage_id,
                    "domain": domain,
                    "name": name,
                    "owner_id": owner_id,
                    "phone": phone,
                    "raw_address": raw_address,
                    "typed_custom_fields": typed_custom_fields,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUpdateResponse,
        )

    async def bulk_create(
        self,
        *,
        accounts: Iterable[account_bulk_create_params.Account],
        append_label_names: SequenceNotStr[str] | Omit = omit,
        run_dedupe: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountBulkCreateResponse:
        """
        Use the Bulk Create Accounts endpoint to create multiple accounts in a single
        API request. This endpoint supports intelligent deduplication, CRM integration,
        and batch processing of up to 100 accounts per request.

        <strong>Important:</strong> This endpoint creates new accounts but does NOT
        update existing ones. Existing accounts that match the criteria will be returned
        in the existing_accounts array without modification. To update existing
        accounts, use the
        <a href="https://docs.apollo.io/reference/update-account-stage" target="_blank">Bulk
        Update Accounts endpoint</a>.

        The endpoint can operate in two modes: default mode (matches by CRM IDs only) or
        aggressive deduplication mode (matches by domain, organization_id, and name as
        well).

        For creating individual accounts, use the
        <a href="https://docs.apollo.io/reference/create-an-account" target="_blank">Create
        an Account endpoint</a> instead.

        Args:
          accounts: Array of account attribute objects (maximum 100 accounts per request)

          append_label_names: Array of label names to add to ALL accounts in this request

          run_dedupe: Enable aggressive deduplication by domain, organization_id, and name. When false
              (default), only matches by CRM IDs. When true, also matches by domain,
              organization_id, and name. Existing accounts are returned without modification
              in both modes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/accounts/bulk_create",
            body=await async_maybe_transform(
                {
                    "accounts": accounts,
                    "append_label_names": append_label_names,
                    "run_dedupe": run_dedupe,
                },
                account_bulk_create_params.AccountBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountBulkCreateResponse,
        )

    async def bulk_update(
        self,
        *,
        account_attributes: Iterable[account_bulk_update_params.AccountAttribute] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        account_stage_id: str | Omit = omit,
        async_: bool | Omit = omit,
        name: str | Omit = omit,
        owner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountBulkUpdateResponse:
        """
        Use the Bulk Update Accounts endpoint to update multiple accounts in your team's
        Apollo account simultaneously.

        This endpoint allows you to update common fields across multiple accounts
        efficiently, such as account stages, owners, names, and custom fields.

        You can update up to 1000 accounts per request.

        <strong>Important:</strong> Asynchronous processing (async parameter) is only
        supported when using account_ids to apply the same updates to all accounts. If
        you attempt to use async with account_attributes (individual updates per
        account), the request will fail with a 422 error.

        For updating individual accounts, use the
        <a href="https://docs.apollo.io/reference/update-an-account" target="_blank">Update
        an Account endpoint</a> instead.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          account_attributes: Array of account objects with individual updates. Use this for applying
              different updates to each account.

          account_ids: Array of account IDs to update with the same values. Use this for applying the
              same updates to multiple accounts.

          account_stage_id: When using account_ids, apply this account stage to all accounts

          async_: Set to true to process updates asynchronously. Only available when using
              account_ids. Not supported with account_attributes.

          name: When using account_ids, apply this name to all accounts

          owner_id: When using account_ids, apply this owner to all accounts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/accounts/bulk_update",
            body=await async_maybe_transform(
                {
                    "account_attributes": account_attributes,
                    "account_ids": account_ids,
                    "account_stage_id": account_stage_id,
                    "async_": async_,
                    "name": name,
                    "owner_id": owner_id,
                },
                account_bulk_update_params.AccountBulkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountBulkUpdateResponse,
        )

    async def search(
        self,
        *,
        account_label_ids: SequenceNotStr[str] | Omit = omit,
        account_stage_ids: SequenceNotStr[str] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        q_organization_name: str | Omit = omit,
        sort_ascending: bool | Omit = omit,
        sort_by_field: Literal["account_last_activity_date", "account_created_at", "account_updated_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountSearchResponse:
        """
        Use the Search for Accounts endpoint to search for the account that have been
        added to your team's Apollo account.

        In Apollo terminology, an account is a company that your team has explicitly
        added to your database.

        This endpoint only returns accounts in the search results. To search for
        companies in the Apollo database, call the
        <a href="https://docs.apollo.io/reference/organization-search" target="_blank">Organization
        Search endpoint</a>.

        To protect Apollo's performance for all users, this endpoint has a display limit
        of 50,000 records (100 records per page, up to 500 pages). Add more filters to
        narrow your search results as much as possible. This limitation does not
        restrict your access to Apollo's database; you just need to access the data in
        batches.

        Args:
          account_label_ids: The Apollo IDs for the labels that you want to include in your search results.
              If you add multiple labels, Apollo will include all accounts connected to any of
              the labels, along with the other parameters, in the search results. Example:
              `['6095a710bd01d100a506d4ae']`

          account_stage_ids: The Apollo IDs for the account stages that you want to include in your search
              results. If you add multiple account stages, Apollo will include all accounts
              that match any of the stages, along with the other parameters, in the search
              results. Call the
              [List Account Stages endpoint](https://docs.apollo.io/reference/list-account-stages)
              to retrieve a list of all the account stage IDs available in your Apollo
              account. Example: `61b8e913e0f4d2012e3af74e`

          page: The page number of the Apollo data that you want to retrieve. Use this parameter
              in combination with the `per_page` parameter to make search results navigable
              and improve the performance of the endpoint. Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance. Use the `page`
              parameter to navigate through the different pages of data. Example: `10`

          q_organization_name: Add keywords to narrow the search of the accounts in your team's Apollo account.
              Keywords should directly match at least part of an account's name. For example,
              searching the keyword `marketing` might return the result
              `NY Marketing Unlimited`, but not `NY Market Analysts`. This parameter only
              searches account names, not other account fields. Examples: `apollo`;
              `microsoft`; `marketing`

          sort_ascending: Set to `true` to sort the matching accounts in ascending order. This parameter
              must be used with `sort_by_field`. Otherwise, the sorting logic is not applied.
              Example: `true`

          sort_by_field:
              Sort the matching accounts by 1 of the following options:

              - `account_last_activity_date`: The most recent activity date recorded first.
              - `account_created_at`: The most recently created first.
              - `account_updated_at`: The most recently updated first.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/accounts/search",
            body=await async_maybe_transform(
                {
                    "account_label_ids": account_label_ids,
                    "account_stage_ids": account_stage_ids,
                    "page": page,
                    "per_page": per_page,
                    "q_organization_name": q_organization_name,
                    "sort_ascending": sort_ascending,
                    "sort_by_field": sort_by_field,
                },
                account_search_params.AccountSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountSearchResponse,
        )

    async def update_owners(
        self,
        *,
        account_ids: SequenceNotStr[str],
        owner_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountUpdateOwnersResponse:
        """
        Use the Update Account Owner for Multiple Accounts endpoint to assign multiple
        accounts to a different user in your team's Apollo account.

        To update more than the account owner, such as domains or phone numbers, use the
        <a href="https://docs.apollo.io/reference/update-an-account" target="_blank">Update
        an Account endpoint</a> instead.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          account_ids: The Apollo IDs for the account that you want to assign to an owner.

              To find account IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-accounts" target="_blank">Search
              for Accounts endpoint</a> and identify the `id` value for the account.

              Example: `66e9abf95ac32901b20d1a0d`

          owner_id: The ID for the account owner within your team's Apollo account. This user will
              be assigned ownership of the accounts.

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
        return await self._post(
            "/accounts/update_owners",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query={
                    "account_ids%5B%5D": account_ids[0] if len(account_ids) == 1 else account_ids,
                    "owner_id": owner_id,
                },
            ),
            cast_to=AccountUpdateOwnersResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_raw_response_wrapper(
            accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            accounts.update,
        )
        self.bulk_create = to_raw_response_wrapper(
            accounts.bulk_create,
        )
        self.bulk_update = to_raw_response_wrapper(
            accounts.bulk_update,
        )
        self.search = to_raw_response_wrapper(
            accounts.search,
        )
        self.update_owners = to_raw_response_wrapper(
            accounts.update_owners,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_raw_response_wrapper(
            accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            accounts.bulk_create,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            accounts.bulk_update,
        )
        self.search = async_to_raw_response_wrapper(
            accounts.search,
        )
        self.update_owners = async_to_raw_response_wrapper(
            accounts.update_owners,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_streamed_response_wrapper(
            accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.bulk_create = to_streamed_response_wrapper(
            accounts.bulk_create,
        )
        self.bulk_update = to_streamed_response_wrapper(
            accounts.bulk_update,
        )
        self.search = to_streamed_response_wrapper(
            accounts.search,
        )
        self.update_owners = to_streamed_response_wrapper(
            accounts.update_owners,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_streamed_response_wrapper(
            accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            accounts.bulk_create,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            accounts.bulk_update,
        )
        self.search = async_to_streamed_response_wrapper(
            accounts.search,
        )
        self.update_owners = async_to_streamed_response_wrapper(
            accounts.update_owners,
        )
