# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from apollo import ApolloSDK, AsyncApolloSDK
from apollo.types import FieldListResponse, FieldCreateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ApolloSDK) -> None:
        field = client.fields.create()
        assert_matches_type(FieldCreateResponse, field, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ApolloSDK) -> None:
        field = client.fields.create(
            label="label",
            meta={"max_length": 0},
            modality="contact",
            type="string",
        )
        assert_matches_type(FieldCreateResponse, field, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ApolloSDK) -> None:
        response = client.fields.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(FieldCreateResponse, field, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ApolloSDK) -> None:
        with client.fields.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(FieldCreateResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: ApolloSDK) -> None:
        field = client.fields.list()
        assert_matches_type(FieldListResponse, field, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ApolloSDK) -> None:
        field = client.fields.list(
            source="system",
        )
        assert_matches_type(FieldListResponse, field, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ApolloSDK) -> None:
        response = client.fields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(FieldListResponse, field, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ApolloSDK) -> None:
        with client.fields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(FieldListResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFields:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncApolloSDK) -> None:
        field = await async_client.fields.create()
        assert_matches_type(FieldCreateResponse, field, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        field = await async_client.fields.create(
            label="label",
            meta={"max_length": 0},
            modality="contact",
            type="string",
        )
        assert_matches_type(FieldCreateResponse, field, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.fields.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(FieldCreateResponse, field, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.fields.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(FieldCreateResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncApolloSDK) -> None:
        field = await async_client.fields.list()
        assert_matches_type(FieldListResponse, field, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        field = await async_client.fields.list(
            source="system",
        )
        assert_matches_type(FieldListResponse, field, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.fields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(FieldListResponse, field, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.fields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(FieldListResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True
