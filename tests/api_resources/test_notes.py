# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from src import ApolloSDK, AsyncApolloSDK
from src.types import NoteListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: ApolloSDK) -> None:
        note = client.notes.list()
        assert_matches_type(NoteListResponse, note, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ApolloSDK) -> None:
        note = client.notes.list(
            account_id="account_id",
            calendar_event_id="calendar_event_id",
            contact_id="contact_id",
            contact_ids=["string"],
            conversation_id="conversation_id",
            conversation_ids=["string"],
            limit=100,
            opportunity_id="opportunity_id",
            skip=0,
            sort_by_field="created_at",
            sort_direction="asc",
            start_date="start_date",
        )
        assert_matches_type(NoteListResponse, note, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ApolloSDK) -> None:
        response = client.notes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(NoteListResponse, note, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ApolloSDK) -> None:
        with client.notes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(NoteListResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNotes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncApolloSDK) -> None:
        note = await async_client.notes.list()
        assert_matches_type(NoteListResponse, note, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        note = await async_client.notes.list(
            account_id="account_id",
            calendar_event_id="calendar_event_id",
            contact_id="contact_id",
            contact_ids=["string"],
            conversation_id="conversation_id",
            conversation_ids=["string"],
            limit=100,
            opportunity_id="opportunity_id",
            skip=0,
            sort_by_field="created_at",
            sort_direction="asc",
            start_date="start_date",
        )
        assert_matches_type(NoteListResponse, note, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.notes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(NoteListResponse, note, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.notes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(NoteListResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True
