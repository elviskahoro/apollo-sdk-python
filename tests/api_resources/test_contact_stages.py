# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from apollo_sdk import ApolloSDK, AsyncApolloSDK

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContactStages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: ApolloSDK) -> None:
        contact_stage = client.contact_stages.list()
        assert contact_stage is None

    @parametrize
    def test_raw_response_list(self, client: ApolloSDK) -> None:
        response = client.contact_stages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_stage = response.parse()
        assert contact_stage is None

    @parametrize
    def test_streaming_response_list(self, client: ApolloSDK) -> None:
        with client.contact_stages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_stage = response.parse()
            assert contact_stage is None

        assert cast(Any, response.is_closed) is True


class TestAsyncContactStages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncApolloSDK) -> None:
        contact_stage = await async_client.contact_stages.list()
        assert contact_stage is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.contact_stages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_stage = await response.parse()
        assert contact_stage is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.contact_stages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_stage = await response.parse()
            assert contact_stage is None

        assert cast(Any, response.is_closed) is True
