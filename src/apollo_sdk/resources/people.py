# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date

import httpx

from ..types import person_search_params, person_enrichment_params, person_bulk_enrichment_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.person_search_response import PersonSearchResponse
from ..types.person_enrichment_response import PersonEnrichmentResponse
from ..types.person_bulk_enrichment_response import PersonBulkEnrichmentResponse

__all__ = ["PeopleResource", "AsyncPeopleResource"]


class PeopleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return PeopleResourceWithStreamingResponse(self)

    def bulk_enrichment(
        self,
        *,
        details: Iterable[person_bulk_enrichment_params.Detail],
        reveal_personal_emails: bool | Omit = omit,
        reveal_phone_number: bool | Omit = omit,
        run_waterfall_email: bool | Omit = omit,
        run_waterfall_phone: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonBulkEnrichmentResponse:
        """
        Use the Bulk People Enrichment endpoint to enrich data for up to 10 people with
        a single API call. To enrich data for only 1 person, use the
        <a href="https://docs.apollo.io/reference/people-enrichment" target="_blank">People
        Enrichment endpoint</a> instead.

        Apollo relies on the information you pass via the endpoint's parameters to
        identify the correct people to enrich. When you provide more information, Apollo
        is more likely to find matches within its database. If you only provide general
        information, such as a name without a domain or email address, you might receive
        a `200` response, but the response will indicate that no records have been
        enriched. The details for each person should be passed as an object with the
        `details[]` array.

        By default, this endpoint does not return personal emails or phone numbers. Use
        the `reveal_personal_emails` and `reveal_phone_number` parameters to retrieve
        emails and phone numbers. If you set either of these parameters to `true`,
        Apollo will attempt to provide emails or phone numbers for all matches.

        You can use also use the `run_waterfall_email` and `run_waterfall_phone`
        parameters to run waterfall enrichment via this endpoint.
        [Waterfall enrichment](https://knowledge.apollo.io/hc/en-us/articles/34071089002509-Waterfall-Enrichment-Overview)
        gives you broader data coverage by checking connected third-party data sources
        for contact emails and phone numbers. When you call this endpoint and include at
        least one waterfall parameter, Apollo returns an immediate synchronous response
        with demographic and firmographic data, along with a waterfall enrichment
        request status. Apollo delivers enriched emails and/or phone numbers
        asynchronously to a configured webhook.

        Using this endpoint will consume credits based on your account's pricing plan.
        If you run waterfall enrichment parameters, your
        [credit usage](https://knowledge.apollo.io/hc/en-us/articles/34071089002509-Waterfall-Enrichment-Overview#does-waterfall-enrichment-require-credits)
        depends on the type of data you request (emails and/or phone numbers) and which
        data source returns enriched data. To view a summary of Apollo's pricing, visit
        the <a href="https://www.apollo.io/pricing" target="_blank"> public pricing page
        ↗</a> For detailed information regarding API credit usage, see the
        <a href="https://app.apollo.io/#/settings/credits/about" target="_blank"> API
        enrichment ↗</a> section on the _About Credits_ page (login required).

        This endpoint's
        <a href="https://docs.apollo.io/reference/rate-limits" target="_blank">rate
        limit</a> is throttled to 50% of the People Enrichment endpoint's per-minute
        rate limit, and is 100% of the hourly and daily rate limits for the same
        individual endpoint.

        Args:
          details: Provide info for each person you want to enrich as an object within this array.
              Add up to 10 people.

          reveal_personal_emails: Set to `true` if you want to enrich all matched people with personal emails.
              This potentially consumes credits as part of your
              <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
              plan</a>. The default value is `false`.

              If a person resides in a
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4409141087757" target="_blank">GDPR</a>-compliant
              region, Apollo will not reveal their personal email.

          reveal_phone_number: Set to `true` if you want to enrich the data of all matched people with all
              available phone numbers, including mobile phone numbers. This potentially
              consumes credits as part of your
              <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
              plan</a>. The default value is `false`.

              If this parameter is set to `true`, you must enter a webhook URL for the
              `webhook_url` parameter. Apollo will asynchronously verify phone numbers for
              you, then send a JSON response that includes only details about the phone
              numbers to the webhook URL you provide. It can take several minutes for the
              phone numbers to be delivered.

          run_waterfall_email: Set to true to enable email waterfall enrichment

          run_waterfall_phone: Set to true to enable phone waterfall enrichment

          webhook_url: If you set the `reveal_phone_number` parameter to `true`, this parameter becomes
              mandatory. Otherwise, do not use this parameter.

              Enter the webhook URL that specifies where Apollo should send a JSON response
              that includes the phone number you requested. Apollo suggests testing this flow
              to ensure you receive the separate response with the phone number.

              If phone numbers are not revealed delivered to the webhook URL, try applying
              UTF-8 encoding to the webhook URL.

              Example: `https://webhook.site/cc4cf44e-e047-4774-8dac-473d28474e40`;
              `https%3A%2F%2Fwebhook.site%2Fcc4cf44e-e047-4774-8dac-473d28474e40`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/people/bulk_match",
            body=maybe_transform({"details": details}, person_bulk_enrichment_params.PersonBulkEnrichmentParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "reveal_personal_emails": reveal_personal_emails,
                        "reveal_phone_number": reveal_phone_number,
                        "run_waterfall_email": run_waterfall_email,
                        "run_waterfall_phone": run_waterfall_phone,
                        "webhook_url": webhook_url,
                    },
                    person_bulk_enrichment_params.PersonBulkEnrichmentParams,
                ),
            ),
            cast_to=PersonBulkEnrichmentResponse,
        )

    def enrichment(
        self,
        *,
        id: str | Omit = omit,
        domain: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        hashed_email: str | Omit = omit,
        last_name: str | Omit = omit,
        linkedin_url: str | Omit = omit,
        name: str | Omit = omit,
        organization_name: str | Omit = omit,
        reveal_personal_emails: bool | Omit = omit,
        reveal_phone_number: bool | Omit = omit,
        run_waterfall_email: bool | Omit = omit,
        run_waterfall_phone: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonEnrichmentResponse:
        """Use the People Enrichment endpoint to enrich data for 1 person.

        To enrich data
        for up to 10 people with a single API call, use the
        <a href="https://docs.apollo.io/reference/bulk-people-enrichment" target="_blank">Bulk
        People Enrichment endpoint</a> instead.

        Apollo relies on the information you pass via the endpoint's parameters to
        identify the correct person to enrich. If you provide more information about a
        person, Apollo is more likely to find a match within its database. If you only
        provide general information, such as a name without a domain or email address,
        you might receive a 200 response, but the response will indicate that no records
        have been enriched.

        By default, this endpoint does not return personal emails or phone numbers. Use
        the `reveal_personal_emails` and `reveal_phone_number` parameters to retrieve
        emails and phone numbers.

        You can use also use the `run_waterfall_email` and `run_waterfall_phone`
        parameters to run waterfall enrichment via this endpoint.
        [Waterfall enrichment](https://knowledge.apollo.io/hc/en-us/articles/34071089002509-Waterfall-Enrichment-Overview)
        gives you broader data coverage by checking connected third-party data sources
        for contact emails and phone numbers. When you call this endpoint and include at
        least one waterfall parameter, Apollo returns an immediate synchronous response
        with demographic and firmographic data, along with a waterfall enrichment
        request status. Apollo delivers enriched emails and/or phone numbers
        asynchronously to a configured webhook.

        Using this endpoint will consume credits based on your account's pricing plan.
        If you run waterfall enrichment parameters, your
        [credit usage](https://knowledge.apollo.io/hc/en-us/articles/34071089002509-Waterfall-Enrichment-Overview#does-waterfall-enrichment-require-credits)
        depends on the type of data you request (emails and/or phone numbers) and which
        data source returns enriched data. To view a summary of Apollo's pricing, visit
        the <a href="https://www.apollo.io/pricing" target="_blank"> public pricing page
        ↗</a> For detailed information regarding API credit usage, see the
        <a href="https://app.apollo.io/#/settings/credits/about" target="_blank"> API
        enrichment ↗</a> section on the _About Credits_ page (login required).

        Args:
          id: The Apollo ID for the person. Each person in the Apollo database is assigned a
              unique ID.

              To find IDs, call the
              <a href="https://docs.apollo.io/reference/people-api-search" target="_blank">People
              API Search endpoint</a> and identify the values for `person_id`.

              Example: `587cf802f65125cad923a266`

          domain: The domain name for the person's employer. This can be the current employer or a
              previous employer. Do not include `www.`, the `@` symbol, or similar.

              Example: `apollo.io` or `microsoft.com`

          email: The email address of the person.

              Example: `example@email.com`

          first_name: The first name of the person. This is typically used in combination with the
              `last_name` parameter.

              Example: `tim`

          hashed_email: The hashed email of the person. The email should adhere to either the MD5 or
              SHA-256 hash format.

              Example: `8d935115b9ff4489f2d1f9249503cadf` (MD5) or
              `97817c0c49994eb500ad0a5e7e2d8aed51977b26424d508f66e4e8887746a152` (SHA-256)

          last_name: The last name of the person. This is typically used in combination with the
              `first_name` parameter.

              Example: `zheng`

          linkedin_url: The URL for the person's LinkedIn profile.

              Example: `http://www.linkedin.com/in/tim-zheng-677ba010`

          name: The full name of the person. This will typically be a first name and last name
              separated by a space. If you use this parameter, you do not need to use the
              `first_name` and `last_name` parameters.

              Example: `tim zheng`

          organization_name: The name of the person's employer. This can be the current employer or a
              previous employer.

              Example: `apollo`

          reveal_personal_emails: Set to `true` if you want to enrich the person's data with personal emails. This
              potentially consumes credits as part of your
              <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
              plan</a>. The default value is `false`.

              If a person resides in a
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4409141087757" target="_blank">GDPR</a>-compliant
              region, Apollo will not reveal their personal email.

          reveal_phone_number: Set to `true` if you want to enrich the person's data with all available phone
              numbers, including mobile phone numbers. This potentially consumes credits as
              part of your
              <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
              plan</a>. The default value is `false`.

              If this parameter is set to `true`, you must enter a webhook URL for the
              `webhook_url` parameter. Apollo will asynchronously verify phone numbers for
              you, then send a JSON response that includes only details about the person's
              phone numbers to the webhook URL you provide. It can take several minutes for
              the phone numbers to be delivered.

          run_waterfall_email: Set to true to enable email waterfall enrichment

          run_waterfall_phone: Set to true to enable phone waterfall enrichment

          webhook_url: If you set the `reveal_phone_number` parameter to `true`, this parameter becomes
              mandatory. Otherwise, do not use this parameter.

              Enter the webhook URL that specifies where Apollo should send a JSON response
              that includes the phone number you requested. Apollo suggests testing this flow
              to ensure you receive the separate response with the phone number.

              If phone numbers are not revealed delivered to the webhook URL, try applying
              UTF-8 encoding to the webhook URL.

              Example: `https://webhook.site/cc4cf44e-e047-4774-8dac-473d28474e40`;
              `https%3A%2F%2Fwebhook.site%2Fcc4cf44e-e047-4774-8dac-473d28474e40`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/people/match",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "domain": domain,
                        "email": email,
                        "first_name": first_name,
                        "hashed_email": hashed_email,
                        "last_name": last_name,
                        "linkedin_url": linkedin_url,
                        "name": name,
                        "organization_name": organization_name,
                        "reveal_personal_emails": reveal_personal_emails,
                        "reveal_phone_number": reveal_phone_number,
                        "run_waterfall_email": run_waterfall_email,
                        "run_waterfall_phone": run_waterfall_phone,
                        "webhook_url": webhook_url,
                    },
                    person_enrichment_params.PersonEnrichmentParams,
                ),
            ),
            cast_to=PersonEnrichmentResponse,
        )

    def search(
        self,
        *,
        contact_email_status: SequenceNotStr[str] | Omit = omit,
        currently_not_using_any_of_technology_uids: SequenceNotStr[str] | Omit = omit,
        currently_using_all_of_technology_uids: SequenceNotStr[str] | Omit = omit,
        currently_using_any_of_technology_uids: SequenceNotStr[str] | Omit = omit,
        include_similar_titles: bool | Omit = omit,
        organization_ids: SequenceNotStr[str] | Omit = omit,
        organization_job_locations: SequenceNotStr[str] | Omit = omit,
        organization_job_posted_at_range_max: Union[str, date] | Omit = omit,
        organization_job_posted_at_range_min: Union[str, date] | Omit = omit,
        organization_locations: SequenceNotStr[str] | Omit = omit,
        organization_num_employees_ranges: SequenceNotStr[str] | Omit = omit,
        organization_num_jobs_range_max: int | Omit = omit,
        organization_num_jobs_range_min: int | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        person_locations: SequenceNotStr[str] | Omit = omit,
        person_seniorities: SequenceNotStr[str] | Omit = omit,
        person_titles: SequenceNotStr[str] | Omit = omit,
        q_keywords: str | Omit = omit,
        q_organization_domains_list: SequenceNotStr[str] | Omit = omit,
        q_organization_job_titles: SequenceNotStr[str] | Omit = omit,
        revenue_range_max: int | Omit = omit,
        revenue_range_min: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonSearchResponse:
        """Use the People API Search endpoint to find net new people in the Apollo
        database.

        Several filters are available to help narrow your search.

        This endpoint is optimized for API usage and does not consume credits. This
        endpoint is primarily designed for prospecting net new people.

        This endpoint does not return email addresses or phone numbers. Use the
        <a href="https://docs.apollo.io/reference/people-enrichment" target="_blank">People
        Enrichment</a> or
        <a href="https://docs.apollo.io/reference/bulk-people-enrichment" target="_blank">Bulk
        People Enrichment</a> endpoints to enrich data.

        This endpoint requires a master API key. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        To protect Apollo's performance for all users, this endpoint has a display limit
        of 50,000 records (100 records per page, up to 500 pages). Add more filters to
        narrow your search results as much as possible. This limitation does not
        restrict your access to Apollo's database; you just need to access the data in
        batches.

        Args:
          contact_email_status: The email statuses for the people you want to find. You can add multiple
              statuses to expand your search.

              The statuses you can search include: <ul> <li> <code>verified</code> </li> <li>
              <code>unverified</code> </li> <li> <code>likely to engage</code> </li> <li>
              <code>unavailable</code> </li> </ul>

          currently_not_using_any_of_technology_uids: Exclude people from your search based on any of the technologies their current
              employer uses. Apollo supports filtering by 1,500+ technologies.

              Apollo calculates technologies data from multiple sources. This data is updated
              regularly. Check out the full list of supported technologies by
              <a href="https://api.apollo.io/v1/auth/supported_technologies_csv" target="_blank">downloading
              this CSV file</a>.

              Use underscores (`_`) to replace spaces and periods for the technologies listed
              in the CSV file.

              Examples: `salesforce`; `google_analytics`; `wordpress_org`

          currently_using_all_of_technology_uids: Find people based on all of the technologies their current employer uses. Apollo
              supports filtering by 1,500+ technologies.

              Apollo calculates technologies data from multiple sources. This data is updated
              regularly. Check out the full list of supported technologies by
              <a href="https://api.apollo.io/v1/auth/supported_technologies_csv" target="_blank">downloading
              this CSV file</a>.

              Use underscores (`_`) to replace spaces and periods for the technologies listed
              in the CSV file.

              Examples: `salesforce`; `google_analytics`; `wordpress_org`

          currently_using_any_of_technology_uids: Find people based on any of the technologies their current employer uses. Apollo
              supports filtering by 1,500+ technologies.

              Apollo calculates technologies data from multiple sources. This data is updated
              regularly. Check out the full list of supported technologies by
              <a href="https://api.apollo.io/v1/auth/supported_technologies_csv" target="_blank">downloading
              this CSV file</a>.

              Use underscores (`_`) to replace spaces and periods for the technologies listed
              in the CSV file.

              Examples: `salesforce`; `google_analytics`; `wordpress_org`

          include_similar_titles: This parameter determines whether people with job titles similar to the titles
              you define in the `person_titles[]` parameter are returned in the response.

              Set this parameter to `false` when using `person_titles[]` to return only strict
              matches for job titles.

          organization_ids: The Apollo IDs for the companies (employers) you want to include in your search
              results. Each company in the Apollo database is assigned a unique ID.

              To find IDs, call the
              <a href="https://docs.apollo.io/reference/organization-search" target="_blank">Organization
              Search endpoint</a> and identify the values for `organization_id`.

              Example: `5e66b6381e05b4008c8331b8`

          organization_job_locations: The locations of the jobs being actively recruited by the person's employer.

              Examples: `atlanta`; `japan`

          organization_job_posted_at_range_max: The latest date when jobs were posted by the person's current employer. Use this
              parameter in combination with `organization_job_posted_at_range[min]` to set a
              date range for when jobs posted.

              Example: `2025-09-25`

          organization_job_posted_at_range_min: The earliest date when jobs were posted by the person's current employer. Use
              this parameter in combination with `organization_job_posted_at_range[max]` to
              set a date range for when jobs posted.

              Example: `2025-07-25`

          organization_locations: The location of the company headquarters for a person's current employer. You
              can search across cities, US states, and countries.

              If a company has several office locations, results are still based on the
              headquarters location. For example, if you search `chicago` but a company's HQ
              location is in `boston`, people that work for the Boston-based company will not
              appear in your results, even if they match other \\pparameters.

              To find people based on their personal location, use the `person_locations`
              parameter.

              Examples: `texas`; `tokyo`; `spain`

          organization_num_employees_ranges: The number range of employees working for the person's current company. This
              enables you to find people based on the headcount of their employer. You can add
              multiple ranges to expand your search results.

              Each range you add needs to be a string, with the upper and lower numbers of the
              range separated only by a comma.

              Examples: `1,10`; `250,500`; `10000,20000`

          organization_num_jobs_range_max: The maximum number of job postings active at the person's current empployer. Use
              this parameter in combination with `organization_num_jobs_range[min]` to set a
              job postings range.

              Examples: `50`; `500`

          organization_num_jobs_range_min: The minimum number of job postings active at the person's current empployer. Use
              this parameter in combination with `organization_num_jobs_range[max]` to set a
              job postings range.

              Examples: `50`; `500`

          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          person_locations: The location where people live. You can search across cities, US states, and
              countries.

              To find people based on the headquarters locations of their current employer,
              use the `organization_locations` parameter.

              Examples: `california`; `ireland`; `chicago`

          person_seniorities: The job seniority that people hold within their current employer. This enables
              you to find people that currently hold positions at certain reporting levels,
              such as Director level or senior IC level.

              For a person to be included in search results, they only need to match 1 of the
              seniorities you add. Adding more seniorities expands your search results.

              Searches only return results based on their current job title, so searching for
              Director-level employees only returns people that currently hold a
              Director-level title. If someone was previously a Director, but is currently a
              VP, they would not be included in your search results.

              Use this parameter in combination with the `person_titles[]` parameter to find
              people based on specific job functions and seniority levels.

              The following options can be used for this parameter:

              <ul><li><code>owner</code></li><li><code>founder</code></li><li><code>c_suite</code></li><li><code>partner</code></li><li><code>vp</code></li><li><code>head</code></li><li><code>director</code></li><li><code>manager</code></li><li><code>senior</code></li><li><code>entry</code></li><li><code>intern</code></li></ul>

          person_titles: Job titles held by the people you want to find. For a person to be included in
              search results, they only need to match 1 of the job titles you add. Adding more
              job titles expands your search results.

              Results also include job titles with the same terms, even if they are not exact
              matches. For example, searching for `marketing manager` might return people with
              the job title `content marketing manager`.

              Use this parameter in combination with the `person_seniorities[]` parameter to
              find people based on specific job functions and seniority levels.

              Examples: `sales development representative`; `marketing manager`;
              `research analyst`

          q_keywords: A string of words over which we want to filter the results.

          q_organization_domains_list: The domain name for the person's employer. This can be the current employer or a
              previous employer. Do not include `www.`, the `@` symbol, or similar.

              This parameter accepts up to 1,000 domains in a single request.

              Examples: `apollo.io`; `microsoft.com`

          q_organization_job_titles: The job titles that are listed in active job postings at the person's current
              employer.

              Examples: `sales manager`; `research analyst`

          revenue_range_max: The maximum revenue the person's current employer generates. Use this parameter
              in combination with `revenue_range[min]` to set a revenue range.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Examples: `500000`; `1500000`

          revenue_range_min: The minimum revenue the person's current employer generates. Use this parameter
              in combination with `revenue_range[max]` to set a revenue range.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Examples: `500000`; `1500000`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/mixed_people/api_search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "contact_email_status": contact_email_status,
                        "currently_not_using_any_of_technology_uids": currently_not_using_any_of_technology_uids,
                        "currently_using_all_of_technology_uids": currently_using_all_of_technology_uids,
                        "currently_using_any_of_technology_uids": currently_using_any_of_technology_uids,
                        "include_similar_titles": include_similar_titles,
                        "organization_ids": organization_ids,
                        "organization_job_locations": organization_job_locations,
                        "organization_job_posted_at_range_max": organization_job_posted_at_range_max,
                        "organization_job_posted_at_range_min": organization_job_posted_at_range_min,
                        "organization_locations": organization_locations,
                        "organization_num_employees_ranges": organization_num_employees_ranges,
                        "organization_num_jobs_range_max": organization_num_jobs_range_max,
                        "organization_num_jobs_range_min": organization_num_jobs_range_min,
                        "page": page,
                        "per_page": per_page,
                        "person_locations": person_locations,
                        "person_seniorities": person_seniorities,
                        "person_titles": person_titles,
                        "q_keywords": q_keywords,
                        "q_organization_domains_list": q_organization_domains_list,
                        "q_organization_job_titles": q_organization_job_titles,
                        "revenue_range_max": revenue_range_max,
                        "revenue_range_min": revenue_range_min,
                    },
                    person_search_params.PersonSearchParams,
                ),
            ),
            cast_to=PersonSearchResponse,
        )


class AsyncPeopleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncPeopleResourceWithStreamingResponse(self)

    async def bulk_enrichment(
        self,
        *,
        details: Iterable[person_bulk_enrichment_params.Detail],
        reveal_personal_emails: bool | Omit = omit,
        reveal_phone_number: bool | Omit = omit,
        run_waterfall_email: bool | Omit = omit,
        run_waterfall_phone: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonBulkEnrichmentResponse:
        """
        Use the Bulk People Enrichment endpoint to enrich data for up to 10 people with
        a single API call. To enrich data for only 1 person, use the
        <a href="https://docs.apollo.io/reference/people-enrichment" target="_blank">People
        Enrichment endpoint</a> instead.

        Apollo relies on the information you pass via the endpoint's parameters to
        identify the correct people to enrich. When you provide more information, Apollo
        is more likely to find matches within its database. If you only provide general
        information, such as a name without a domain or email address, you might receive
        a `200` response, but the response will indicate that no records have been
        enriched. The details for each person should be passed as an object with the
        `details[]` array.

        By default, this endpoint does not return personal emails or phone numbers. Use
        the `reveal_personal_emails` and `reveal_phone_number` parameters to retrieve
        emails and phone numbers. If you set either of these parameters to `true`,
        Apollo will attempt to provide emails or phone numbers for all matches.

        You can use also use the `run_waterfall_email` and `run_waterfall_phone`
        parameters to run waterfall enrichment via this endpoint.
        [Waterfall enrichment](https://knowledge.apollo.io/hc/en-us/articles/34071089002509-Waterfall-Enrichment-Overview)
        gives you broader data coverage by checking connected third-party data sources
        for contact emails and phone numbers. When you call this endpoint and include at
        least one waterfall parameter, Apollo returns an immediate synchronous response
        with demographic and firmographic data, along with a waterfall enrichment
        request status. Apollo delivers enriched emails and/or phone numbers
        asynchronously to a configured webhook.

        Using this endpoint will consume credits based on your account's pricing plan.
        If you run waterfall enrichment parameters, your
        [credit usage](https://knowledge.apollo.io/hc/en-us/articles/34071089002509-Waterfall-Enrichment-Overview#does-waterfall-enrichment-require-credits)
        depends on the type of data you request (emails and/or phone numbers) and which
        data source returns enriched data. To view a summary of Apollo's pricing, visit
        the <a href="https://www.apollo.io/pricing" target="_blank"> public pricing page
        ↗</a> For detailed information regarding API credit usage, see the
        <a href="https://app.apollo.io/#/settings/credits/about" target="_blank"> API
        enrichment ↗</a> section on the _About Credits_ page (login required).

        This endpoint's
        <a href="https://docs.apollo.io/reference/rate-limits" target="_blank">rate
        limit</a> is throttled to 50% of the People Enrichment endpoint's per-minute
        rate limit, and is 100% of the hourly and daily rate limits for the same
        individual endpoint.

        Args:
          details: Provide info for each person you want to enrich as an object within this array.
              Add up to 10 people.

          reveal_personal_emails: Set to `true` if you want to enrich all matched people with personal emails.
              This potentially consumes credits as part of your
              <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
              plan</a>. The default value is `false`.

              If a person resides in a
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4409141087757" target="_blank">GDPR</a>-compliant
              region, Apollo will not reveal their personal email.

          reveal_phone_number: Set to `true` if you want to enrich the data of all matched people with all
              available phone numbers, including mobile phone numbers. This potentially
              consumes credits as part of your
              <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
              plan</a>. The default value is `false`.

              If this parameter is set to `true`, you must enter a webhook URL for the
              `webhook_url` parameter. Apollo will asynchronously verify phone numbers for
              you, then send a JSON response that includes only details about the phone
              numbers to the webhook URL you provide. It can take several minutes for the
              phone numbers to be delivered.

          run_waterfall_email: Set to true to enable email waterfall enrichment

          run_waterfall_phone: Set to true to enable phone waterfall enrichment

          webhook_url: If you set the `reveal_phone_number` parameter to `true`, this parameter becomes
              mandatory. Otherwise, do not use this parameter.

              Enter the webhook URL that specifies where Apollo should send a JSON response
              that includes the phone number you requested. Apollo suggests testing this flow
              to ensure you receive the separate response with the phone number.

              If phone numbers are not revealed delivered to the webhook URL, try applying
              UTF-8 encoding to the webhook URL.

              Example: `https://webhook.site/cc4cf44e-e047-4774-8dac-473d28474e40`;
              `https%3A%2F%2Fwebhook.site%2Fcc4cf44e-e047-4774-8dac-473d28474e40`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/people/bulk_match",
            body=await async_maybe_transform(
                {"details": details}, person_bulk_enrichment_params.PersonBulkEnrichmentParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "reveal_personal_emails": reveal_personal_emails,
                        "reveal_phone_number": reveal_phone_number,
                        "run_waterfall_email": run_waterfall_email,
                        "run_waterfall_phone": run_waterfall_phone,
                        "webhook_url": webhook_url,
                    },
                    person_bulk_enrichment_params.PersonBulkEnrichmentParams,
                ),
            ),
            cast_to=PersonBulkEnrichmentResponse,
        )

    async def enrichment(
        self,
        *,
        id: str | Omit = omit,
        domain: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        hashed_email: str | Omit = omit,
        last_name: str | Omit = omit,
        linkedin_url: str | Omit = omit,
        name: str | Omit = omit,
        organization_name: str | Omit = omit,
        reveal_personal_emails: bool | Omit = omit,
        reveal_phone_number: bool | Omit = omit,
        run_waterfall_email: bool | Omit = omit,
        run_waterfall_phone: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonEnrichmentResponse:
        """Use the People Enrichment endpoint to enrich data for 1 person.

        To enrich data
        for up to 10 people with a single API call, use the
        <a href="https://docs.apollo.io/reference/bulk-people-enrichment" target="_blank">Bulk
        People Enrichment endpoint</a> instead.

        Apollo relies on the information you pass via the endpoint's parameters to
        identify the correct person to enrich. If you provide more information about a
        person, Apollo is more likely to find a match within its database. If you only
        provide general information, such as a name without a domain or email address,
        you might receive a 200 response, but the response will indicate that no records
        have been enriched.

        By default, this endpoint does not return personal emails or phone numbers. Use
        the `reveal_personal_emails` and `reveal_phone_number` parameters to retrieve
        emails and phone numbers.

        You can use also use the `run_waterfall_email` and `run_waterfall_phone`
        parameters to run waterfall enrichment via this endpoint.
        [Waterfall enrichment](https://knowledge.apollo.io/hc/en-us/articles/34071089002509-Waterfall-Enrichment-Overview)
        gives you broader data coverage by checking connected third-party data sources
        for contact emails and phone numbers. When you call this endpoint and include at
        least one waterfall parameter, Apollo returns an immediate synchronous response
        with demographic and firmographic data, along with a waterfall enrichment
        request status. Apollo delivers enriched emails and/or phone numbers
        asynchronously to a configured webhook.

        Using this endpoint will consume credits based on your account's pricing plan.
        If you run waterfall enrichment parameters, your
        [credit usage](https://knowledge.apollo.io/hc/en-us/articles/34071089002509-Waterfall-Enrichment-Overview#does-waterfall-enrichment-require-credits)
        depends on the type of data you request (emails and/or phone numbers) and which
        data source returns enriched data. To view a summary of Apollo's pricing, visit
        the <a href="https://www.apollo.io/pricing" target="_blank"> public pricing page
        ↗</a> For detailed information regarding API credit usage, see the
        <a href="https://app.apollo.io/#/settings/credits/about" target="_blank"> API
        enrichment ↗</a> section on the _About Credits_ page (login required).

        Args:
          id: The Apollo ID for the person. Each person in the Apollo database is assigned a
              unique ID.

              To find IDs, call the
              <a href="https://docs.apollo.io/reference/people-api-search" target="_blank">People
              API Search endpoint</a> and identify the values for `person_id`.

              Example: `587cf802f65125cad923a266`

          domain: The domain name for the person's employer. This can be the current employer or a
              previous employer. Do not include `www.`, the `@` symbol, or similar.

              Example: `apollo.io` or `microsoft.com`

          email: The email address of the person.

              Example: `example@email.com`

          first_name: The first name of the person. This is typically used in combination with the
              `last_name` parameter.

              Example: `tim`

          hashed_email: The hashed email of the person. The email should adhere to either the MD5 or
              SHA-256 hash format.

              Example: `8d935115b9ff4489f2d1f9249503cadf` (MD5) or
              `97817c0c49994eb500ad0a5e7e2d8aed51977b26424d508f66e4e8887746a152` (SHA-256)

          last_name: The last name of the person. This is typically used in combination with the
              `first_name` parameter.

              Example: `zheng`

          linkedin_url: The URL for the person's LinkedIn profile.

              Example: `http://www.linkedin.com/in/tim-zheng-677ba010`

          name: The full name of the person. This will typically be a first name and last name
              separated by a space. If you use this parameter, you do not need to use the
              `first_name` and `last_name` parameters.

              Example: `tim zheng`

          organization_name: The name of the person's employer. This can be the current employer or a
              previous employer.

              Example: `apollo`

          reveal_personal_emails: Set to `true` if you want to enrich the person's data with personal emails. This
              potentially consumes credits as part of your
              <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
              plan</a>. The default value is `false`.

              If a person resides in a
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4409141087757" target="_blank">GDPR</a>-compliant
              region, Apollo will not reveal their personal email.

          reveal_phone_number: Set to `true` if you want to enrich the person's data with all available phone
              numbers, including mobile phone numbers. This potentially consumes credits as
              part of your
              <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
              plan</a>. The default value is `false`.

              If this parameter is set to `true`, you must enter a webhook URL for the
              `webhook_url` parameter. Apollo will asynchronously verify phone numbers for
              you, then send a JSON response that includes only details about the person's
              phone numbers to the webhook URL you provide. It can take several minutes for
              the phone numbers to be delivered.

          run_waterfall_email: Set to true to enable email waterfall enrichment

          run_waterfall_phone: Set to true to enable phone waterfall enrichment

          webhook_url: If you set the `reveal_phone_number` parameter to `true`, this parameter becomes
              mandatory. Otherwise, do not use this parameter.

              Enter the webhook URL that specifies where Apollo should send a JSON response
              that includes the phone number you requested. Apollo suggests testing this flow
              to ensure you receive the separate response with the phone number.

              If phone numbers are not revealed delivered to the webhook URL, try applying
              UTF-8 encoding to the webhook URL.

              Example: `https://webhook.site/cc4cf44e-e047-4774-8dac-473d28474e40`;
              `https%3A%2F%2Fwebhook.site%2Fcc4cf44e-e047-4774-8dac-473d28474e40`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/people/match",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "domain": domain,
                        "email": email,
                        "first_name": first_name,
                        "hashed_email": hashed_email,
                        "last_name": last_name,
                        "linkedin_url": linkedin_url,
                        "name": name,
                        "organization_name": organization_name,
                        "reveal_personal_emails": reveal_personal_emails,
                        "reveal_phone_number": reveal_phone_number,
                        "run_waterfall_email": run_waterfall_email,
                        "run_waterfall_phone": run_waterfall_phone,
                        "webhook_url": webhook_url,
                    },
                    person_enrichment_params.PersonEnrichmentParams,
                ),
            ),
            cast_to=PersonEnrichmentResponse,
        )

    async def search(
        self,
        *,
        contact_email_status: SequenceNotStr[str] | Omit = omit,
        currently_not_using_any_of_technology_uids: SequenceNotStr[str] | Omit = omit,
        currently_using_all_of_technology_uids: SequenceNotStr[str] | Omit = omit,
        currently_using_any_of_technology_uids: SequenceNotStr[str] | Omit = omit,
        include_similar_titles: bool | Omit = omit,
        organization_ids: SequenceNotStr[str] | Omit = omit,
        organization_job_locations: SequenceNotStr[str] | Omit = omit,
        organization_job_posted_at_range_max: Union[str, date] | Omit = omit,
        organization_job_posted_at_range_min: Union[str, date] | Omit = omit,
        organization_locations: SequenceNotStr[str] | Omit = omit,
        organization_num_employees_ranges: SequenceNotStr[str] | Omit = omit,
        organization_num_jobs_range_max: int | Omit = omit,
        organization_num_jobs_range_min: int | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        person_locations: SequenceNotStr[str] | Omit = omit,
        person_seniorities: SequenceNotStr[str] | Omit = omit,
        person_titles: SequenceNotStr[str] | Omit = omit,
        q_keywords: str | Omit = omit,
        q_organization_domains_list: SequenceNotStr[str] | Omit = omit,
        q_organization_job_titles: SequenceNotStr[str] | Omit = omit,
        revenue_range_max: int | Omit = omit,
        revenue_range_min: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonSearchResponse:
        """Use the People API Search endpoint to find net new people in the Apollo
        database.

        Several filters are available to help narrow your search.

        This endpoint is optimized for API usage and does not consume credits. This
        endpoint is primarily designed for prospecting net new people.

        This endpoint does not return email addresses or phone numbers. Use the
        <a href="https://docs.apollo.io/reference/people-enrichment" target="_blank">People
        Enrichment</a> or
        <a href="https://docs.apollo.io/reference/bulk-people-enrichment" target="_blank">Bulk
        People Enrichment</a> endpoints to enrich data.

        This endpoint requires a master API key. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        To protect Apollo's performance for all users, this endpoint has a display limit
        of 50,000 records (100 records per page, up to 500 pages). Add more filters to
        narrow your search results as much as possible. This limitation does not
        restrict your access to Apollo's database; you just need to access the data in
        batches.

        Args:
          contact_email_status: The email statuses for the people you want to find. You can add multiple
              statuses to expand your search.

              The statuses you can search include: <ul> <li> <code>verified</code> </li> <li>
              <code>unverified</code> </li> <li> <code>likely to engage</code> </li> <li>
              <code>unavailable</code> </li> </ul>

          currently_not_using_any_of_technology_uids: Exclude people from your search based on any of the technologies their current
              employer uses. Apollo supports filtering by 1,500+ technologies.

              Apollo calculates technologies data from multiple sources. This data is updated
              regularly. Check out the full list of supported technologies by
              <a href="https://api.apollo.io/v1/auth/supported_technologies_csv" target="_blank">downloading
              this CSV file</a>.

              Use underscores (`_`) to replace spaces and periods for the technologies listed
              in the CSV file.

              Examples: `salesforce`; `google_analytics`; `wordpress_org`

          currently_using_all_of_technology_uids: Find people based on all of the technologies their current employer uses. Apollo
              supports filtering by 1,500+ technologies.

              Apollo calculates technologies data from multiple sources. This data is updated
              regularly. Check out the full list of supported technologies by
              <a href="https://api.apollo.io/v1/auth/supported_technologies_csv" target="_blank">downloading
              this CSV file</a>.

              Use underscores (`_`) to replace spaces and periods for the technologies listed
              in the CSV file.

              Examples: `salesforce`; `google_analytics`; `wordpress_org`

          currently_using_any_of_technology_uids: Find people based on any of the technologies their current employer uses. Apollo
              supports filtering by 1,500+ technologies.

              Apollo calculates technologies data from multiple sources. This data is updated
              regularly. Check out the full list of supported technologies by
              <a href="https://api.apollo.io/v1/auth/supported_technologies_csv" target="_blank">downloading
              this CSV file</a>.

              Use underscores (`_`) to replace spaces and periods for the technologies listed
              in the CSV file.

              Examples: `salesforce`; `google_analytics`; `wordpress_org`

          include_similar_titles: This parameter determines whether people with job titles similar to the titles
              you define in the `person_titles[]` parameter are returned in the response.

              Set this parameter to `false` when using `person_titles[]` to return only strict
              matches for job titles.

          organization_ids: The Apollo IDs for the companies (employers) you want to include in your search
              results. Each company in the Apollo database is assigned a unique ID.

              To find IDs, call the
              <a href="https://docs.apollo.io/reference/organization-search" target="_blank">Organization
              Search endpoint</a> and identify the values for `organization_id`.

              Example: `5e66b6381e05b4008c8331b8`

          organization_job_locations: The locations of the jobs being actively recruited by the person's employer.

              Examples: `atlanta`; `japan`

          organization_job_posted_at_range_max: The latest date when jobs were posted by the person's current employer. Use this
              parameter in combination with `organization_job_posted_at_range[min]` to set a
              date range for when jobs posted.

              Example: `2025-09-25`

          organization_job_posted_at_range_min: The earliest date when jobs were posted by the person's current employer. Use
              this parameter in combination with `organization_job_posted_at_range[max]` to
              set a date range for when jobs posted.

              Example: `2025-07-25`

          organization_locations: The location of the company headquarters for a person's current employer. You
              can search across cities, US states, and countries.

              If a company has several office locations, results are still based on the
              headquarters location. For example, if you search `chicago` but a company's HQ
              location is in `boston`, people that work for the Boston-based company will not
              appear in your results, even if they match other \\pparameters.

              To find people based on their personal location, use the `person_locations`
              parameter.

              Examples: `texas`; `tokyo`; `spain`

          organization_num_employees_ranges: The number range of employees working for the person's current company. This
              enables you to find people based on the headcount of their employer. You can add
              multiple ranges to expand your search results.

              Each range you add needs to be a string, with the upper and lower numbers of the
              range separated only by a comma.

              Examples: `1,10`; `250,500`; `10000,20000`

          organization_num_jobs_range_max: The maximum number of job postings active at the person's current empployer. Use
              this parameter in combination with `organization_num_jobs_range[min]` to set a
              job postings range.

              Examples: `50`; `500`

          organization_num_jobs_range_min: The minimum number of job postings active at the person's current empployer. Use
              this parameter in combination with `organization_num_jobs_range[max]` to set a
              job postings range.

              Examples: `50`; `500`

          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          person_locations: The location where people live. You can search across cities, US states, and
              countries.

              To find people based on the headquarters locations of their current employer,
              use the `organization_locations` parameter.

              Examples: `california`; `ireland`; `chicago`

          person_seniorities: The job seniority that people hold within their current employer. This enables
              you to find people that currently hold positions at certain reporting levels,
              such as Director level or senior IC level.

              For a person to be included in search results, they only need to match 1 of the
              seniorities you add. Adding more seniorities expands your search results.

              Searches only return results based on their current job title, so searching for
              Director-level employees only returns people that currently hold a
              Director-level title. If someone was previously a Director, but is currently a
              VP, they would not be included in your search results.

              Use this parameter in combination with the `person_titles[]` parameter to find
              people based on specific job functions and seniority levels.

              The following options can be used for this parameter:

              <ul><li><code>owner</code></li><li><code>founder</code></li><li><code>c_suite</code></li><li><code>partner</code></li><li><code>vp</code></li><li><code>head</code></li><li><code>director</code></li><li><code>manager</code></li><li><code>senior</code></li><li><code>entry</code></li><li><code>intern</code></li></ul>

          person_titles: Job titles held by the people you want to find. For a person to be included in
              search results, they only need to match 1 of the job titles you add. Adding more
              job titles expands your search results.

              Results also include job titles with the same terms, even if they are not exact
              matches. For example, searching for `marketing manager` might return people with
              the job title `content marketing manager`.

              Use this parameter in combination with the `person_seniorities[]` parameter to
              find people based on specific job functions and seniority levels.

              Examples: `sales development representative`; `marketing manager`;
              `research analyst`

          q_keywords: A string of words over which we want to filter the results.

          q_organization_domains_list: The domain name for the person's employer. This can be the current employer or a
              previous employer. Do not include `www.`, the `@` symbol, or similar.

              This parameter accepts up to 1,000 domains in a single request.

              Examples: `apollo.io`; `microsoft.com`

          q_organization_job_titles: The job titles that are listed in active job postings at the person's current
              employer.

              Examples: `sales manager`; `research analyst`

          revenue_range_max: The maximum revenue the person's current employer generates. Use this parameter
              in combination with `revenue_range[min]` to set a revenue range.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Examples: `500000`; `1500000`

          revenue_range_min: The minimum revenue the person's current employer generates. Use this parameter
              in combination with `revenue_range[max]` to set a revenue range.

              Do not enter currency symbols, commas, or decimal points in the figure.

              Examples: `500000`; `1500000`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/mixed_people/api_search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "contact_email_status": contact_email_status,
                        "currently_not_using_any_of_technology_uids": currently_not_using_any_of_technology_uids,
                        "currently_using_all_of_technology_uids": currently_using_all_of_technology_uids,
                        "currently_using_any_of_technology_uids": currently_using_any_of_technology_uids,
                        "include_similar_titles": include_similar_titles,
                        "organization_ids": organization_ids,
                        "organization_job_locations": organization_job_locations,
                        "organization_job_posted_at_range_max": organization_job_posted_at_range_max,
                        "organization_job_posted_at_range_min": organization_job_posted_at_range_min,
                        "organization_locations": organization_locations,
                        "organization_num_employees_ranges": organization_num_employees_ranges,
                        "organization_num_jobs_range_max": organization_num_jobs_range_max,
                        "organization_num_jobs_range_min": organization_num_jobs_range_min,
                        "page": page,
                        "per_page": per_page,
                        "person_locations": person_locations,
                        "person_seniorities": person_seniorities,
                        "person_titles": person_titles,
                        "q_keywords": q_keywords,
                        "q_organization_domains_list": q_organization_domains_list,
                        "q_organization_job_titles": q_organization_job_titles,
                        "revenue_range_max": revenue_range_max,
                        "revenue_range_min": revenue_range_min,
                    },
                    person_search_params.PersonSearchParams,
                ),
            ),
            cast_to=PersonSearchResponse,
        )


class PeopleResourceWithRawResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.bulk_enrichment = to_raw_response_wrapper(
            people.bulk_enrichment,
        )
        self.enrichment = to_raw_response_wrapper(
            people.enrichment,
        )
        self.search = to_raw_response_wrapper(
            people.search,
        )


class AsyncPeopleResourceWithRawResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.bulk_enrichment = async_to_raw_response_wrapper(
            people.bulk_enrichment,
        )
        self.enrichment = async_to_raw_response_wrapper(
            people.enrichment,
        )
        self.search = async_to_raw_response_wrapper(
            people.search,
        )


class PeopleResourceWithStreamingResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.bulk_enrichment = to_streamed_response_wrapper(
            people.bulk_enrichment,
        )
        self.enrichment = to_streamed_response_wrapper(
            people.enrichment,
        )
        self.search = to_streamed_response_wrapper(
            people.search,
        )


class AsyncPeopleResourceWithStreamingResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.bulk_enrichment = async_to_streamed_response_wrapper(
            people.bulk_enrichment,
        )
        self.enrichment = async_to_streamed_response_wrapper(
            people.enrichment,
        )
        self.search = async_to_streamed_response_wrapper(
            people.search,
        )
