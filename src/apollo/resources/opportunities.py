# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import date

import httpx

from ..types import opportunity_list_params, opportunity_create_params, opportunity_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.opportunity_list_response import OpportunityListResponse
from ..types.opportunity_create_response import OpportunityCreateResponse
from ..types.opportunity_update_response import OpportunityUpdateResponse
from ..types.opportunity_retrieve_response import OpportunityRetrieveResponse

__all__ = ["OpportunitiesResource", "AsyncOpportunitiesResource"]


class OpportunitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpportunitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OpportunitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpportunitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return OpportunitiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        account_id: str | Omit = omit,
        amount: str | Omit = omit,
        closed_date: Union[str, date] | Omit = omit,
        opportunity_stage_id: str | Omit = omit,
        owner_id: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpportunityCreateResponse:
        """Use the Create Deal endpoint to create new deals for an Apollo account.

        Deals
        enable you to track account activity, including monetary values of a deal, deal
        owners, and deal stages.

        To update existing deals in your Apollo account, use the
        <a href="https://docs.apollo.io/reference/update-deal" target="_blank">Update
        Deal endpoint</a> instead.

        This endpoint also requires a master API key. If you attempt to call the
        endpoint without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          name: Name the deal you are creating. This should be a human-readable name.

              Example: `Massive Q3 Deal`

          account_id: The ID for the account within your Apollo instance. This is the company that you
              are targeting as part of the deal being created.

              Each company in the Apollo database is assigned a unique ID. To find IDs, call
              the
              <a href="https://docs.apollo.io/reference/organization-search" target="_blank">Organization
              Search endpoint</a> and identify the values for `organization_id`.

              Example: `5e66b6381e05b4008c8331b8`

          amount: The monetary value of the deal being created.

              Do not enter commas or currency symbols for the value. The currency is
              automatically populated by the settings within your Apollo account. Commas are
              not accepted and result in the deal amount being left blank.

              Example: `55123478` (results in a deal value of `$55,123,478` if the default
              currency is USD)

          closed_date: The estimated close date for the deal. This can be a future or past date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-10-30`

          opportunity_stage_id: The ID for the deal stage within your team's Apollo account.

              Each deal stage is assigned a unique ID. To find deal stage IDs, call the
              <a href="https://docs.apollo.io/reference/list-deal-stages" target="_blank">List
              Deal Stages endpoint</a> and identify the value for `id` for each stage.

              Example: `6095a710bd01d100a506d4bd`

          owner_id: The ID for the deal owner within your team's Apollo account.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          typed_custom_fields: Add information to
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4415062486669-Create-a-Deal" target="_blank">custom
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
            "/opportunities",
            body=maybe_transform(
                {
                    "name": name,
                    "account_id": account_id,
                    "amount": amount,
                    "closed_date": closed_date,
                    "opportunity_stage_id": opportunity_stage_id,
                    "owner_id": owner_id,
                    "typed_custom_fields": typed_custom_fields,
                },
                opportunity_create_params.OpportunityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpportunityCreateResponse,
        )

    def retrieve(
        self,
        opportunity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpportunityRetrieveResponse:
        """
        Use the View Deal endpoint to retrieve complete details about a deal within your
        team's Apollo account.

        Deal information can include the ID of the deal owner, the monetary value of the
        deal, the deal stage, and general details about the account.

        This endpoint also requires a master API key. If you attempt to call the
        endpoint without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not opportunity_id:
            raise ValueError(f"Expected a non-empty value for `opportunity_id` but received {opportunity_id!r}")
        return self._get(
            path_template("/opportunities/{opportunity_id}", opportunity_id=opportunity_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpportunityRetrieveResponse,
        )

    def update(
        self,
        opportunity_id: str,
        *,
        amount: str | Omit = omit,
        closed_date: Union[str, date] | Omit = omit,
        name: str | Omit = omit,
        opportunity_stage_id: str | Omit = omit,
        owner_id: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpportunityUpdateResponse:
        """
        Use the Update Deal endpoint to update the details of existing deals within your
        team's Apollo account. Deals enable you to track account activity, including
        monetary values of a deal, deal owners, and deal stages.

        To create new deals in your Apollo account, use the
        <a href="https://docs.apollo.io/reference/create-deal" target="_blank">Create
        Deal endpoint</a> instead.

        This endpoint also requires a master API key. If you attempt to call the
        endpoint without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          amount: The monetary value of the deal. Enter a different value to update the deal
              amount.

              Do not enter commas or currency symbols for the value. The currency is
              automatically populated by the settings within your Apollo account. Commas are
              not accepted and result in the deal amount being left blank.

              Example: `55123478` (results in a deal value of `$55,123,478` if the default
              currency is USD)

          closed_date: Update the estimated close date for the deal. This can be a future or past date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-10-30`

          name: Update the name of the deal. This should be a human-readable name.

              Example: `Massive Q3 Deal`

          opportunity_stage_id: The ID for the deal stage within your team's Apollo account. Enter a different
              ID to update the deal stage.

              Each deal stage is assigned a unique ID. To find deal stage IDs, call the
              <a href="https://docs.apollo.io/reference/get-a-list-of-opportunity-stages" target="_blank">List
              Deal Stages endpoint</a> and identify the value for `id` for each stage.

              Example: `6095a710bd01d100a506d4bd`

          owner_id: The ID for the deal owner within your team's Apollo account. Enter a different
              ID to update the owner of the deal.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          typed_custom_fields: Add information to
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4415062486669-Create-a-Deal" target="_blank">custom
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
        if not opportunity_id:
            raise ValueError(f"Expected a non-empty value for `opportunity_id` but received {opportunity_id!r}")
        return self._patch(
            path_template("/opportunities/{opportunity_id}", opportunity_id=opportunity_id),
            body=maybe_transform(
                {
                    "amount": amount,
                    "closed_date": closed_date,
                    "name": name,
                    "opportunity_stage_id": opportunity_stage_id,
                    "owner_id": owner_id,
                    "typed_custom_fields": typed_custom_fields,
                },
                opportunity_update_params.OpportunityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpportunityUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort_by_field: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpportunityListResponse:
        """
        Use the List All Deals endpoint to retrieve every deal that has been created for
        your team's Apollo account.

        This endpoint also requires a master API key. If you attempt to call the
        endpoint without a master key, you will receive a `403` response. Refer to
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

          sort_by_field: Sort the tasks by 1 of the following options: <ul> <li> `amount`: The largest
              deal values first. </li> <li> `is_closed`: Deals that have been closed first.
              </li> <li> `is_won`: Deals that have been won first. </li> </ul>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/opportunities/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "sort_by_field": sort_by_field,
                    },
                    opportunity_list_params.OpportunityListParams,
                ),
            ),
            cast_to=OpportunityListResponse,
        )


class AsyncOpportunitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpportunitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOpportunitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpportunitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncOpportunitiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        account_id: str | Omit = omit,
        amount: str | Omit = omit,
        closed_date: Union[str, date] | Omit = omit,
        opportunity_stage_id: str | Omit = omit,
        owner_id: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpportunityCreateResponse:
        """Use the Create Deal endpoint to create new deals for an Apollo account.

        Deals
        enable you to track account activity, including monetary values of a deal, deal
        owners, and deal stages.

        To update existing deals in your Apollo account, use the
        <a href="https://docs.apollo.io/reference/update-deal" target="_blank">Update
        Deal endpoint</a> instead.

        This endpoint also requires a master API key. If you attempt to call the
        endpoint without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          name: Name the deal you are creating. This should be a human-readable name.

              Example: `Massive Q3 Deal`

          account_id: The ID for the account within your Apollo instance. This is the company that you
              are targeting as part of the deal being created.

              Each company in the Apollo database is assigned a unique ID. To find IDs, call
              the
              <a href="https://docs.apollo.io/reference/organization-search" target="_blank">Organization
              Search endpoint</a> and identify the values for `organization_id`.

              Example: `5e66b6381e05b4008c8331b8`

          amount: The monetary value of the deal being created.

              Do not enter commas or currency symbols for the value. The currency is
              automatically populated by the settings within your Apollo account. Commas are
              not accepted and result in the deal amount being left blank.

              Example: `55123478` (results in a deal value of `$55,123,478` if the default
              currency is USD)

          closed_date: The estimated close date for the deal. This can be a future or past date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-10-30`

          opportunity_stage_id: The ID for the deal stage within your team's Apollo account.

              Each deal stage is assigned a unique ID. To find deal stage IDs, call the
              <a href="https://docs.apollo.io/reference/list-deal-stages" target="_blank">List
              Deal Stages endpoint</a> and identify the value for `id` for each stage.

              Example: `6095a710bd01d100a506d4bd`

          owner_id: The ID for the deal owner within your team's Apollo account.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          typed_custom_fields: Add information to
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4415062486669-Create-a-Deal" target="_blank">custom
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
            "/opportunities",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "account_id": account_id,
                    "amount": amount,
                    "closed_date": closed_date,
                    "opportunity_stage_id": opportunity_stage_id,
                    "owner_id": owner_id,
                    "typed_custom_fields": typed_custom_fields,
                },
                opportunity_create_params.OpportunityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpportunityCreateResponse,
        )

    async def retrieve(
        self,
        opportunity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpportunityRetrieveResponse:
        """
        Use the View Deal endpoint to retrieve complete details about a deal within your
        team's Apollo account.

        Deal information can include the ID of the deal owner, the monetary value of the
        deal, the deal stage, and general details about the account.

        This endpoint also requires a master API key. If you attempt to call the
        endpoint without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not opportunity_id:
            raise ValueError(f"Expected a non-empty value for `opportunity_id` but received {opportunity_id!r}")
        return await self._get(
            path_template("/opportunities/{opportunity_id}", opportunity_id=opportunity_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpportunityRetrieveResponse,
        )

    async def update(
        self,
        opportunity_id: str,
        *,
        amount: str | Omit = omit,
        closed_date: Union[str, date] | Omit = omit,
        name: str | Omit = omit,
        opportunity_stage_id: str | Omit = omit,
        owner_id: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpportunityUpdateResponse:
        """
        Use the Update Deal endpoint to update the details of existing deals within your
        team's Apollo account. Deals enable you to track account activity, including
        monetary values of a deal, deal owners, and deal stages.

        To create new deals in your Apollo account, use the
        <a href="https://docs.apollo.io/reference/create-deal" target="_blank">Create
        Deal endpoint</a> instead.

        This endpoint also requires a master API key. If you attempt to call the
        endpoint without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          amount: The monetary value of the deal. Enter a different value to update the deal
              amount.

              Do not enter commas or currency symbols for the value. The currency is
              automatically populated by the settings within your Apollo account. Commas are
              not accepted and result in the deal amount being left blank.

              Example: `55123478` (results in a deal value of `$55,123,478` if the default
              currency is USD)

          closed_date: Update the estimated close date for the deal. This can be a future or past date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-10-30`

          name: Update the name of the deal. This should be a human-readable name.

              Example: `Massive Q3 Deal`

          opportunity_stage_id: The ID for the deal stage within your team's Apollo account. Enter a different
              ID to update the deal stage.

              Each deal stage is assigned a unique ID. To find deal stage IDs, call the
              <a href="https://docs.apollo.io/reference/get-a-list-of-opportunity-stages" target="_blank">List
              Deal Stages endpoint</a> and identify the value for `id` for each stage.

              Example: `6095a710bd01d100a506d4bd`

          owner_id: The ID for the deal owner within your team's Apollo account. Enter a different
              ID to update the owner of the deal.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          typed_custom_fields: Add information to
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4415062486669-Create-a-Deal" target="_blank">custom
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
        if not opportunity_id:
            raise ValueError(f"Expected a non-empty value for `opportunity_id` but received {opportunity_id!r}")
        return await self._patch(
            path_template("/opportunities/{opportunity_id}", opportunity_id=opportunity_id),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "closed_date": closed_date,
                    "name": name,
                    "opportunity_stage_id": opportunity_stage_id,
                    "owner_id": owner_id,
                    "typed_custom_fields": typed_custom_fields,
                },
                opportunity_update_params.OpportunityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpportunityUpdateResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort_by_field: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpportunityListResponse:
        """
        Use the List All Deals endpoint to retrieve every deal that has been created for
        your team's Apollo account.

        This endpoint also requires a master API key. If you attempt to call the
        endpoint without a master key, you will receive a `403` response. Refer to
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

          sort_by_field: Sort the tasks by 1 of the following options: <ul> <li> `amount`: The largest
              deal values first. </li> <li> `is_closed`: Deals that have been closed first.
              </li> <li> `is_won`: Deals that have been won first. </li> </ul>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/opportunities/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "sort_by_field": sort_by_field,
                    },
                    opportunity_list_params.OpportunityListParams,
                ),
            ),
            cast_to=OpportunityListResponse,
        )


class OpportunitiesResourceWithRawResponse:
    def __init__(self, opportunities: OpportunitiesResource) -> None:
        self._opportunities = opportunities

        self.create = to_raw_response_wrapper(
            opportunities.create,
        )
        self.retrieve = to_raw_response_wrapper(
            opportunities.retrieve,
        )
        self.update = to_raw_response_wrapper(
            opportunities.update,
        )
        self.list = to_raw_response_wrapper(
            opportunities.list,
        )


class AsyncOpportunitiesResourceWithRawResponse:
    def __init__(self, opportunities: AsyncOpportunitiesResource) -> None:
        self._opportunities = opportunities

        self.create = async_to_raw_response_wrapper(
            opportunities.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            opportunities.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            opportunities.update,
        )
        self.list = async_to_raw_response_wrapper(
            opportunities.list,
        )


class OpportunitiesResourceWithStreamingResponse:
    def __init__(self, opportunities: OpportunitiesResource) -> None:
        self._opportunities = opportunities

        self.create = to_streamed_response_wrapper(
            opportunities.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            opportunities.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            opportunities.update,
        )
        self.list = to_streamed_response_wrapper(
            opportunities.list,
        )


class AsyncOpportunitiesResourceWithStreamingResponse:
    def __init__(self, opportunities: AsyncOpportunitiesResource) -> None:
        self._opportunities = opportunities

        self.create = async_to_streamed_response_wrapper(
            opportunities.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            opportunities.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            opportunities.update,
        )
        self.list = async_to_streamed_response_wrapper(
            opportunities.list,
        )
