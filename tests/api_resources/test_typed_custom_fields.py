# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from src import ApolloSDK, AsyncApolloSDK
from src.types import TypedCustomFieldListResponse
from tests.utils import assert_matches_type

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTypedCustomFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: ApolloSDK) -> None:
        with pytest.warns(DeprecationWarning):
            typed_custom_field = client.typed_custom_fields.list()

        assert_matches_type(TypedCustomFieldListResponse, typed_custom_field, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ApolloSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.typed_custom_fields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        typed_custom_field = response.parse()
        assert_matches_type(TypedCustomFieldListResponse, typed_custom_field, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ApolloSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.typed_custom_fields.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                typed_custom_field = response.parse()
                assert_matches_type(TypedCustomFieldListResponse, typed_custom_field, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTypedCustomFields:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncApolloSDK) -> None:
        with pytest.warns(DeprecationWarning):
            typed_custom_field = await async_client.typed_custom_fields.list()

        assert_matches_type(TypedCustomFieldListResponse, typed_custom_field, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncApolloSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.typed_custom_fields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        typed_custom_field = await response.parse()
        assert_matches_type(TypedCustomFieldListResponse, typed_custom_field, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncApolloSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.typed_custom_fields.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                typed_custom_field = await response.parse()
                assert_matches_type(TypedCustomFieldListResponse, typed_custom_field, path=["response"])

        assert cast(Any, response.is_closed) is True
