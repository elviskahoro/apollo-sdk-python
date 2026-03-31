# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from src import ApolloSDK, AsyncApolloSDK
from src.types import (
    AccountCreateResponse,
    AccountSearchResponse,
    AccountUpdateResponse,
    AccountRetrieveResponse,
    AccountBulkCreateResponse,
    AccountBulkUpdateResponse,
    AccountUpdateOwnersResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ApolloSDK) -> None:
        account = client.accounts.create()
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ApolloSDK) -> None:
        account = client.accounts.create(
            account_stage_id="account_stage_id",
            domain="domain",
            name="name",
            owner_id="owner_id",
            phone="phone",
            raw_address="raw_address",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ApolloSDK) -> None:
        response = client.accounts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ApolloSDK) -> None:
        with client.accounts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountCreateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ApolloSDK) -> None:
        account = client.accounts.retrieve(
            account_id="account_id",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ApolloSDK) -> None:
        response = client.accounts.with_raw_response.retrieve(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ApolloSDK) -> None:
        with client.accounts.with_streaming_response.retrieve(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.retrieve(
                account_id="",
            )

    @parametrize
    def test_method_update(self, client: ApolloSDK) -> None:
        account = client.accounts.update(
            account_id="account_id",
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ApolloSDK) -> None:
        account = client.accounts.update(
            account_id="account_id",
            account_stage_id="account_stage_id",
            domain="domain",
            name="name",
            owner_id="owner_id",
            phone="phone",
            raw_address="raw_address",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ApolloSDK) -> None:
        response = client.accounts.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ApolloSDK) -> None:
        with client.accounts.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountUpdateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.update(
                account_id="",
            )

    @parametrize
    def test_method_bulk_create(self, client: ApolloSDK) -> None:
        account = client.accounts.bulk_create(
            accounts=[{}, {}],
        )
        assert_matches_type(AccountBulkCreateResponse, account, path=["response"])

    @parametrize
    def test_method_bulk_create_with_all_params(self, client: ApolloSDK) -> None:
        account = client.accounts.bulk_create(
            accounts=[
                {
                    "account_stage_id": "507f1f77bcf86cd799439014",
                    "domain": "acme.com",
                    "facebook_url": "https://facebook.com/acme",
                    "hubspot_id": "12345678",
                    "linkedin_url": "https://linkedin.com/company/acme",
                    "merged_crm_ids": ["string"],
                    "name": "Acme Corporation",
                    "organization_id": "507f1f77bcf86cd799439012",
                    "owner_id": "507f1f77bcf86cd799439013",
                    "parent_account_id": "507f1f77bcf86cd799439016",
                    "phone": "+1-555-0100",
                    "phone_status_cd": "phone_status_cd",
                    "raw_address": "123 Main St, San Francisco, CA 94105",
                    "salesforce_id": "001xx000003DGb2AAG",
                    "twitter_url": "https://twitter.com/acme",
                    "typed_custom_fields": {
                        "507f1f77bcf86cd799439020": "High Value",
                        "507f1f77bcf86cd799439021": "Q4 2025",
                    },
                },
                {
                    "account_stage_id": "507f1f77bcf86cd799439014",
                    "domain": "techstart.io",
                    "facebook_url": "https://facebook.com/acme",
                    "hubspot_id": "12345678",
                    "linkedin_url": "https://linkedin.com/company/techstart",
                    "merged_crm_ids": ["string"],
                    "name": "TechStart Inc",
                    "organization_id": "507f1f77bcf86cd799439012",
                    "owner_id": "507f1f77bcf86cd799439013",
                    "parent_account_id": "507f1f77bcf86cd799439016",
                    "phone": "+1-555-0100",
                    "phone_status_cd": "phone_status_cd",
                    "raw_address": "123 Main St, San Francisco, CA 94105",
                    "salesforce_id": "001xx000003DGb2AAG",
                    "twitter_url": "https://twitter.com/acme",
                    "typed_custom_fields": {
                        "507f1f77bcf86cd799439020": "High Value",
                        "507f1f77bcf86cd799439021": "Q4 2025",
                    },
                },
            ],
            append_label_names=["Enterprise", "High Priority"],
            run_dedupe=True,
        )
        assert_matches_type(AccountBulkCreateResponse, account, path=["response"])

    @parametrize
    def test_raw_response_bulk_create(self, client: ApolloSDK) -> None:
        response = client.accounts.with_raw_response.bulk_create(
            accounts=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountBulkCreateResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_bulk_create(self, client: ApolloSDK) -> None:
        with client.accounts.with_streaming_response.bulk_create(
            accounts=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountBulkCreateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_bulk_update(self, client: ApolloSDK) -> None:
        account = client.accounts.bulk_update()
        assert_matches_type(AccountBulkUpdateResponse, account, path=["response"])

    @parametrize
    def test_method_bulk_update_with_all_params(self, client: ApolloSDK) -> None:
        account = client.accounts.bulk_update(
            account_attributes=[
                {
                    "id": "66e9abf95ac32901b20d1a0d",
                    "account_stage_id": "6095a710bd01d100a506d4b7",
                    "name": "Acme Corporation",
                    "owner_id": "66302798d03b9601c7934ebf",
                    "typed_custom_fields": {"60c39ed82bd02f01154c470a": "2025-08-07"},
                }
            ],
            account_ids=["66e9abf95ac32901b20d1a0d", "66e9a4db056fe802d331fb8a"],
            account_stage_id="6095a710bd01d100a506d4b7",
            async_=False,
            name="Updated Account Name",
            owner_id="66302798d03b9601c7934ebf",
        )
        assert_matches_type(AccountBulkUpdateResponse, account, path=["response"])

    @parametrize
    def test_raw_response_bulk_update(self, client: ApolloSDK) -> None:
        response = client.accounts.with_raw_response.bulk_update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountBulkUpdateResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_bulk_update(self, client: ApolloSDK) -> None:
        with client.accounts.with_streaming_response.bulk_update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountBulkUpdateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: ApolloSDK) -> None:
        account = client.accounts.search()
        assert_matches_type(AccountSearchResponse, account, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: ApolloSDK) -> None:
        account = client.accounts.search(
            account_label_ids=["string"],
            account_stage_ids=["string"],
            page=0,
            per_page=0,
            q_organization_name="q_organization_name",
            sort_ascending=True,
            sort_by_field="account_last_activity_date",
        )
        assert_matches_type(AccountSearchResponse, account, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: ApolloSDK) -> None:
        response = client.accounts.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountSearchResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: ApolloSDK) -> None:
        with client.accounts.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountSearchResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_owners(self, client: ApolloSDK) -> None:
        account = client.accounts.update_owners(
            account_ids=["string"],
            owner_id="owner_id",
        )
        assert_matches_type(AccountUpdateOwnersResponse, account, path=["response"])

    @parametrize
    def test_raw_response_update_owners(self, client: ApolloSDK) -> None:
        response = client.accounts.with_raw_response.update_owners(
            account_ids=["string"],
            owner_id="owner_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountUpdateOwnersResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_update_owners(self, client: ApolloSDK) -> None:
        with client.accounts.with_streaming_response.update_owners(
            account_ids=["string"],
            owner_id="owner_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountUpdateOwnersResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncApolloSDK) -> None:
        account = await async_client.accounts.create()
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        account = await async_client.accounts.create(
            account_stage_id="account_stage_id",
            domain="domain",
            name="name",
            owner_id="owner_id",
            phone="phone",
            raw_address="raw_address",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.accounts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.accounts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountCreateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncApolloSDK) -> None:
        account = await async_client.accounts.retrieve(
            account_id="account_id",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.accounts.with_raw_response.retrieve(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.accounts.with_streaming_response.retrieve(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve(
                account_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncApolloSDK) -> None:
        account = await async_client.accounts.update(
            account_id="account_id",
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        account = await async_client.accounts.update(
            account_id="account_id",
            account_stage_id="account_stage_id",
            domain="domain",
            name="name",
            owner_id="owner_id",
            phone="phone",
            raw_address="raw_address",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.accounts.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.accounts.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountUpdateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.update(
                account_id="",
            )

    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncApolloSDK) -> None:
        account = await async_client.accounts.bulk_create(
            accounts=[{}, {}],
        )
        assert_matches_type(AccountBulkCreateResponse, account, path=["response"])

    @parametrize
    async def test_method_bulk_create_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        account = await async_client.accounts.bulk_create(
            accounts=[
                {
                    "account_stage_id": "507f1f77bcf86cd799439014",
                    "domain": "acme.com",
                    "facebook_url": "https://facebook.com/acme",
                    "hubspot_id": "12345678",
                    "linkedin_url": "https://linkedin.com/company/acme",
                    "merged_crm_ids": ["string"],
                    "name": "Acme Corporation",
                    "organization_id": "507f1f77bcf86cd799439012",
                    "owner_id": "507f1f77bcf86cd799439013",
                    "parent_account_id": "507f1f77bcf86cd799439016",
                    "phone": "+1-555-0100",
                    "phone_status_cd": "phone_status_cd",
                    "raw_address": "123 Main St, San Francisco, CA 94105",
                    "salesforce_id": "001xx000003DGb2AAG",
                    "twitter_url": "https://twitter.com/acme",
                    "typed_custom_fields": {
                        "507f1f77bcf86cd799439020": "High Value",
                        "507f1f77bcf86cd799439021": "Q4 2025",
                    },
                },
                {
                    "account_stage_id": "507f1f77bcf86cd799439014",
                    "domain": "techstart.io",
                    "facebook_url": "https://facebook.com/acme",
                    "hubspot_id": "12345678",
                    "linkedin_url": "https://linkedin.com/company/techstart",
                    "merged_crm_ids": ["string"],
                    "name": "TechStart Inc",
                    "organization_id": "507f1f77bcf86cd799439012",
                    "owner_id": "507f1f77bcf86cd799439013",
                    "parent_account_id": "507f1f77bcf86cd799439016",
                    "phone": "+1-555-0100",
                    "phone_status_cd": "phone_status_cd",
                    "raw_address": "123 Main St, San Francisco, CA 94105",
                    "salesforce_id": "001xx000003DGb2AAG",
                    "twitter_url": "https://twitter.com/acme",
                    "typed_custom_fields": {
                        "507f1f77bcf86cd799439020": "High Value",
                        "507f1f77bcf86cd799439021": "Q4 2025",
                    },
                },
            ],
            append_label_names=["Enterprise", "High Priority"],
            run_dedupe=True,
        )
        assert_matches_type(AccountBulkCreateResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.accounts.with_raw_response.bulk_create(
            accounts=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountBulkCreateResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.accounts.with_streaming_response.bulk_create(
            accounts=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountBulkCreateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncApolloSDK) -> None:
        account = await async_client.accounts.bulk_update()
        assert_matches_type(AccountBulkUpdateResponse, account, path=["response"])

    @parametrize
    async def test_method_bulk_update_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        account = await async_client.accounts.bulk_update(
            account_attributes=[
                {
                    "id": "66e9abf95ac32901b20d1a0d",
                    "account_stage_id": "6095a710bd01d100a506d4b7",
                    "name": "Acme Corporation",
                    "owner_id": "66302798d03b9601c7934ebf",
                    "typed_custom_fields": {"60c39ed82bd02f01154c470a": "2025-08-07"},
                }
            ],
            account_ids=["66e9abf95ac32901b20d1a0d", "66e9a4db056fe802d331fb8a"],
            account_stage_id="6095a710bd01d100a506d4b7",
            async_=False,
            name="Updated Account Name",
            owner_id="66302798d03b9601c7934ebf",
        )
        assert_matches_type(AccountBulkUpdateResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.accounts.with_raw_response.bulk_update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountBulkUpdateResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.accounts.with_streaming_response.bulk_update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountBulkUpdateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncApolloSDK) -> None:
        account = await async_client.accounts.search()
        assert_matches_type(AccountSearchResponse, account, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        account = await async_client.accounts.search(
            account_label_ids=["string"],
            account_stage_ids=["string"],
            page=0,
            per_page=0,
            q_organization_name="q_organization_name",
            sort_ascending=True,
            sort_by_field="account_last_activity_date",
        )
        assert_matches_type(AccountSearchResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.accounts.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountSearchResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.accounts.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountSearchResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_owners(self, async_client: AsyncApolloSDK) -> None:
        account = await async_client.accounts.update_owners(
            account_ids=["string"],
            owner_id="owner_id",
        )
        assert_matches_type(AccountUpdateOwnersResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_update_owners(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.accounts.with_raw_response.update_owners(
            account_ids=["string"],
            owner_id="owner_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountUpdateOwnersResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_update_owners(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.accounts.with_streaming_response.update_owners(
            account_ids=["string"],
            owner_id="owner_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountUpdateOwnersResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
