# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from apollo import ApolloSDK, AsyncApolloSDK
from apollo._utils import parse_date, parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ApolloSDK) -> None:
        phone_call = client.phone_calls.create()
        assert phone_call is None

    @parametrize
    def test_method_create_with_all_params(self, client: ApolloSDK) -> None:
        phone_call = client.phone_calls.create(
            account_id="account_id",
            contact_id="contact_id",
            duration=0,
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            from_number="from_number",
            logged=True,
            note="note",
            phone_call_outcome_id="phone_call_outcome_id",
            phone_call_purpose_id="phone_call_purpose_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="status",
            to_number="to_number",
            user_id=["string"],
        )
        assert phone_call is None

    @parametrize
    def test_raw_response_create(self, client: ApolloSDK) -> None:
        response = client.phone_calls.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_call = response.parse()
        assert phone_call is None

    @parametrize
    def test_streaming_response_create(self, client: ApolloSDK) -> None:
        with client.phone_calls.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_call = response.parse()
            assert phone_call is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: ApolloSDK) -> None:
        phone_call = client.phone_calls.update(
            id="id",
        )
        assert phone_call is None

    @parametrize
    def test_method_update_with_all_params(self, client: ApolloSDK) -> None:
        phone_call = client.phone_calls.update(
            id="id",
            account_id="account_id",
            contact_id="contact_id",
            duration=0,
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            from_number="from_number",
            logged=True,
            note="note",
            phone_call_outcome_id="phone_call_outcome_id",
            phone_call_purpose_id="phone_call_purpose_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="status",
            to_number="to_number",
            user_id=["string"],
        )
        assert phone_call is None

    @parametrize
    def test_raw_response_update(self, client: ApolloSDK) -> None:
        response = client.phone_calls.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_call = response.parse()
        assert phone_call is None

    @parametrize
    def test_streaming_response_update(self, client: ApolloSDK) -> None:
        with client.phone_calls.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_call = response.parse()
            assert phone_call is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.phone_calls.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_search(self, client: ApolloSDK) -> None:
        phone_call = client.phone_calls.search()
        assert phone_call is None

    @parametrize
    def test_method_search_with_all_params(self, client: ApolloSDK) -> None:
        phone_call = client.phone_calls.search(
            contact_label_ids=["string"],
            date_range_max=parse_date("2019-12-27"),
            date_range_min=parse_date("2019-12-27"),
            duration_max=0,
            duration_min=0,
            inbound="inbound",
            page="page",
            per_page="per_page",
            phone_call_outcome_ids=["string"],
            phone_call_purpose_ids=["string"],
            q_keywords="q_keywords",
            user_ids=["string"],
        )
        assert phone_call is None

    @parametrize
    def test_raw_response_search(self, client: ApolloSDK) -> None:
        response = client.phone_calls.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_call = response.parse()
        assert phone_call is None

    @parametrize
    def test_streaming_response_search(self, client: ApolloSDK) -> None:
        with client.phone_calls.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_call = response.parse()
            assert phone_call is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPhoneCalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncApolloSDK) -> None:
        phone_call = await async_client.phone_calls.create()
        assert phone_call is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        phone_call = await async_client.phone_calls.create(
            account_id="account_id",
            contact_id="contact_id",
            duration=0,
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            from_number="from_number",
            logged=True,
            note="note",
            phone_call_outcome_id="phone_call_outcome_id",
            phone_call_purpose_id="phone_call_purpose_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="status",
            to_number="to_number",
            user_id=["string"],
        )
        assert phone_call is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.phone_calls.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_call = await response.parse()
        assert phone_call is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.phone_calls.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_call = await response.parse()
            assert phone_call is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncApolloSDK) -> None:
        phone_call = await async_client.phone_calls.update(
            id="id",
        )
        assert phone_call is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        phone_call = await async_client.phone_calls.update(
            id="id",
            account_id="account_id",
            contact_id="contact_id",
            duration=0,
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            from_number="from_number",
            logged=True,
            note="note",
            phone_call_outcome_id="phone_call_outcome_id",
            phone_call_purpose_id="phone_call_purpose_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="status",
            to_number="to_number",
            user_id=["string"],
        )
        assert phone_call is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.phone_calls.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_call = await response.parse()
        assert phone_call is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.phone_calls.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_call = await response.parse()
            assert phone_call is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.phone_calls.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncApolloSDK) -> None:
        phone_call = await async_client.phone_calls.search()
        assert phone_call is None

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        phone_call = await async_client.phone_calls.search(
            contact_label_ids=["string"],
            date_range_max=parse_date("2019-12-27"),
            date_range_min=parse_date("2019-12-27"),
            duration_max=0,
            duration_min=0,
            inbound="inbound",
            page="page",
            per_page="per_page",
            phone_call_outcome_ids=["string"],
            phone_call_purpose_ids=["string"],
            q_keywords="q_keywords",
            user_ids=["string"],
        )
        assert phone_call is None

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.phone_calls.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_call = await response.parse()
        assert phone_call is None

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.phone_calls.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_call = await response.parse()
            assert phone_call is None

        assert cast(Any, response.is_closed) is True
