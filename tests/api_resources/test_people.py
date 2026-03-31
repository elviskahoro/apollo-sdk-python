# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from apollo_sdk import ApolloSDK, AsyncApolloSDK
from tests.utils import assert_matches_type
from apollo_sdk.types import PersonEnrichmentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPeople:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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


class TestAsyncPeople:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

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
