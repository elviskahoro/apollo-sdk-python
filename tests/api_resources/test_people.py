# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from apollo_sdk import ApolloSDK, AsyncApolloSDK
from tests.utils import assert_matches_type
from apollo_sdk.types import (
    PersonSearchResponse,
    PersonEnrichmentResponse,
    PersonBulkEnrichmentResponse,
)
from apollo_sdk._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPeople:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_bulk_enrichment(self, client: ApolloSDK) -> None:
        person = client.people.bulk_enrichment(
            details=[{}],
        )
        assert_matches_type(PersonBulkEnrichmentResponse, person, path=["response"])

    @parametrize
    def test_method_bulk_enrichment_with_all_params(self, client: ApolloSDK) -> None:
        person = client.people.bulk_enrichment(
            details=[
                {
                    "id": "64a7ff0cc4dfae00013df1a5",
                    "domain": "domain",
                    "email": "email",
                    "first_name": "first_name",
                    "hashed_email": "hashed_email",
                    "last_name": "last_name",
                    "linkedin_url": "linkedin_url",
                    "name": "name",
                    "organization_name": "organization_name",
                }
            ],
            reveal_personal_emails=True,
            reveal_phone_number=True,
            run_waterfall_email=True,
            run_waterfall_phone=True,
            webhook_url="webhook_url",
        )
        assert_matches_type(PersonBulkEnrichmentResponse, person, path=["response"])

    @parametrize
    def test_raw_response_bulk_enrichment(self, client: ApolloSDK) -> None:
        response = client.people.with_raw_response.bulk_enrichment(
            details=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PersonBulkEnrichmentResponse, person, path=["response"])

    @parametrize
    def test_streaming_response_bulk_enrichment(self, client: ApolloSDK) -> None:
        with client.people.with_streaming_response.bulk_enrichment(
            details=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PersonBulkEnrichmentResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_enrichment(self, client: ApolloSDK) -> None:
        person = client.people.enrichment()
        assert_matches_type(PersonEnrichmentResponse, person, path=["response"])

    @parametrize
    def test_method_enrichment_with_all_params(self, client: ApolloSDK) -> None:
        person = client.people.enrichment(
            id="id",
            domain="domain",
            email="email",
            first_name="first_name",
            hashed_email="hashed_email",
            last_name="last_name",
            linkedin_url="linkedin_url",
            name="name",
            organization_name="organization_name",
            reveal_personal_emails=True,
            reveal_phone_number=True,
            run_waterfall_email=True,
            run_waterfall_phone=True,
            webhook_url="webhook_url",
        )
        assert_matches_type(PersonEnrichmentResponse, person, path=["response"])

    @parametrize
    def test_raw_response_enrichment(self, client: ApolloSDK) -> None:
        response = client.people.with_raw_response.enrichment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PersonEnrichmentResponse, person, path=["response"])

    @parametrize
    def test_streaming_response_enrichment(self, client: ApolloSDK) -> None:
        with client.people.with_streaming_response.enrichment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PersonEnrichmentResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: ApolloSDK) -> None:
        person = client.people.search()
        assert_matches_type(PersonSearchResponse, person, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: ApolloSDK) -> None:
        person = client.people.search(
            contact_email_status=["string"],
            currently_not_using_any_of_technology_uids=["string"],
            currently_using_all_of_technology_uids=["string"],
            currently_using_any_of_technology_uids=["string"],
            include_similar_titles=True,
            organization_ids=["string"],
            organization_job_locations=["string"],
            organization_job_posted_at_range_max=parse_date("2019-12-27"),
            organization_job_posted_at_range_min=parse_date("2019-12-27"),
            organization_locations=["string"],
            organization_num_employees_ranges=["string"],
            organization_num_jobs_range_max=0,
            organization_num_jobs_range_min=0,
            page=0,
            per_page=0,
            person_locations=["string"],
            person_seniorities=["string"],
            person_titles=["string"],
            q_keywords="q_keywords",
            q_organization_domains_list=["string"],
            q_organization_job_titles=["string"],
            revenue_range_max=0,
            revenue_range_min=0,
        )
        assert_matches_type(PersonSearchResponse, person, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: ApolloSDK) -> None:
        response = client.people.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PersonSearchResponse, person, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: ApolloSDK) -> None:
        with client.people.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PersonSearchResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPeople:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_bulk_enrichment(self, async_client: AsyncApolloSDK) -> None:
        person = await async_client.people.bulk_enrichment(
            details=[{}],
        )
        assert_matches_type(PersonBulkEnrichmentResponse, person, path=["response"])

    @parametrize
    async def test_method_bulk_enrichment_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        person = await async_client.people.bulk_enrichment(
            details=[
                {
                    "id": "64a7ff0cc4dfae00013df1a5",
                    "domain": "domain",
                    "email": "email",
                    "first_name": "first_name",
                    "hashed_email": "hashed_email",
                    "last_name": "last_name",
                    "linkedin_url": "linkedin_url",
                    "name": "name",
                    "organization_name": "organization_name",
                }
            ],
            reveal_personal_emails=True,
            reveal_phone_number=True,
            run_waterfall_email=True,
            run_waterfall_phone=True,
            webhook_url="webhook_url",
        )
        assert_matches_type(PersonBulkEnrichmentResponse, person, path=["response"])

    @parametrize
    async def test_raw_response_bulk_enrichment(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.people.with_raw_response.bulk_enrichment(
            details=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PersonBulkEnrichmentResponse, person, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_enrichment(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.people.with_streaming_response.bulk_enrichment(
            details=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PersonBulkEnrichmentResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_enrichment(self, async_client: AsyncApolloSDK) -> None:
        person = await async_client.people.enrichment()
        assert_matches_type(PersonEnrichmentResponse, person, path=["response"])

    @parametrize
    async def test_method_enrichment_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        person = await async_client.people.enrichment(
            id="id",
            domain="domain",
            email="email",
            first_name="first_name",
            hashed_email="hashed_email",
            last_name="last_name",
            linkedin_url="linkedin_url",
            name="name",
            organization_name="organization_name",
            reveal_personal_emails=True,
            reveal_phone_number=True,
            run_waterfall_email=True,
            run_waterfall_phone=True,
            webhook_url="webhook_url",
        )
        assert_matches_type(PersonEnrichmentResponse, person, path=["response"])

    @parametrize
    async def test_raw_response_enrichment(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.people.with_raw_response.enrichment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PersonEnrichmentResponse, person, path=["response"])

    @parametrize
    async def test_streaming_response_enrichment(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.people.with_streaming_response.enrichment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PersonEnrichmentResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncApolloSDK) -> None:
        person = await async_client.people.search()
        assert_matches_type(PersonSearchResponse, person, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        person = await async_client.people.search(
            contact_email_status=["string"],
            currently_not_using_any_of_technology_uids=["string"],
            currently_using_all_of_technology_uids=["string"],
            currently_using_any_of_technology_uids=["string"],
            include_similar_titles=True,
            organization_ids=["string"],
            organization_job_locations=["string"],
            organization_job_posted_at_range_max=parse_date("2019-12-27"),
            organization_job_posted_at_range_min=parse_date("2019-12-27"),
            organization_locations=["string"],
            organization_num_employees_ranges=["string"],
            organization_num_jobs_range_max=0,
            organization_num_jobs_range_min=0,
            page=0,
            per_page=0,
            person_locations=["string"],
            person_seniorities=["string"],
            person_titles=["string"],
            q_keywords="q_keywords",
            q_organization_domains_list=["string"],
            q_organization_job_titles=["string"],
            revenue_range_max=0,
            revenue_range_min=0,
        )
        assert_matches_type(PersonSearchResponse, person, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.people.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PersonSearchResponse, person, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.people.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PersonSearchResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True
