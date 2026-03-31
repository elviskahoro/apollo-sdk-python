# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from src import ApolloSDK, AsyncApolloSDK
from src.types import (
    OrganizationEnrichResponse,
    OrganizationSearchResponse,
    OrganizationBulkEnrichResponse,
    OrganizationJobPostingsResponse,
)
from src._utils import parse_date
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_bulk_enrich(self, client: ApolloSDK) -> None:
        organization = client.organizations.bulk_enrich(
            domains=["string"],
        )
        assert_matches_type(OrganizationBulkEnrichResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_bulk_enrich(self, client: ApolloSDK) -> None:
        response = client.organizations.with_raw_response.bulk_enrich(
            domains=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationBulkEnrichResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_bulk_enrich(self, client: ApolloSDK) -> None:
        with client.organizations.with_streaming_response.bulk_enrich(
            domains=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationBulkEnrichResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_enrich(self, client: ApolloSDK) -> None:
        organization = client.organizations.enrich(
            domain="domain",
        )
        assert_matches_type(OrganizationEnrichResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_enrich(self, client: ApolloSDK) -> None:
        response = client.organizations.with_raw_response.enrich(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationEnrichResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_enrich(self, client: ApolloSDK) -> None:
        with client.organizations.with_streaming_response.enrich(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationEnrichResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_job_postings(self, client: ApolloSDK) -> None:
        organization = client.organizations.job_postings(
            organization_id="organization_id",
        )
        assert_matches_type(OrganizationJobPostingsResponse, organization, path=["response"])

    @parametrize
    def test_method_job_postings_with_all_params(self, client: ApolloSDK) -> None:
        organization = client.organizations.job_postings(
            organization_id="organization_id",
            page=0,
            per_page=0,
        )
        assert_matches_type(OrganizationJobPostingsResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_job_postings(self, client: ApolloSDK) -> None:
        response = client.organizations.with_raw_response.job_postings(
            organization_id="organization_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationJobPostingsResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_job_postings(self, client: ApolloSDK) -> None:
        with client.organizations.with_streaming_response.job_postings(
            organization_id="organization_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationJobPostingsResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_job_postings(self, client: ApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.with_raw_response.job_postings(
                organization_id="",
            )

    @parametrize
    def test_method_search(self, client: ApolloSDK) -> None:
        organization = client.organizations.search()
        assert_matches_type(OrganizationSearchResponse, organization, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: ApolloSDK) -> None:
        organization = client.organizations.search(
            currently_using_any_of_technology_uids=["string"],
            latest_funding_amount_range_max=0,
            latest_funding_amount_range_min=0,
            latest_funding_date_range_max=parse_date("2019-12-27"),
            latest_funding_date_range_min=parse_date("2019-12-27"),
            organization_ids=["string"],
            organization_job_locations=["string"],
            organization_job_posted_at_range_max=parse_date("2019-12-27"),
            organization_job_posted_at_range_min=parse_date("2019-12-27"),
            organization_locations=["string"],
            organization_not_locations=["string"],
            organization_num_employees_ranges=["string"],
            organization_num_jobs_range_max=0,
            organization_num_jobs_range_min=0,
            page=0,
            per_page=0,
            q_organization_domains_list=["string"],
            q_organization_job_titles=["string"],
            q_organization_keyword_tags=["string"],
            q_organization_name="q_organization_name",
            revenue_range_max=0,
            revenue_range_min=0,
            total_funding_range_max=0,
            total_funding_range_min=0,
        )
        assert_matches_type(OrganizationSearchResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: ApolloSDK) -> None:
        response = client.organizations.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationSearchResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: ApolloSDK) -> None:
        with client.organizations.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationSearchResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_bulk_enrich(self, async_client: AsyncApolloSDK) -> None:
        organization = await async_client.organizations.bulk_enrich(
            domains=["string"],
        )
        assert_matches_type(OrganizationBulkEnrichResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_bulk_enrich(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.organizations.with_raw_response.bulk_enrich(
            domains=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationBulkEnrichResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_enrich(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.organizations.with_streaming_response.bulk_enrich(
            domains=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationBulkEnrichResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_enrich(self, async_client: AsyncApolloSDK) -> None:
        organization = await async_client.organizations.enrich(
            domain="domain",
        )
        assert_matches_type(OrganizationEnrichResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_enrich(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.organizations.with_raw_response.enrich(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationEnrichResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_enrich(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.organizations.with_streaming_response.enrich(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationEnrichResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_job_postings(self, async_client: AsyncApolloSDK) -> None:
        organization = await async_client.organizations.job_postings(
            organization_id="organization_id",
        )
        assert_matches_type(OrganizationJobPostingsResponse, organization, path=["response"])

    @parametrize
    async def test_method_job_postings_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        organization = await async_client.organizations.job_postings(
            organization_id="organization_id",
            page=0,
            per_page=0,
        )
        assert_matches_type(OrganizationJobPostingsResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_job_postings(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.organizations.with_raw_response.job_postings(
            organization_id="organization_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationJobPostingsResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_job_postings(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.organizations.with_streaming_response.job_postings(
            organization_id="organization_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationJobPostingsResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_job_postings(self, async_client: AsyncApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.with_raw_response.job_postings(
                organization_id="",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncApolloSDK) -> None:
        organization = await async_client.organizations.search()
        assert_matches_type(OrganizationSearchResponse, organization, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        organization = await async_client.organizations.search(
            currently_using_any_of_technology_uids=["string"],
            latest_funding_amount_range_max=0,
            latest_funding_amount_range_min=0,
            latest_funding_date_range_max=parse_date("2019-12-27"),
            latest_funding_date_range_min=parse_date("2019-12-27"),
            organization_ids=["string"],
            organization_job_locations=["string"],
            organization_job_posted_at_range_max=parse_date("2019-12-27"),
            organization_job_posted_at_range_min=parse_date("2019-12-27"),
            organization_locations=["string"],
            organization_not_locations=["string"],
            organization_num_employees_ranges=["string"],
            organization_num_jobs_range_max=0,
            organization_num_jobs_range_min=0,
            page=0,
            per_page=0,
            q_organization_domains_list=["string"],
            q_organization_job_titles=["string"],
            q_organization_keyword_tags=["string"],
            q_organization_name="q_organization_name",
            revenue_range_max=0,
            revenue_range_min=0,
            total_funding_range_max=0,
            total_funding_range_min=0,
        )
        assert_matches_type(OrganizationSearchResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.organizations.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationSearchResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.organizations.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationSearchResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True
