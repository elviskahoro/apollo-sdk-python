# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from apollo import ApolloSDK, AsyncApolloSDK
from apollo.types import (
    ContactCreateResponse,
    ContactSearchResponse,
    ContactUpdateResponse,
    ContactRetrieveResponse,
    ContactBulkCreateResponse,
    ContactBulkUpdateResponse,
    ContactUpdateOwnersResponse,
    ContactUpdateStagesResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ApolloSDK) -> None:
        contact = client.contacts.create()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ApolloSDK) -> None:
        contact = client.contacts.create(
            account_id="account_id",
            contact_stage_id="contact_stage_id",
            corporate_phone="corporate_phone",
            direct_phone="direct_phone",
            email="john.smith@example.com",
            first_name="John",
            home_phone="home_phone",
            label_names=["string"],
            last_name="Smith",
            mobile_phone="mobile_phone",
            organization_name="Example Corp",
            other_phone="other_phone",
            present_raw_address="present_raw_address",
            run_dedupe=True,
            title="Software Engineer",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
            website_url="website_url",
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ApolloSDK) -> None:
        response = client.contacts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ApolloSDK) -> None:
        with client.contacts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ApolloSDK) -> None:
        contact = client.contacts.retrieve(
            "contact_id",
        )
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ApolloSDK) -> None:
        response = client.contacts.with_raw_response.retrieve(
            "contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ApolloSDK) -> None:
        with client.contacts.with_streaming_response.retrieve(
            "contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ApolloSDK) -> None:
        contact = client.contacts.update(
            contact_id="contact_id",
        )
        assert_matches_type(ContactUpdateResponse, contact, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ApolloSDK) -> None:
        contact = client.contacts.update(
            contact_id="contact_id",
            account_id="account_id",
            contact_stage_id="contact_stage_id",
            corporate_phone="corporate_phone",
            direct_phone="direct_phone",
            email="email",
            first_name="first_name",
            home_phone="home_phone",
            label_names=["string"],
            last_name="last_name",
            mobile_phone="mobile_phone",
            organization_name="organization_name",
            other_phone="other_phone",
            present_raw_address="present_raw_address",
            title="title",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
            website_url="website_url",
        )
        assert_matches_type(ContactUpdateResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ApolloSDK) -> None:
        response = client.contacts.with_raw_response.update(
            contact_id="contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactUpdateResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ApolloSDK) -> None:
        with client.contacts.with_streaming_response.update(
            contact_id="contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactUpdateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.with_raw_response.update(
                contact_id="",
            )

    @parametrize
    def test_method_bulk_create(self, client: ApolloSDK) -> None:
        contact = client.contacts.bulk_create(
            contacts=[{}, {}],
        )
        assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

    @parametrize
    def test_method_bulk_create_with_all_params(self, client: ApolloSDK) -> None:
        contact = client.contacts.bulk_create(
            contacts=[
                {
                    "account_id": "507f1f77bcf86cd799439011",
                    "contact_emails": [
                        {
                            "email": "john.doe@example.com",
                            "position": 0,
                        }
                    ],
                    "contact_role_type_ids": ["507f1f77bcf86cd799439020"],
                    "contact_stage_id": "507f1f77bcf86cd799439014",
                    "email": "john.doe@example.com",
                    "facebook_url": "https://www.facebook.com/johndoe",
                    "first_name": "John",
                    "hubspot_id": "12345678",
                    "last_name": "Doe",
                    "linkedin_url": "https://www.linkedin.com/in/johndoe",
                    "organization_id": "507f1f77bcf86cd799439012",
                    "organization_name": "Acme Corporation",
                    "outreach_id": "98765",
                    "owner_id": "507f1f77bcf86cd799439013",
                    "phone": "+1-555-0100",
                    "phone_numbers": [
                        {
                            "position": 0,
                            "raw_number": "+1-555-0100",
                        }
                    ],
                    "phone_status_cd": "phone_status_cd",
                    "photo_url": "https://example.com/photo.jpg",
                    "present_raw_address": "San Francisco, CA",
                    "primary_title": "VP of Sales",
                    "salesforce_account_id": "001xx000003DGb2AAG",
                    "salesforce_contact_id": "003xx000004TmiQAAS",
                    "salesforce_id": "003xx000004TmiQAAS",
                    "salesforce_lead_id": "00Qxx000001abcDEFG",
                    "salesloft_id": "54321",
                    "title": "Senior Manager",
                    "twitter_url": "https://twitter.com/johndoe",
                    "typed_custom_fields": {"60c39ed82bd02f01154c470a": "2025-08-07"},
                },
                {
                    "account_id": "507f1f77bcf86cd799439011",
                    "contact_emails": [
                        {
                            "email": "john.doe@example.com",
                            "position": 0,
                        }
                    ],
                    "contact_role_type_ids": ["507f1f77bcf86cd799439020"],
                    "contact_stage_id": "507f1f77bcf86cd799439014",
                    "email": "jane.smith@techstart.io",
                    "facebook_url": "https://www.facebook.com/johndoe",
                    "first_name": "Jane",
                    "hubspot_id": "12345678",
                    "last_name": "Smith",
                    "linkedin_url": "https://www.linkedin.com/in/janesmith",
                    "organization_id": "507f1f77bcf86cd799439012",
                    "organization_name": "TechStart Inc",
                    "outreach_id": "98765",
                    "owner_id": "507f1f77bcf86cd799439013",
                    "phone": "+1-555-0100",
                    "phone_numbers": [
                        {
                            "position": 0,
                            "raw_number": "+1-555-0100",
                        }
                    ],
                    "phone_status_cd": "phone_status_cd",
                    "photo_url": "https://example.com/photo.jpg",
                    "present_raw_address": "San Francisco, CA",
                    "primary_title": "VP of Sales",
                    "salesforce_account_id": "001xx000003DGb2AAG",
                    "salesforce_contact_id": "003xx000004TmiQAAS",
                    "salesforce_id": "003xx000004TmiQAAS",
                    "salesforce_lead_id": "00Qxx000001abcDEFG",
                    "salesloft_id": "54321",
                    "title": "VP of Sales",
                    "twitter_url": "https://twitter.com/johndoe",
                    "typed_custom_fields": {"60c39ed82bd02f01154c470a": "2025-08-07"},
                },
            ],
            append_label_names=["Hot Lead", "Q1 2024"],
            run_dedupe=True,
        )
        assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_bulk_create(self, client: ApolloSDK) -> None:
        response = client.contacts.with_raw_response.bulk_create(
            contacts=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_bulk_create(self, client: ApolloSDK) -> None:
        with client.contacts.with_streaming_response.bulk_create(
            contacts=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_bulk_update(self, client: ApolloSDK) -> None:
        contact = client.contacts.bulk_update()
        assert_matches_type(ContactBulkUpdateResponse, contact, path=["response"])

    @parametrize
    def test_method_bulk_update_with_all_params(self, client: ApolloSDK) -> None:
        contact = client.contacts.bulk_update(
            account_id="63f53afe4ceeca00016bdd2f",
            async_=False,
            contact_attributes=[
                {
                    "id": "66e34b81740c50074e3d1bd4",
                    "account_id": "63f53afe4ceeca00016bdd2f",
                    "email": "john.doe@example.com",
                    "first_name": "John",
                    "last_name": "Doe",
                    "linkedin_url": "https://www.linkedin.com/in/johndoe",
                    "organization_name": "Example Corp",
                    "owner_id": "66302798d03b9601c7934ebf",
                    "present_raw_address": "San Francisco, CA",
                    "title": "Senior Manager",
                    "typed_custom_fields": {"60c39ed82bd02f01154c470a": "2025-08-07"},
                }
            ],
            contact_ids=["66e34b81740c50074e3d1bd4", "66e370fbf5f5c003f0e1d0cf"],
            email="updated@example.com",
            first_name="Updated",
            last_name="Name",
            linkedin_url="https://www.linkedin.com/in/updated",
            organization_name="Updated Corp",
            owner_id="66302798d03b9601c7934ebf",
            present_raw_address="New York, NY",
            title="Updated Title",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
            visible_entity_ids=["66e34b81740c50074e3d1bd4"],
        )
        assert_matches_type(ContactBulkUpdateResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_bulk_update(self, client: ApolloSDK) -> None:
        response = client.contacts.with_raw_response.bulk_update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactBulkUpdateResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_bulk_update(self, client: ApolloSDK) -> None:
        with client.contacts.with_streaming_response.bulk_update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactBulkUpdateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: ApolloSDK) -> None:
        contact = client.contacts.search()
        assert_matches_type(ContactSearchResponse, contact, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: ApolloSDK) -> None:
        contact = client.contacts.search(
            contact_label_ids=["string"],
            contact_stage_ids=["string"],
            page=0,
            per_page=0,
            q_keywords="q_keywords",
            sort_ascending=True,
            sort_by_field="sort_by_field",
        )
        assert_matches_type(ContactSearchResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: ApolloSDK) -> None:
        response = client.contacts.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactSearchResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: ApolloSDK) -> None:
        with client.contacts.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactSearchResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_owners(self, client: ApolloSDK) -> None:
        contact = client.contacts.update_owners(
            contact_ids=["string"],
            owner_id="owner_id",
        )
        assert_matches_type(ContactUpdateOwnersResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_update_owners(self, client: ApolloSDK) -> None:
        response = client.contacts.with_raw_response.update_owners(
            contact_ids=["string"],
            owner_id="owner_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactUpdateOwnersResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_update_owners(self, client: ApolloSDK) -> None:
        with client.contacts.with_streaming_response.update_owners(
            contact_ids=["string"],
            owner_id="owner_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactUpdateOwnersResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_stages(self, client: ApolloSDK) -> None:
        contact = client.contacts.update_stages(
            contact_ids=["string"],
            contact_stage_id="contact_stage_id",
        )
        assert_matches_type(ContactUpdateStagesResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_update_stages(self, client: ApolloSDK) -> None:
        response = client.contacts.with_raw_response.update_stages(
            contact_ids=["string"],
            contact_stage_id="contact_stage_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactUpdateStagesResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_update_stages(self, client: ApolloSDK) -> None:
        with client.contacts.with_streaming_response.update_stages(
            contact_ids=["string"],
            contact_stage_id="contact_stage_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactUpdateStagesResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.create()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.create(
            account_id="account_id",
            contact_stage_id="contact_stage_id",
            corporate_phone="corporate_phone",
            direct_phone="direct_phone",
            email="john.smith@example.com",
            first_name="John",
            home_phone="home_phone",
            label_names=["string"],
            last_name="Smith",
            mobile_phone="mobile_phone",
            organization_name="Example Corp",
            other_phone="other_phone",
            present_raw_address="present_raw_address",
            run_dedupe=True,
            title="Software Engineer",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
            website_url="website_url",
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.contacts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.contacts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.retrieve(
            "contact_id",
        )
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.contacts.with_raw_response.retrieve(
            "contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.contacts.with_streaming_response.retrieve(
            "contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.update(
            contact_id="contact_id",
        )
        assert_matches_type(ContactUpdateResponse, contact, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.update(
            contact_id="contact_id",
            account_id="account_id",
            contact_stage_id="contact_stage_id",
            corporate_phone="corporate_phone",
            direct_phone="direct_phone",
            email="email",
            first_name="first_name",
            home_phone="home_phone",
            label_names=["string"],
            last_name="last_name",
            mobile_phone="mobile_phone",
            organization_name="organization_name",
            other_phone="other_phone",
            present_raw_address="present_raw_address",
            title="title",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
            website_url="website_url",
        )
        assert_matches_type(ContactUpdateResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.contacts.with_raw_response.update(
            contact_id="contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactUpdateResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.contacts.with_streaming_response.update(
            contact_id="contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactUpdateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.with_raw_response.update(
                contact_id="",
            )

    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.bulk_create(
            contacts=[{}, {}],
        )
        assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

    @parametrize
    async def test_method_bulk_create_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.bulk_create(
            contacts=[
                {
                    "account_id": "507f1f77bcf86cd799439011",
                    "contact_emails": [
                        {
                            "email": "john.doe@example.com",
                            "position": 0,
                        }
                    ],
                    "contact_role_type_ids": ["507f1f77bcf86cd799439020"],
                    "contact_stage_id": "507f1f77bcf86cd799439014",
                    "email": "john.doe@example.com",
                    "facebook_url": "https://www.facebook.com/johndoe",
                    "first_name": "John",
                    "hubspot_id": "12345678",
                    "last_name": "Doe",
                    "linkedin_url": "https://www.linkedin.com/in/johndoe",
                    "organization_id": "507f1f77bcf86cd799439012",
                    "organization_name": "Acme Corporation",
                    "outreach_id": "98765",
                    "owner_id": "507f1f77bcf86cd799439013",
                    "phone": "+1-555-0100",
                    "phone_numbers": [
                        {
                            "position": 0,
                            "raw_number": "+1-555-0100",
                        }
                    ],
                    "phone_status_cd": "phone_status_cd",
                    "photo_url": "https://example.com/photo.jpg",
                    "present_raw_address": "San Francisco, CA",
                    "primary_title": "VP of Sales",
                    "salesforce_account_id": "001xx000003DGb2AAG",
                    "salesforce_contact_id": "003xx000004TmiQAAS",
                    "salesforce_id": "003xx000004TmiQAAS",
                    "salesforce_lead_id": "00Qxx000001abcDEFG",
                    "salesloft_id": "54321",
                    "title": "Senior Manager",
                    "twitter_url": "https://twitter.com/johndoe",
                    "typed_custom_fields": {"60c39ed82bd02f01154c470a": "2025-08-07"},
                },
                {
                    "account_id": "507f1f77bcf86cd799439011",
                    "contact_emails": [
                        {
                            "email": "john.doe@example.com",
                            "position": 0,
                        }
                    ],
                    "contact_role_type_ids": ["507f1f77bcf86cd799439020"],
                    "contact_stage_id": "507f1f77bcf86cd799439014",
                    "email": "jane.smith@techstart.io",
                    "facebook_url": "https://www.facebook.com/johndoe",
                    "first_name": "Jane",
                    "hubspot_id": "12345678",
                    "last_name": "Smith",
                    "linkedin_url": "https://www.linkedin.com/in/janesmith",
                    "organization_id": "507f1f77bcf86cd799439012",
                    "organization_name": "TechStart Inc",
                    "outreach_id": "98765",
                    "owner_id": "507f1f77bcf86cd799439013",
                    "phone": "+1-555-0100",
                    "phone_numbers": [
                        {
                            "position": 0,
                            "raw_number": "+1-555-0100",
                        }
                    ],
                    "phone_status_cd": "phone_status_cd",
                    "photo_url": "https://example.com/photo.jpg",
                    "present_raw_address": "San Francisco, CA",
                    "primary_title": "VP of Sales",
                    "salesforce_account_id": "001xx000003DGb2AAG",
                    "salesforce_contact_id": "003xx000004TmiQAAS",
                    "salesforce_id": "003xx000004TmiQAAS",
                    "salesforce_lead_id": "00Qxx000001abcDEFG",
                    "salesloft_id": "54321",
                    "title": "VP of Sales",
                    "twitter_url": "https://twitter.com/johndoe",
                    "typed_custom_fields": {"60c39ed82bd02f01154c470a": "2025-08-07"},
                },
            ],
            append_label_names=["Hot Lead", "Q1 2024"],
            run_dedupe=True,
        )
        assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.contacts.with_raw_response.bulk_create(
            contacts=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.contacts.with_streaming_response.bulk_create(
            contacts=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.bulk_update()
        assert_matches_type(ContactBulkUpdateResponse, contact, path=["response"])

    @parametrize
    async def test_method_bulk_update_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.bulk_update(
            account_id="63f53afe4ceeca00016bdd2f",
            async_=False,
            contact_attributes=[
                {
                    "id": "66e34b81740c50074e3d1bd4",
                    "account_id": "63f53afe4ceeca00016bdd2f",
                    "email": "john.doe@example.com",
                    "first_name": "John",
                    "last_name": "Doe",
                    "linkedin_url": "https://www.linkedin.com/in/johndoe",
                    "organization_name": "Example Corp",
                    "owner_id": "66302798d03b9601c7934ebf",
                    "present_raw_address": "San Francisco, CA",
                    "title": "Senior Manager",
                    "typed_custom_fields": {"60c39ed82bd02f01154c470a": "2025-08-07"},
                }
            ],
            contact_ids=["66e34b81740c50074e3d1bd4", "66e370fbf5f5c003f0e1d0cf"],
            email="updated@example.com",
            first_name="Updated",
            last_name="Name",
            linkedin_url="https://www.linkedin.com/in/updated",
            organization_name="Updated Corp",
            owner_id="66302798d03b9601c7934ebf",
            present_raw_address="New York, NY",
            title="Updated Title",
            typed_custom_fields={"60c39ed82bd02f01154c470a": "2025-08-07"},
            visible_entity_ids=["66e34b81740c50074e3d1bd4"],
        )
        assert_matches_type(ContactBulkUpdateResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.contacts.with_raw_response.bulk_update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactBulkUpdateResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.contacts.with_streaming_response.bulk_update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactBulkUpdateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.search()
        assert_matches_type(ContactSearchResponse, contact, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.search(
            contact_label_ids=["string"],
            contact_stage_ids=["string"],
            page=0,
            per_page=0,
            q_keywords="q_keywords",
            sort_ascending=True,
            sort_by_field="sort_by_field",
        )
        assert_matches_type(ContactSearchResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.contacts.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactSearchResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.contacts.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactSearchResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_owners(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.update_owners(
            contact_ids=["string"],
            owner_id="owner_id",
        )
        assert_matches_type(ContactUpdateOwnersResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_update_owners(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.contacts.with_raw_response.update_owners(
            contact_ids=["string"],
            owner_id="owner_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactUpdateOwnersResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_update_owners(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.contacts.with_streaming_response.update_owners(
            contact_ids=["string"],
            owner_id="owner_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactUpdateOwnersResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_stages(self, async_client: AsyncApolloSDK) -> None:
        contact = await async_client.contacts.update_stages(
            contact_ids=["string"],
            contact_stage_id="contact_stage_id",
        )
        assert_matches_type(ContactUpdateStagesResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_update_stages(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.contacts.with_raw_response.update_stages(
            contact_ids=["string"],
            contact_stage_id="contact_stage_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactUpdateStagesResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_update_stages(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.contacts.with_streaming_response.update_stages(
            contact_ids=["string"],
            contact_stage_id="contact_stage_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactUpdateStagesResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True
