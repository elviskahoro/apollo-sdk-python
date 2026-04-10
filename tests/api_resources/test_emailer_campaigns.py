# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from apollo import ApolloSDK, AsyncApolloSDK
from tests.utils import assert_matches_type
from apollo.types import (
    EmailerCampaignSearchResponse,
    EmailerCampaignArchiveResponse,
    EmailerCampaignActivateResponse,
    EmailerCampaignDeactivateResponse,
    EmailerCampaignAddContactsResponse,
    EmailerCampaignUpdateContactStatusResponse,
)
from apollo._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailerCampaigns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_activate(self, client: ApolloSDK) -> None:
        emailer_campaign = client.emailer_campaigns.activate(
            "sequence_id",
        )
        assert_matches_type(EmailerCampaignActivateResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_raw_response_activate(self, client: ApolloSDK) -> None:
        response = client.emailer_campaigns.with_raw_response.activate(
            "sequence_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emailer_campaign = response.parse()
        assert_matches_type(EmailerCampaignActivateResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_streaming_response_activate(self, client: ApolloSDK) -> None:
        with client.emailer_campaigns.with_streaming_response.activate(
            "sequence_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emailer_campaign = response.parse()
            assert_matches_type(EmailerCampaignActivateResponse, emailer_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_activate(self, client: ApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sequence_id` but received ''"):
            client.emailer_campaigns.with_raw_response.activate(
                "",
            )

    @parametrize
    def test_method_add_contacts(self, client: ApolloSDK) -> None:
        emailer_campaign = client.emailer_campaigns.add_contacts(
            sequence_id="sequence_id",
            emailer_campaign_id="emailer_campaign_id",
            send_email_from_email_account_id="send_email_from_email_account_id",
        )
        assert_matches_type(EmailerCampaignAddContactsResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_method_add_contacts_with_all_params(self, client: ApolloSDK) -> None:
        emailer_campaign = client.emailer_campaigns.add_contacts(
            sequence_id="sequence_id",
            emailer_campaign_id="emailer_campaign_id",
            send_email_from_email_account_id="send_email_from_email_account_id",
            add_if_in_queue=True,
            auto_unpause_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            contact_ids=["string"],
            contact_verification_skipped=True,
            contacts_without_ownership_permission=True,
            label_names=["string"],
            send_email_from_email_address="send_email_from_email_address",
            sequence_active_in_other_campaigns=True,
            sequence_finished_in_other_campaigns=True,
            sequence_job_change=True,
            sequence_no_email=True,
            sequence_same_company_in_same_campaign=True,
            sequence_unverified_email=True,
            status="active",
            user_id="user_id",
        )
        assert_matches_type(EmailerCampaignAddContactsResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_raw_response_add_contacts(self, client: ApolloSDK) -> None:
        response = client.emailer_campaigns.with_raw_response.add_contacts(
            sequence_id="sequence_id",
            emailer_campaign_id="emailer_campaign_id",
            send_email_from_email_account_id="send_email_from_email_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emailer_campaign = response.parse()
        assert_matches_type(EmailerCampaignAddContactsResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_streaming_response_add_contacts(self, client: ApolloSDK) -> None:
        with client.emailer_campaigns.with_streaming_response.add_contacts(
            sequence_id="sequence_id",
            emailer_campaign_id="emailer_campaign_id",
            send_email_from_email_account_id="send_email_from_email_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emailer_campaign = response.parse()
            assert_matches_type(EmailerCampaignAddContactsResponse, emailer_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_contacts(self, client: ApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sequence_id` but received ''"):
            client.emailer_campaigns.with_raw_response.add_contacts(
                sequence_id="",
                emailer_campaign_id="emailer_campaign_id",
                send_email_from_email_account_id="send_email_from_email_account_id",
            )

    @parametrize
    def test_method_archive(self, client: ApolloSDK) -> None:
        emailer_campaign = client.emailer_campaigns.archive(
            "sequence_id",
        )
        assert_matches_type(EmailerCampaignArchiveResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: ApolloSDK) -> None:
        response = client.emailer_campaigns.with_raw_response.archive(
            "sequence_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emailer_campaign = response.parse()
        assert_matches_type(EmailerCampaignArchiveResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: ApolloSDK) -> None:
        with client.emailer_campaigns.with_streaming_response.archive(
            "sequence_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emailer_campaign = response.parse()
            assert_matches_type(EmailerCampaignArchiveResponse, emailer_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: ApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sequence_id` but received ''"):
            client.emailer_campaigns.with_raw_response.archive(
                "",
            )

    @parametrize
    def test_method_deactivate(self, client: ApolloSDK) -> None:
        emailer_campaign = client.emailer_campaigns.deactivate(
            "sequence_id",
        )
        assert_matches_type(EmailerCampaignDeactivateResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_raw_response_deactivate(self, client: ApolloSDK) -> None:
        response = client.emailer_campaigns.with_raw_response.deactivate(
            "sequence_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emailer_campaign = response.parse()
        assert_matches_type(EmailerCampaignDeactivateResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_streaming_response_deactivate(self, client: ApolloSDK) -> None:
        with client.emailer_campaigns.with_streaming_response.deactivate(
            "sequence_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emailer_campaign = response.parse()
            assert_matches_type(EmailerCampaignDeactivateResponse, emailer_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deactivate(self, client: ApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sequence_id` but received ''"):
            client.emailer_campaigns.with_raw_response.deactivate(
                "",
            )

    @parametrize
    def test_method_search(self, client: ApolloSDK) -> None:
        emailer_campaign = client.emailer_campaigns.search()
        assert_matches_type(EmailerCampaignSearchResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: ApolloSDK) -> None:
        emailer_campaign = client.emailer_campaigns.search(
            page="page",
            per_page="per_page",
            q_name="q_name",
        )
        assert_matches_type(EmailerCampaignSearchResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: ApolloSDK) -> None:
        response = client.emailer_campaigns.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emailer_campaign = response.parse()
        assert_matches_type(EmailerCampaignSearchResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: ApolloSDK) -> None:
        with client.emailer_campaigns.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emailer_campaign = response.parse()
            assert_matches_type(EmailerCampaignSearchResponse, emailer_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_contact_status(self, client: ApolloSDK) -> None:
        emailer_campaign = client.emailer_campaigns.update_contact_status(
            contact_ids=["string"],
            emailer_campaign_ids=["string"],
            mode="mode",
        )
        assert_matches_type(EmailerCampaignUpdateContactStatusResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_raw_response_update_contact_status(self, client: ApolloSDK) -> None:
        response = client.emailer_campaigns.with_raw_response.update_contact_status(
            contact_ids=["string"],
            emailer_campaign_ids=["string"],
            mode="mode",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emailer_campaign = response.parse()
        assert_matches_type(EmailerCampaignUpdateContactStatusResponse, emailer_campaign, path=["response"])

    @parametrize
    def test_streaming_response_update_contact_status(self, client: ApolloSDK) -> None:
        with client.emailer_campaigns.with_streaming_response.update_contact_status(
            contact_ids=["string"],
            emailer_campaign_ids=["string"],
            mode="mode",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emailer_campaign = response.parse()
            assert_matches_type(EmailerCampaignUpdateContactStatusResponse, emailer_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmailerCampaigns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_activate(self, async_client: AsyncApolloSDK) -> None:
        emailer_campaign = await async_client.emailer_campaigns.activate(
            "sequence_id",
        )
        assert_matches_type(EmailerCampaignActivateResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.emailer_campaigns.with_raw_response.activate(
            "sequence_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emailer_campaign = await response.parse()
        assert_matches_type(EmailerCampaignActivateResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.emailer_campaigns.with_streaming_response.activate(
            "sequence_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emailer_campaign = await response.parse()
            assert_matches_type(EmailerCampaignActivateResponse, emailer_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_activate(self, async_client: AsyncApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sequence_id` but received ''"):
            await async_client.emailer_campaigns.with_raw_response.activate(
                "",
            )

    @parametrize
    async def test_method_add_contacts(self, async_client: AsyncApolloSDK) -> None:
        emailer_campaign = await async_client.emailer_campaigns.add_contacts(
            sequence_id="sequence_id",
            emailer_campaign_id="emailer_campaign_id",
            send_email_from_email_account_id="send_email_from_email_account_id",
        )
        assert_matches_type(EmailerCampaignAddContactsResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_method_add_contacts_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        emailer_campaign = await async_client.emailer_campaigns.add_contacts(
            sequence_id="sequence_id",
            emailer_campaign_id="emailer_campaign_id",
            send_email_from_email_account_id="send_email_from_email_account_id",
            add_if_in_queue=True,
            auto_unpause_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            contact_ids=["string"],
            contact_verification_skipped=True,
            contacts_without_ownership_permission=True,
            label_names=["string"],
            send_email_from_email_address="send_email_from_email_address",
            sequence_active_in_other_campaigns=True,
            sequence_finished_in_other_campaigns=True,
            sequence_job_change=True,
            sequence_no_email=True,
            sequence_same_company_in_same_campaign=True,
            sequence_unverified_email=True,
            status="active",
            user_id="user_id",
        )
        assert_matches_type(EmailerCampaignAddContactsResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_raw_response_add_contacts(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.emailer_campaigns.with_raw_response.add_contacts(
            sequence_id="sequence_id",
            emailer_campaign_id="emailer_campaign_id",
            send_email_from_email_account_id="send_email_from_email_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emailer_campaign = await response.parse()
        assert_matches_type(EmailerCampaignAddContactsResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_streaming_response_add_contacts(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.emailer_campaigns.with_streaming_response.add_contacts(
            sequence_id="sequence_id",
            emailer_campaign_id="emailer_campaign_id",
            send_email_from_email_account_id="send_email_from_email_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emailer_campaign = await response.parse()
            assert_matches_type(EmailerCampaignAddContactsResponse, emailer_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_contacts(self, async_client: AsyncApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sequence_id` but received ''"):
            await async_client.emailer_campaigns.with_raw_response.add_contacts(
                sequence_id="",
                emailer_campaign_id="emailer_campaign_id",
                send_email_from_email_account_id="send_email_from_email_account_id",
            )

    @parametrize
    async def test_method_archive(self, async_client: AsyncApolloSDK) -> None:
        emailer_campaign = await async_client.emailer_campaigns.archive(
            "sequence_id",
        )
        assert_matches_type(EmailerCampaignArchiveResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.emailer_campaigns.with_raw_response.archive(
            "sequence_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emailer_campaign = await response.parse()
        assert_matches_type(EmailerCampaignArchiveResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.emailer_campaigns.with_streaming_response.archive(
            "sequence_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emailer_campaign = await response.parse()
            assert_matches_type(EmailerCampaignArchiveResponse, emailer_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sequence_id` but received ''"):
            await async_client.emailer_campaigns.with_raw_response.archive(
                "",
            )

    @parametrize
    async def test_method_deactivate(self, async_client: AsyncApolloSDK) -> None:
        emailer_campaign = await async_client.emailer_campaigns.deactivate(
            "sequence_id",
        )
        assert_matches_type(EmailerCampaignDeactivateResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.emailer_campaigns.with_raw_response.deactivate(
            "sequence_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emailer_campaign = await response.parse()
        assert_matches_type(EmailerCampaignDeactivateResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.emailer_campaigns.with_streaming_response.deactivate(
            "sequence_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emailer_campaign = await response.parse()
            assert_matches_type(EmailerCampaignDeactivateResponse, emailer_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncApolloSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sequence_id` but received ''"):
            await async_client.emailer_campaigns.with_raw_response.deactivate(
                "",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncApolloSDK) -> None:
        emailer_campaign = await async_client.emailer_campaigns.search()
        assert_matches_type(EmailerCampaignSearchResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        emailer_campaign = await async_client.emailer_campaigns.search(
            page="page",
            per_page="per_page",
            q_name="q_name",
        )
        assert_matches_type(EmailerCampaignSearchResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.emailer_campaigns.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emailer_campaign = await response.parse()
        assert_matches_type(EmailerCampaignSearchResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.emailer_campaigns.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emailer_campaign = await response.parse()
            assert_matches_type(EmailerCampaignSearchResponse, emailer_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_contact_status(self, async_client: AsyncApolloSDK) -> None:
        emailer_campaign = await async_client.emailer_campaigns.update_contact_status(
            contact_ids=["string"],
            emailer_campaign_ids=["string"],
            mode="mode",
        )
        assert_matches_type(EmailerCampaignUpdateContactStatusResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_raw_response_update_contact_status(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.emailer_campaigns.with_raw_response.update_contact_status(
            contact_ids=["string"],
            emailer_campaign_ids=["string"],
            mode="mode",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emailer_campaign = await response.parse()
        assert_matches_type(EmailerCampaignUpdateContactStatusResponse, emailer_campaign, path=["response"])

    @parametrize
    async def test_streaming_response_update_contact_status(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.emailer_campaigns.with_streaming_response.update_contact_status(
            contact_ids=["string"],
            emailer_campaign_ids=["string"],
            mode="mode",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emailer_campaign = await response.parse()
            assert_matches_type(EmailerCampaignUpdateContactStatusResponse, emailer_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True
