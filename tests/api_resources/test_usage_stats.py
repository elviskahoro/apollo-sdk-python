# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from apollo import ApolloSDK, AsyncApolloSDK

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsageStats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_api_usage_stats(self, client: ApolloSDK) -> None:
        usage_stat = client.usage_stats.api_usage_stats()
        assert usage_stat is None

    @parametrize
    def test_raw_response_api_usage_stats(self, client: ApolloSDK) -> None:
        response = client.usage_stats.with_raw_response.api_usage_stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_stat = response.parse()
        assert usage_stat is None

    @parametrize
    def test_streaming_response_api_usage_stats(self, client: ApolloSDK) -> None:
        with client.usage_stats.with_streaming_response.api_usage_stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_stat = response.parse()
            assert usage_stat is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUsageStats:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_api_usage_stats(self, async_client: AsyncApolloSDK) -> None:
        usage_stat = await async_client.usage_stats.api_usage_stats()
        assert usage_stat is None

    @parametrize
    async def test_raw_response_api_usage_stats(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.usage_stats.with_raw_response.api_usage_stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_stat = await response.parse()
        assert usage_stat is None

    @parametrize
    async def test_streaming_response_api_usage_stats(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.usage_stats.with_streaming_response.api_usage_stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_stat = await response.parse()
            assert usage_stat is None

        assert cast(Any, response.is_closed) is True
