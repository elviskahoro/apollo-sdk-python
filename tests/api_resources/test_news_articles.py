# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from src import ApolloSDK, AsyncApolloSDK
from src._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNewsArticles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_search(self, client: ApolloSDK) -> None:
        news_article = client.news_articles.search(
            organization_ids=["string"],
        )
        assert news_article is None

    @parametrize
    def test_method_search_with_all_params(self, client: ApolloSDK) -> None:
        news_article = client.news_articles.search(
            organization_ids=["string"],
            categories=["string"],
            page=0,
            per_page=0,
            published_at_max=parse_date("2019-12-27"),
            published_at_min=parse_date("2019-12-27"),
        )
        assert news_article is None

    @parametrize
    def test_raw_response_search(self, client: ApolloSDK) -> None:
        response = client.news_articles.with_raw_response.search(
            organization_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_article = response.parse()
        assert news_article is None

    @parametrize
    def test_streaming_response_search(self, client: ApolloSDK) -> None:
        with client.news_articles.with_streaming_response.search(
            organization_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news_article = response.parse()
            assert news_article is None

        assert cast(Any, response.is_closed) is True


class TestAsyncNewsArticles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_search(self, async_client: AsyncApolloSDK) -> None:
        news_article = await async_client.news_articles.search(
            organization_ids=["string"],
        )
        assert news_article is None

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncApolloSDK) -> None:
        news_article = await async_client.news_articles.search(
            organization_ids=["string"],
            categories=["string"],
            page=0,
            per_page=0,
            published_at_max=parse_date("2019-12-27"),
            published_at_min=parse_date("2019-12-27"),
        )
        assert news_article is None

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncApolloSDK) -> None:
        response = await async_client.news_articles.with_raw_response.search(
            organization_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_article = await response.parse()
        assert news_article is None

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncApolloSDK) -> None:
        async with async_client.news_articles.with_streaming_response.search(
            organization_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news_article = await response.parse()
            assert news_article is None

        assert cast(Any, response.is_closed) is True
