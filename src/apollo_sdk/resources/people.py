# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import person_enrichment_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.person_enrichment_response import PersonEnrichmentResponse

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


class PeopleResourceWithRawResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.enrichment = to_raw_response_wrapper(
            people.enrichment,
        )


class AsyncPeopleResourceWithRawResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.enrichment = async_to_raw_response_wrapper(
            people.enrichment,
        )


class PeopleResourceWithStreamingResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.enrichment = to_streamed_response_wrapper(
            people.enrichment,
        )


class AsyncPeopleResourceWithStreamingResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.enrichment = async_to_streamed_response_wrapper(
            people.enrichment,
        )
