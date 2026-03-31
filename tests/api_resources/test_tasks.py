# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from apollo_sdk import ApolloSDK, AsyncApolloSDK
from tests.utils import assert_matches_type
from apollo_sdk.types import (
    TaskCreateResponse,
    TaskSearchResponse,
    TaskBulkCreateResponse,
)
from apollo_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ApolloSDK) -> None:
        task = client.tasks.create(
            contact_id="66e34b81740c50074e3d1bd4",
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ApolloSDK) -> None:
        task = client.tasks.create(
            contact_id="66e34b81740c50074e3d1bd4",
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
            note="Discuss product demo results and next steps.",
            priority="high",
            title="Follow-up call",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ApolloSDK) -> None:
        response = client.tasks.with_raw_response.create(
            contact_id="66e34b81740c50074e3d1bd4",
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ApolloSDK) -> None:
        with client.tasks.with_streaming_response.create(
            contact_id="66e34b81740c50074e3d1bd4",
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_bulk_create(self, client: ApolloSDK) -> None:
        task = client.tasks.bulk_create(
            contact_ids=["66e34b81740c50074e3d1bd4", "66e34b81740c50074e3d1bd5", "66e34b81740c50074e3d1bd6"],
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
        )
        assert_matches_type(TaskBulkCreateResponse, task, path=["response"])

    @parametrize
    def test_method_bulk_create_with_all_params(self, client: ApolloSDK) -> None:
        task = client.tasks.bulk_create(
            contact_ids=["66e34b81740c50074e3d1bd4", "66e34b81740c50074e3d1bd5", "66e34b81740c50074e3d1bd6"],
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
            note="Follow up on demo request.",
            priority="high",
        )
        assert_matches_type(TaskBulkCreateResponse, task, path=["response"])

    @parametrize
    def test_raw_response_bulk_create(self, client: ApolloSDK) -> None:
        response = client.tasks.with_raw_response.bulk_create(
            contact_ids=["66e34b81740c50074e3d1bd4", "66e34b81740c50074e3d1bd5", "66e34b81740c50074e3d1bd6"],
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskBulkCreateResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_bulk_create(self, client: ApolloSDK) -> None:
        with client.tasks.with_streaming_response.bulk_create(
            contact_ids=["66e34b81740c50074e3d1bd4", "66e34b81740c50074e3d1bd5", "66e34b81740c50074e3d1bd6"],
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskBulkCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: ApolloSDK) -> None:
        task = client.tasks.search()
        assert_matches_type(TaskSearchResponse, task, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: ApolloSDK) -> None:
        task = client.tasks.search(
            open_factor_names=["string"],
            page=0,
            per_page=0,
            sort_by_field="sort_by_field",
        )
        assert_matches_type(TaskSearchResponse, task, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: ApolloSDK) -> None:
        response = client.tasks.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskSearchResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: ApolloSDK) -> None:
        with client.tasks.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskSearchResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncApolloSDK) -> None:
        task = await async_client.tasks.create(
            contact_id="66e34b81740c50074e3d1bd4",
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        task = await async_client.tasks.create(
            contact_id="66e34b81740c50074e3d1bd4",
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
            note="Discuss product demo results and next steps.",
            priority="high",
            title="Follow-up call",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.tasks.with_raw_response.create(
            contact_id="66e34b81740c50074e3d1bd4",
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.tasks.with_streaming_response.create(
            contact_id="66e34b81740c50074e3d1bd4",
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncApolloSDK) -> None:
        task = await async_client.tasks.bulk_create(
            contact_ids=["66e34b81740c50074e3d1bd4", "66e34b81740c50074e3d1bd5", "66e34b81740c50074e3d1bd6"],
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
        )
        assert_matches_type(TaskBulkCreateResponse, task, path=["response"])

    @parametrize
    async def test_method_bulk_create_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        task = await async_client.tasks.bulk_create(
            contact_ids=["66e34b81740c50074e3d1bd4", "66e34b81740c50074e3d1bd5", "66e34b81740c50074e3d1bd6"],
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
            note="Follow up on demo request.",
            priority="high",
        )
        assert_matches_type(TaskBulkCreateResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.tasks.with_raw_response.bulk_create(
            contact_ids=["66e34b81740c50074e3d1bd4", "66e34b81740c50074e3d1bd5", "66e34b81740c50074e3d1bd6"],
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskBulkCreateResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.tasks.with_streaming_response.bulk_create(
            contact_ids=["66e34b81740c50074e3d1bd4", "66e34b81740c50074e3d1bd5", "66e34b81740c50074e3d1bd6"],
            due_at=parse_datetime("2025-02-15T10:00:00Z"),
            status="scheduled",
            type="call",
            user_id="66302798d03b9601c7934ebf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskBulkCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncApolloSDK) -> None:
        task = await async_client.tasks.search()
        assert_matches_type(TaskSearchResponse, task, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        task = await async_client.tasks.search(
            open_factor_names=["string"],
            page=0,
            per_page=0,
            sort_by_field="sort_by_field",
        )
        assert_matches_type(TaskSearchResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.tasks.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskSearchResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.tasks.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskSearchResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True
