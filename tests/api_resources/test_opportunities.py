# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from apollo_sdk import ApolloSDK, AsyncApolloSDK
from tests.utils import assert_matches_type
from apollo_sdk.types import (
    OpportunityListResponse,
    OpportunityCreateResponse,
    OpportunityUpdateResponse,
    OpportunityRetrieveResponse,
)
from apollo_sdk._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOpportunities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ApolloSDK) -> None:
        opportunity = client.opportunities.create(
            name="name",
        )
        assert_matches_type(OpportunityCreateResponse, opportunity, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ApolloSDK) -> None:
        opportunity = client.opportunities.create(
            name="name",
            account_id="account_id",
            amount="amount",
            closed_date=parse_date("2019-12-27"),
            opportunity_stage_id="opportunity_stage_id",
            owner_id="owner_id",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
        )
        assert_matches_type(OpportunityCreateResponse, opportunity, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ApolloSDK) -> None:
        response = client.opportunities.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opportunity = response.parse()
        assert_matches_type(OpportunityCreateResponse, opportunity, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ApolloSDK) -> None:
        with client.opportunities.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opportunity = response.parse()
            assert_matches_type(OpportunityCreateResponse, opportunity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ApolloSDK) -> None:
        opportunity = client.opportunities.retrieve(
            "opportunity_id",
        )
        assert_matches_type(OpportunityRetrieveResponse, opportunity, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ApolloSDK) -> None:
        response = client.opportunities.with_raw_response.retrieve(
            "opportunity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opportunity = response.parse()
        assert_matches_type(OpportunityRetrieveResponse, opportunity, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ApolloSDK) -> None:
        with client.opportunities.with_streaming_response.retrieve(
            "opportunity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opportunity = response.parse()
            assert_matches_type(OpportunityRetrieveResponse, opportunity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `opportunity_id` but received ''"):
            client.opportunities.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ApolloSDK) -> None:
        opportunity = client.opportunities.update(
            opportunity_id="opportunity_id",
        )
        assert_matches_type(OpportunityUpdateResponse, opportunity, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ApolloSDK) -> None:
        opportunity = client.opportunities.update(
            opportunity_id="opportunity_id",
            amount="amount",
            closed_date=parse_date("2019-12-27"),
            name="name",
            opportunity_stage_id="opportunity_stage_id",
            owner_id="owner_id",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
        )
        assert_matches_type(OpportunityUpdateResponse, opportunity, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ApolloSDK) -> None:
        response = client.opportunities.with_raw_response.update(
            opportunity_id="opportunity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opportunity = response.parse()
        assert_matches_type(OpportunityUpdateResponse, opportunity, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ApolloSDK) -> None:
        with client.opportunities.with_streaming_response.update(
            opportunity_id="opportunity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opportunity = response.parse()
            assert_matches_type(OpportunityUpdateResponse, opportunity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `opportunity_id` but received ''"):
            client.opportunities.with_raw_response.update(
                opportunity_id="",
            )

    @parametrize
    def test_method_list(self, client: ApolloSDK) -> None:
        opportunity = client.opportunities.list()
        assert_matches_type(OpportunityListResponse, opportunity, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ApolloSDK) -> None:
        opportunity = client.opportunities.list(
            page=0,
            per_page=0,
            sort_by_field="sort_by_field",
        )
        assert_matches_type(OpportunityListResponse, opportunity, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ApolloSDK) -> None:
        response = client.opportunities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opportunity = response.parse()
        assert_matches_type(OpportunityListResponse, opportunity, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ApolloSDK) -> None:
        with client.opportunities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opportunity = response.parse()
            assert_matches_type(OpportunityListResponse, opportunity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOpportunities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncApolloSDK) -> None:
        opportunity = await async_client.opportunities.create(
            name="name",
        )
        assert_matches_type(OpportunityCreateResponse, opportunity, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        opportunity = await async_client.opportunities.create(
            name="name",
            account_id="account_id",
            amount="amount",
            closed_date=parse_date("2019-12-27"),
            opportunity_stage_id="opportunity_stage_id",
            owner_id="owner_id",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
        )
        assert_matches_type(OpportunityCreateResponse, opportunity, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.opportunities.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opportunity = await response.parse()
        assert_matches_type(OpportunityCreateResponse, opportunity, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.opportunities.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opportunity = await response.parse()
            assert_matches_type(OpportunityCreateResponse, opportunity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncApolloSDK) -> None:
        opportunity = await async_client.opportunities.retrieve(
            "opportunity_id",
        )
        assert_matches_type(OpportunityRetrieveResponse, opportunity, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.opportunities.with_raw_response.retrieve(
            "opportunity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opportunity = await response.parse()
        assert_matches_type(OpportunityRetrieveResponse, opportunity, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.opportunities.with_streaming_response.retrieve(
            "opportunity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opportunity = await response.parse()
            assert_matches_type(OpportunityRetrieveResponse, opportunity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `opportunity_id` but received ''"):
            await async_client.opportunities.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncApolloSDK) -> None:
        opportunity = await async_client.opportunities.update(
            opportunity_id="opportunity_id",
        )
        assert_matches_type(OpportunityUpdateResponse, opportunity, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        opportunity = await async_client.opportunities.update(
            opportunity_id="opportunity_id",
            amount="amount",
            closed_date=parse_date("2019-12-27"),
            name="name",
            opportunity_stage_id="opportunity_stage_id",
            owner_id="owner_id",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
        )
        assert_matches_type(OpportunityUpdateResponse, opportunity, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.opportunities.with_raw_response.update(
            opportunity_id="opportunity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opportunity = await response.parse()
        assert_matches_type(OpportunityUpdateResponse, opportunity, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.opportunities.with_streaming_response.update(
            opportunity_id="opportunity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opportunity = await response.parse()
            assert_matches_type(OpportunityUpdateResponse, opportunity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `opportunity_id` but received ''"):
            await async_client.opportunities.with_raw_response.update(
                opportunity_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncApolloSDK) -> None:
        opportunity = await async_client.opportunities.list()
        assert_matches_type(OpportunityListResponse, opportunity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        opportunity = await async_client.opportunities.list(
            page=0,
            per_page=0,
            sort_by_field="sort_by_field",
        )
        assert_matches_type(OpportunityListResponse, opportunity, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.opportunities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opportunity = await response.parse()
        assert_matches_type(OpportunityListResponse, opportunity, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.opportunities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opportunity = await response.parse()
            assert_matches_type(OpportunityListResponse, opportunity, path=["response"])

        assert cast(Any, response.is_closed) is True
