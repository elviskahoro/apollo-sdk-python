# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from apollo_sdk import ApolloSDK, AsyncApolloSDK
from tests.utils import assert_matches_type
from apollo_sdk.types import EmailAccountListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: ApolloSDK) -> None:
        email_account = client.email_accounts.list()
        assert_matches_type(EmailAccountListResponse, email_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ApolloSDK) -> None:
        response = client.email_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_account = response.parse()
        assert_matches_type(EmailAccountListResponse, email_account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ApolloSDK) -> None:
        with client.email_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_account = response.parse()
            assert_matches_type(EmailAccountListResponse, email_account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmailAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncApolloSDK) -> None:
        email_account = await async_client.email_accounts.list()
        assert_matches_type(EmailAccountListResponse, email_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.email_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_account = await response.parse()
        assert_matches_type(EmailAccountListResponse, email_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.email_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_account = await response.parse()
            assert_matches_type(EmailAccountListResponse, email_account, path=["response"])

        assert cast(Any, response.is_closed) is True
