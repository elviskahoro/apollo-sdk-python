# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from apollo_sdk import ApolloSDK, AsyncApolloSDK
from tests.utils import assert_matches_type
from apollo_sdk.types import OpportunityStageListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOpportunityStages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: ApolloSDK) -> None:
        opportunity_stage = client.opportunity_stages.list()
        assert_matches_type(OpportunityStageListResponse, opportunity_stage, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ApolloSDK) -> None:
        response = client.opportunity_stages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opportunity_stage = response.parse()
        assert_matches_type(OpportunityStageListResponse, opportunity_stage, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ApolloSDK) -> None:
        with client.opportunity_stages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opportunity_stage = response.parse()
            assert_matches_type(OpportunityStageListResponse, opportunity_stage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOpportunityStages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncApolloSDK) -> None:
        opportunity_stage = await async_client.opportunity_stages.list()
        assert_matches_type(OpportunityStageListResponse, opportunity_stage, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.opportunity_stages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opportunity_stage = await response.parse()
        assert_matches_type(OpportunityStageListResponse, opportunity_stage, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.opportunity_stages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opportunity_stage = await response.parse()
            assert_matches_type(OpportunityStageListResponse, opportunity_stage, path=["response"])

        assert cast(Any, response.is_closed) is True
