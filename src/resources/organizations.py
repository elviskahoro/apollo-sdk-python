# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import (
    organization_enrich_params,
    organization_search_params,
    organization_bulk_enrich_params,
    organization_job_postings_params,
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
from ..types.organization_enrich_response import OrganizationEnrichResponse
from ..types.organization_search_response import OrganizationSearchResponse
from ..types.organization_retrieve_response import OrganizationRetrieveResponse
from ..types.organization_bulk_enrich_response import OrganizationBulkEnrichResponse
from ..types.organization_job_postings_response import OrganizationJobPostingsResponse

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)

    def bulk_enrich(
        self,
        *,
        domains: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationBulkEnrichResponse:
        """
        Use the Bulk Organization Enrichment endpoint to enrich data for up to 10
        companies with a single API call. To enrich data for only 1 company, use the
        <a href="https://docs.apollo.io/reference/organization-enrichment" target="_blank">Organization
        Enrichment endpoint</a> instead.

        Enriched data potentially includes industry information, revenue, employee
        counts, funding round details, and corporate phone numbers and locations.

        This endpoint's
        <a href="https://docs.apollo.io/reference/rate-limits" target="_blank">rate
        limit</a> is throttled to 50% of the Organization Enrichment endpoint's
        per-minute rate limit, and is 100% of the hourly and daily rate limits for the
        same individual endpoint.

        Args:
          domains: The domain of each company that you want to enrich. Do not include `www.`, the
              `@` symbol, or similar.

              Example: `apollo.io` and `microsoft.com`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/organizations/bulk_enrich",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query={
                    "domains%5B%5D": domains[0] if len(domains) == 1 else domains,
                },
            ),
            cast_to=OrganizationBulkEnrichResponse,
        )

    def enrich(
        self,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationEnrichResponse:
        """Use the Oganization Enrichment endpoint to enrich data for 1 company.

        To enrich
        data for up to 10 companies with a single API call, use the
        <a href="https://docs.apollo.io/reference/bulk-organization-enrichment" target="_blank">Bulk
        Organization Enrichment endpoint</a> instead.

        Enriched data potentially includes industry information, revenue, employee
        counts, funding round details, and corporate phone numbers and locations.

        Args:
          domain: The domain of the company that you want to enrich. Do not include `www.`, the
              `@` symbol, or similar.

              Example: `apollo.io` or `microsoft.com`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organizations/enrich",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"domain": domain}, organization_enrich_params.OrganizationEnrichParams),
            ),
            cast_to=OrganizationEnrichResponse,
        )

    def retrieve(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationRetrieveResponse:
        """
        Use the Get Complete Organization Info endpoint to retrieve complete details
        about an organization in Apollo.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(
                f"Expected a non-empty value for `organization_id` but received {organization_id!r}"
            )
        return self._get(
            path_template("/organizations/{organization_id}", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationRetrieveResponse,
        )

    def job_postings(
        self,
        organization_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationJobPostingsResponse:
        """
        Use the Organization Job Postings endpoint to retrieve the current job postings
        for companies. This can help you identify companies that are growing headcount
        in areas that are strategically important for you.

        Calling this endpoint does consume credits as part of your
        <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
        plan</a>.

        To protect Apollo's performance for all users, this endpoint has a display limit
        of 10,000 records. This limitation does not restrict your access to Apollo's
        database; you just need to access the data in batches.

        Args:
          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            path_template("/organizations/{organization_id}/job_postings", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    organization_job_postings_params.OrganizationJobPostingsParams,
                ),
            ),
            cast_to=OrganizationJobPostingsResponse,
        )

    def search(
        self,
        *,
        currently_using_any_of_technology_uids: SequenceNotStr[str] | Omit = omit,
        latest_funding_amount_range_max: int | Omit = omit,
        latest_funding_amount_range_min: int | Omit = omit,
        latest_funding_date_range_max: Union[str, date] | Omit = omit,
        latest_funding_date_range_min: Union[str, date] | Omit = omit,
        organization_ids: SequenceNotStr[str] | Omit = omit,
        organization_job_locations: SequenceNotStr[str] | Omit = omit,
        organization_job_posted_at_range_max: Union[str, date] | Omit = omit,
        organization_job_posted_at_range_min: Union[str, date] | Omit = omit,
        organization_locations: SequenceNotStr[str] | Omit = omit,
        organization_not_locations: SequenceNotStr[str] | Omit = omit,
        organization_num_employees_ranges: SequenceNotStr[str] | Omit = omit,
        organization_num_jobs_range_max: int | Omit = omit,
        organization_num_jobs_range_min: int | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        q_organization_domains_list: SequenceNotStr[str] | Omit = omit,
        q_organization_job_titles: SequenceNotStr[str] | Omit = omit,
        q_organization_keyword_tags: SequenceNotStr[str] | Omit = omit,
        q_organization_name: str | Omit = omit,
        revenue_range_max: int | Omit = omit,
        revenue_range_min: int | Omit = omit,
        total_funding_range_max: int | Omit = omit,
        total_funding_range_min: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationSearchResponse:
        """
        Use the Organization Search endpoint to find companies in the Apollo database.
        Several filters are available to help narrow your search.

        Calling this endpoint does consume credits as part of your
        <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
        plan</a>.

        To protect Apollo's performance for all users, this endpoint has a display limit
        of 50,000 records (100 records per page, up to 500 pages). Add more filters to
        narrow your search results as much as possible. This limitation does not
        restrict your access to Apollo's database; you just need to access the data in
        batches.

        Args:
          currently_using_any_of_technology_uids: Find organizations based on the technologies they currently use. Apollo supports
              filtering by 1,500+ technologies.

              Apollo calculates technologies data from multiple sources. This data is updated
              regularly. Check out the full list of supported technologies by
              <a href="https://api.apollo.io/v1/auth/supported_technologies_csv" target="_blank">downloading
              this CSV file</a>.

              Use underscores (`_`) to replace spaces and periods for the technologies listed
              in the CSV file.

              Examples: `salesforce`; `google_analytics`; `wordpress_org`

          latest_funding_amount_range_max: The maximium amount the company received with its most recent funding round. Use
              this parameter in combination with `latest_funding_amount_range[min]` to set a
              monetary range for the company's most recent funding round.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Examples: `5000000`; `15000000`

          latest_funding_amount_range_min: The minimum amount the company received with its most recent funding round. Use
              this parameter in combination with `latest_funding_amount_range[max]` to set a
              monetary range for the company's most recent funding round.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Examples: `5000000`; `15000000`

          latest_funding_date_range_max: The latest date when the company received its most recent funding round. Use
              this parameter in combination with `latest_funding_date_range[min]` to set a
              date range for when the company received its most recent funding round.

              Example: `2025-09-25`

          latest_funding_date_range_min: The earliest date when the company received its most recent funding round. Use
              this parameter in combination with `latest_funding_date_range[max]` to set a
              date range for when the company received its most recent funding round.

              Example: `2025-07-25`

          organization_ids: The Apollo IDs for the companies you want to include in your search results.
              Each company in the Apollo database is assigned a unique ID.

              To find IDs, identify the values for `organization_id` when you call this
              endpoint.

              Example: `5e66b6381e05b4008c8331b8`

          organization_job_locations: The locations of the jobs being actively recruited by the company.

              Examples: `atlanta`; `japan`

          organization_job_posted_at_range_max: The latest date when jobs were posted by the company. Use this parameter in
              combination with `organization_job_posted_at_range[min]` to set a date range for
              when jobs posted.

              Example: `2025-09-25`

          organization_job_posted_at_range_min: The earliest date when jobs were posted by the company. Use this parameter in
              combination with `organization_job_posted_at_range[max]` to set a date range for
              when jobs posted.

              Example: `2025-07-25`

          organization_locations: The location of the company headquarters. You can search across cities, US
              states, and countries.

              If a company has several office locations, results are still based on the
              headquarters location. For example, if you search `chicago` but a company's HQ
              location is in `boston`, any Boston-based companies will not appearch in your
              search results, even if they match other parameters..

              To exclude companies based on location, use the `organization_not_locations`
              parameter.

              Examples: `texas`; `tokyo`; `spain`

          organization_not_locations: Exclude companies from search results based on the location of the company
              headquarters. You can use cities, US states, and countries as locations to
              exclude.

              This parameter is useful for ensuring you do not prospect in an undesirable
              territory. For example, if you use `ireland` as a value, no Ireland-based
              companies will appear in your search results.

              Examples: `minnesota`; `ireland`; `seoul`

          organization_num_employees_ranges: The number range of employees working for the company. This enables you to find
              companies based on headcount. You can add multiple ranges to expand your search
              results.

              Each range you add needs to be a string, with the upper and lower numbers of the
              range separated only by a comma.

              Examples: `1,10`; `250,500`; `10000,20000`

          organization_num_jobs_range_max: The maximum number of job postings active at the company. Use this parameter in
              combination with `organization_num_jobs_range[min]` to set a job postings range.

              Examples: `50`; `500`

          organization_num_jobs_range_min: The minimum number of job postings active at the company. Use this parameter in
              combination with `organization_num_jobs_range[max]` to set a job postings range.

              Examples: `50`; `500`

          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          q_organization_domains_list: The domain name for the person's employer. This can be the current employer or a
              previous employer. Do not include `www.`, the `@` symbol, or similar.

              This parameter accepts up to 1,000 domains in a single request.

              Examples: `apollo.io`; `microsoft.com`

          q_organization_job_titles: The job titles that are listed in active job postings at the company.

              Examples: `sales manager`; `research analyst`

          q_organization_keyword_tags: Filter search results based on keywords associated with companies. For example,
              you can enter `mining` as a value to return only companies that have an
              association with the mining industry.

              Examples: `mining`; `sales strategy`; `consulting`

          q_organization_name: Filter search results to include a specific company name.

              If the value you enter for this parameter does not match with a company's name,
              the company will not appear in search results, even if it matches other
              parameters. Partial matches are accepted. For example, if you filter by the
              value `marketing`, a company called `NY Marketing Unlimited` would still be
              eligible as a search result, but `NY Market Analysis` would not be eligible.

              Example: `apollo` or `mining`

          revenue_range_max: Search for organizations based on their revenue.

              Use this parameter to set the upper range of organization revenue. Use the
              `revenue_range[min]` parameter to set the lower range of revenue.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Example: `50000000`

          revenue_range_min: Search for organizations based on their revenue.

              Use this parameter to set the lower range of organization revenue. Use the
              `revenue_range[max]` parameter to set the upper range of revenue.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Example: `300000`

          total_funding_range_max: The maximum amount the company received during all of its funding rounds
              combined. Use this parameter in combination with `total_funding_range[min]` to
              set a monetary range for all of the company's funding rounds.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Examples: `50000000`; `350000000`

          total_funding_range_min: The minimum amount the company received during all of its funding rounds
              combined. Use this parameter in combination with `total_funding_range[max]` to
              set a monetary range for all of the company's funding rounds.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Examples: `50000000`; `350000000`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/mixed_companies/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currently_using_any_of_technology_uids": currently_using_any_of_technology_uids,
                        "latest_funding_amount_range_max": latest_funding_amount_range_max,
                        "latest_funding_amount_range_min": latest_funding_amount_range_min,
                        "latest_funding_date_range_max": latest_funding_date_range_max,
                        "latest_funding_date_range_min": latest_funding_date_range_min,
                        "organization_ids": organization_ids,
                        "organization_job_locations": organization_job_locations,
                        "organization_job_posted_at_range_max": organization_job_posted_at_range_max,
                        "organization_job_posted_at_range_min": organization_job_posted_at_range_min,
                        "organization_locations": organization_locations,
                        "organization_not_locations": organization_not_locations,
                        "organization_num_employees_ranges": organization_num_employees_ranges,
                        "organization_num_jobs_range_max": organization_num_jobs_range_max,
                        "organization_num_jobs_range_min": organization_num_jobs_range_min,
                        "page": page,
                        "per_page": per_page,
                        "q_organization_domains_list": q_organization_domains_list,
                        "q_organization_job_titles": q_organization_job_titles,
                        "q_organization_keyword_tags": q_organization_keyword_tags,
                        "q_organization_name": q_organization_name,
                        "revenue_range_max": revenue_range_max,
                        "revenue_range_min": revenue_range_min,
                        "total_funding_range_max": total_funding_range_max,
                        "total_funding_range_min": total_funding_range_min,
                    },
                    organization_search_params.OrganizationSearchParams,
                ),
            ),
            cast_to=OrganizationSearchResponse,
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def bulk_enrich(
        self,
        *,
        domains: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationBulkEnrichResponse:
        """
        Use the Bulk Organization Enrichment endpoint to enrich data for up to 10
        companies with a single API call. To enrich data for only 1 company, use the
        <a href="https://docs.apollo.io/reference/organization-enrichment" target="_blank">Organization
        Enrichment endpoint</a> instead.

        Enriched data potentially includes industry information, revenue, employee
        counts, funding round details, and corporate phone numbers and locations.

        This endpoint's
        <a href="https://docs.apollo.io/reference/rate-limits" target="_blank">rate
        limit</a> is throttled to 50% of the Organization Enrichment endpoint's
        per-minute rate limit, and is 100% of the hourly and daily rate limits for the
        same individual endpoint.

        Args:
          domains: The domain of each company that you want to enrich. Do not include `www.`, the
              `@` symbol, or similar.

              Example: `apollo.io` and `microsoft.com`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/organizations/bulk_enrich",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query={
                    "domains%5B%5D": domains[0] if len(domains) == 1 else domains,
                },
            ),
            cast_to=OrganizationBulkEnrichResponse,
        )

    async def enrich(
        self,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationEnrichResponse:
        """Use the Oganization Enrichment endpoint to enrich data for 1 company.

        To enrich
        data for up to 10 companies with a single API call, use the
        <a href="https://docs.apollo.io/reference/bulk-organization-enrichment" target="_blank">Bulk
        Organization Enrichment endpoint</a> instead.

        Enriched data potentially includes industry information, revenue, employee
        counts, funding round details, and corporate phone numbers and locations.

        Args:
          domain: The domain of the company that you want to enrich. Do not include `www.`, the
              `@` symbol, or similar.

              Example: `apollo.io` or `microsoft.com`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organizations/enrich",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"domain": domain}, organization_enrich_params.OrganizationEnrichParams
                ),
            ),
            cast_to=OrganizationEnrichResponse,
        )

    async def retrieve(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationRetrieveResponse:
        """
        Use the Get Complete Organization Info endpoint to retrieve complete details
        about an organization in Apollo.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(
                f"Expected a non-empty value for `organization_id` but received {organization_id!r}"
            )
        return await self._get(
            path_template("/organizations/{organization_id}", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationRetrieveResponse,
        )

    async def job_postings(
        self,
        organization_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationJobPostingsResponse:
        """
        Use the Organization Job Postings endpoint to retrieve the current job postings
        for companies. This can help you identify companies that are growing headcount
        in areas that are strategically important for you.

        Calling this endpoint does consume credits as part of your
        <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
        plan</a>.

        To protect Apollo's performance for all users, this endpoint has a display limit
        of 10,000 records. This limitation does not restrict your access to Apollo's
        database; you just need to access the data in batches.

        Args:
          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            path_template("/organizations/{organization_id}/job_postings", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    organization_job_postings_params.OrganizationJobPostingsParams,
                ),
            ),
            cast_to=OrganizationJobPostingsResponse,
        )

    async def search(
        self,
        *,
        currently_using_any_of_technology_uids: SequenceNotStr[str] | Omit = omit,
        latest_funding_amount_range_max: int | Omit = omit,
        latest_funding_amount_range_min: int | Omit = omit,
        latest_funding_date_range_max: Union[str, date] | Omit = omit,
        latest_funding_date_range_min: Union[str, date] | Omit = omit,
        organization_ids: SequenceNotStr[str] | Omit = omit,
        organization_job_locations: SequenceNotStr[str] | Omit = omit,
        organization_job_posted_at_range_max: Union[str, date] | Omit = omit,
        organization_job_posted_at_range_min: Union[str, date] | Omit = omit,
        organization_locations: SequenceNotStr[str] | Omit = omit,
        organization_not_locations: SequenceNotStr[str] | Omit = omit,
        organization_num_employees_ranges: SequenceNotStr[str] | Omit = omit,
        organization_num_jobs_range_max: int | Omit = omit,
        organization_num_jobs_range_min: int | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        q_organization_domains_list: SequenceNotStr[str] | Omit = omit,
        q_organization_job_titles: SequenceNotStr[str] | Omit = omit,
        q_organization_keyword_tags: SequenceNotStr[str] | Omit = omit,
        q_organization_name: str | Omit = omit,
        revenue_range_max: int | Omit = omit,
        revenue_range_min: int | Omit = omit,
        total_funding_range_max: int | Omit = omit,
        total_funding_range_min: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationSearchResponse:
        """
        Use the Organization Search endpoint to find companies in the Apollo database.
        Several filters are available to help narrow your search.

        Calling this endpoint does consume credits as part of your
        <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
        plan</a>.

        To protect Apollo's performance for all users, this endpoint has a display limit
        of 50,000 records (100 records per page, up to 500 pages). Add more filters to
        narrow your search results as much as possible. This limitation does not
        restrict your access to Apollo's database; you just need to access the data in
        batches.

        Args:
          currently_using_any_of_technology_uids: Find organizations based on the technologies they currently use. Apollo supports
              filtering by 1,500+ technologies.

              Apollo calculates technologies data from multiple sources. This data is updated
              regularly. Check out the full list of supported technologies by
              <a href="https://api.apollo.io/v1/auth/supported_technologies_csv" target="_blank">downloading
              this CSV file</a>.

              Use underscores (`_`) to replace spaces and periods for the technologies listed
              in the CSV file.

              Examples: `salesforce`; `google_analytics`; `wordpress_org`

          latest_funding_amount_range_max: The maximium amount the company received with its most recent funding round. Use
              this parameter in combination with `latest_funding_amount_range[min]` to set a
              monetary range for the company's most recent funding round.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Examples: `5000000`; `15000000`

          latest_funding_amount_range_min: The minimum amount the company received with its most recent funding round. Use
              this parameter in combination with `latest_funding_amount_range[max]` to set a
              monetary range for the company's most recent funding round.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Examples: `5000000`; `15000000`

          latest_funding_date_range_max: The latest date when the company received its most recent funding round. Use
              this parameter in combination with `latest_funding_date_range[min]` to set a
              date range for when the company received its most recent funding round.

              Example: `2025-09-25`

          latest_funding_date_range_min: The earliest date when the company received its most recent funding round. Use
              this parameter in combination with `latest_funding_date_range[max]` to set a
              date range for when the company received its most recent funding round.

              Example: `2025-07-25`

          organization_ids: The Apollo IDs for the companies you want to include in your search results.
              Each company in the Apollo database is assigned a unique ID.

              To find IDs, identify the values for `organization_id` when you call this
              endpoint.

              Example: `5e66b6381e05b4008c8331b8`

          organization_job_locations: The locations of the jobs being actively recruited by the company.

              Examples: `atlanta`; `japan`

          organization_job_posted_at_range_max: The latest date when jobs were posted by the company. Use this parameter in
              combination with `organization_job_posted_at_range[min]` to set a date range for
              when jobs posted.

              Example: `2025-09-25`

          organization_job_posted_at_range_min: The earliest date when jobs were posted by the company. Use this parameter in
              combination with `organization_job_posted_at_range[max]` to set a date range for
              when jobs posted.

              Example: `2025-07-25`

          organization_locations: The location of the company headquarters. You can search across cities, US
              states, and countries.

              If a company has several office locations, results are still based on the
              headquarters location. For example, if you search `chicago` but a company's HQ
              location is in `boston`, any Boston-based companies will not appearch in your
              search results, even if they match other parameters..

              To exclude companies based on location, use the `organization_not_locations`
              parameter.

              Examples: `texas`; `tokyo`; `spain`

          organization_not_locations: Exclude companies from search results based on the location of the company
              headquarters. You can use cities, US states, and countries as locations to
              exclude.

              This parameter is useful for ensuring you do not prospect in an undesirable
              territory. For example, if you use `ireland` as a value, no Ireland-based
              companies will appear in your search results.

              Examples: `minnesota`; `ireland`; `seoul`

          organization_num_employees_ranges: The number range of employees working for the company. This enables you to find
              companies based on headcount. You can add multiple ranges to expand your search
              results.

              Each range you add needs to be a string, with the upper and lower numbers of the
              range separated only by a comma.

              Examples: `1,10`; `250,500`; `10000,20000`

          organization_num_jobs_range_max: The maximum number of job postings active at the company. Use this parameter in
              combination with `organization_num_jobs_range[min]` to set a job postings range.

              Examples: `50`; `500`

          organization_num_jobs_range_min: The minimum number of job postings active at the company. Use this parameter in
              combination with `organization_num_jobs_range[max]` to set a job postings range.

              Examples: `50`; `500`

          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          q_organization_domains_list: The domain name for the person's employer. This can be the current employer or a
              previous employer. Do not include `www.`, the `@` symbol, or similar.

              This parameter accepts up to 1,000 domains in a single request.

              Examples: `apollo.io`; `microsoft.com`

          q_organization_job_titles: The job titles that are listed in active job postings at the company.

              Examples: `sales manager`; `research analyst`

          q_organization_keyword_tags: Filter search results based on keywords associated with companies. For example,
              you can enter `mining` as a value to return only companies that have an
              association with the mining industry.

              Examples: `mining`; `sales strategy`; `consulting`

          q_organization_name: Filter search results to include a specific company name.

              If the value you enter for this parameter does not match with a company's name,
              the company will not appear in search results, even if it matches other
              parameters. Partial matches are accepted. For example, if you filter by the
              value `marketing`, a company called `NY Marketing Unlimited` would still be
              eligible as a search result, but `NY Market Analysis` would not be eligible.

              Example: `apollo` or `mining`

          revenue_range_max: Search for organizations based on their revenue.

              Use this parameter to set the upper range of organization revenue. Use the
              `revenue_range[min]` parameter to set the lower range of revenue.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Example: `50000000`

          revenue_range_min: Search for organizations based on their revenue.

              Use this parameter to set the lower range of organization revenue. Use the
              `revenue_range[max]` parameter to set the upper range of revenue.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Example: `300000`

          total_funding_range_max: The maximum amount the company received during all of its funding rounds
              combined. Use this parameter in combination with `total_funding_range[min]` to
              set a monetary range for all of the company's funding rounds.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Examples: `50000000`; `350000000`

          total_funding_range_min: The minimum amount the company received during all of its funding rounds
              combined. Use this parameter in combination with `total_funding_range[max]` to
              set a monetary range for all of the company's funding rounds.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Examples: `50000000`; `350000000`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/mixed_companies/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "currently_using_any_of_technology_uids": currently_using_any_of_technology_uids,
                        "latest_funding_amount_range_max": latest_funding_amount_range_max,
                        "latest_funding_amount_range_min": latest_funding_amount_range_min,
                        "latest_funding_date_range_max": latest_funding_date_range_max,
                        "latest_funding_date_range_min": latest_funding_date_range_min,
                        "organization_ids": organization_ids,
                        "organization_job_locations": organization_job_locations,
                        "organization_job_posted_at_range_max": organization_job_posted_at_range_max,
                        "organization_job_posted_at_range_min": organization_job_posted_at_range_min,
                        "organization_locations": organization_locations,
                        "organization_not_locations": organization_not_locations,
                        "organization_num_employees_ranges": organization_num_employees_ranges,
                        "organization_num_jobs_range_max": organization_num_jobs_range_max,
                        "organization_num_jobs_range_min": organization_num_jobs_range_min,
                        "page": page,
                        "per_page": per_page,
                        "q_organization_domains_list": q_organization_domains_list,
                        "q_organization_job_titles": q_organization_job_titles,
                        "q_organization_keyword_tags": q_organization_keyword_tags,
                        "q_organization_name": q_organization_name,
                        "revenue_range_max": revenue_range_max,
                        "revenue_range_min": revenue_range_min,
                        "total_funding_range_max": total_funding_range_max,
                        "total_funding_range_min": total_funding_range_min,
                    },
                    organization_search_params.OrganizationSearchParams,
                ),
            ),
            cast_to=OrganizationSearchResponse,
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.bulk_enrich = to_raw_response_wrapper(
            organizations.bulk_enrich,
        )
        self.enrich = to_raw_response_wrapper(
            organizations.enrich,
        )
        self.retrieve = to_raw_response_wrapper(
            organizations.retrieve,
        )
        self.job_postings = to_raw_response_wrapper(
            organizations.job_postings,
        )
        self.search = to_raw_response_wrapper(
            organizations.search,
        )


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.bulk_enrich = async_to_raw_response_wrapper(
            organizations.bulk_enrich,
        )
        self.enrich = async_to_raw_response_wrapper(
            organizations.enrich,
        )
        self.retrieve = async_to_raw_response_wrapper(
            organizations.retrieve,
        )
        self.job_postings = async_to_raw_response_wrapper(
            organizations.job_postings,
        )
        self.search = async_to_raw_response_wrapper(
            organizations.search,
        )


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.bulk_enrich = to_streamed_response_wrapper(
            organizations.bulk_enrich,
        )
        self.enrich = to_streamed_response_wrapper(
            organizations.enrich,
        )
        self.retrieve = to_streamed_response_wrapper(
            organizations.retrieve,
        )
        self.job_postings = to_streamed_response_wrapper(
            organizations.job_postings,
        )
        self.search = to_streamed_response_wrapper(
            organizations.search,
        )


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.bulk_enrich = async_to_streamed_response_wrapper(
            organizations.bulk_enrich,
        )
        self.enrich = async_to_streamed_response_wrapper(
            organizations.enrich,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            organizations.retrieve,
        )
        self.job_postings = async_to_streamed_response_wrapper(
            organizations.job_postings,
        )
        self.search = async_to_streamed_response_wrapper(
            organizations.search,
        )
