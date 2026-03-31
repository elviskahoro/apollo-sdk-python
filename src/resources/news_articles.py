# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import news_article_search_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["NewsArticlesResource", "AsyncNewsArticlesResource"]


class NewsArticlesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NewsArticlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return NewsArticlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewsArticlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return NewsArticlesResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        organization_ids: SequenceNotStr[str],
        categories: SequenceNotStr[str] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        published_at_max: Union[str, date] | Omit = omit,
        published_at_min: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        news_articles_search

        Args:
          organization_ids: The Apollo IDs for the companies you want to include in your search results.
              Each company in the Apollo database is assigned a unique ID.

              To find IDs, call the
              <a href="https://docs.apollo.io/reference/organization-search" target="_blank">Organization
              Search endpoint</a> and identify the values for `organization_id`.

              Example: `5e66b6381e05b4008c8331b8`

          categories: Filter your search to include only certain categories or sub-categories of news.
              Use the <b>News</b> search filter for companies within Apollo to uncover all
              possible categories and sub-categories.

              Examples: `hires`; `investment`; `contract`

          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          published_at_max: Set the upper bound of the date range you want to search.

              Use this parameter in combination with the `published_at[min]` parameter. This
              date should fall after the `published_at[min]` date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-05-15`

          published_at_min: Set the lower bound of the date range you want to search.

              Use this parameter in combination with the `published_at[max]` parameter. This
              date should fall before the `published_at[max]` date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-02-15`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/news_articles/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_ids%5B%5D": organization_ids[0]
                        if len(organization_ids) == 1
                        else organization_ids,
                        "categories%5B%5D": categories,
                        "page": page,
                        "per_page": per_page,
                        "published_at_max": published_at_max,
                        "published_at_min": published_at_min,
                    },
                    news_article_search_params.NewsArticleSearchParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncNewsArticlesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNewsArticlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNewsArticlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewsArticlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncNewsArticlesResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        organization_ids: SequenceNotStr[str],
        categories: SequenceNotStr[str] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        published_at_max: Union[str, date] | Omit = omit,
        published_at_min: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        news_articles_search

        Args:
          organization_ids: The Apollo IDs for the companies you want to include in your search results.
              Each company in the Apollo database is assigned a unique ID.

              To find IDs, call the
              <a href="https://docs.apollo.io/reference/organization-search" target="_blank">Organization
              Search endpoint</a> and identify the values for `organization_id`.

              Example: `5e66b6381e05b4008c8331b8`

          categories: Filter your search to include only certain categories or sub-categories of news.
              Use the <b>News</b> search filter for companies within Apollo to uncover all
              possible categories and sub-categories.

              Examples: `hires`; `investment`; `contract`

          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          published_at_max: Set the upper bound of the date range you want to search.

              Use this parameter in combination with the `published_at[min]` parameter. This
              date should fall after the `published_at[min]` date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-05-15`

          published_at_min: Set the lower bound of the date range you want to search.

              Use this parameter in combination with the `published_at[max]` parameter. This
              date should fall before the `published_at[max]` date.

              The date should be formatted as `YYYY-MM-DD`.

              Example: `2025-02-15`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/news_articles/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_ids%5B%5D": organization_ids[0]
                        if len(organization_ids) == 1
                        else organization_ids,
                        "categories%5B%5D": categories,
                        "page": page,
                        "per_page": per_page,
                        "published_at_max": published_at_max,
                        "published_at_min": published_at_min,
                    },
                    news_article_search_params.NewsArticleSearchParams,
                ),
            ),
            cast_to=NoneType,
        )


class NewsArticlesResourceWithRawResponse:
    def __init__(self, news_articles: NewsArticlesResource) -> None:
        self._news_articles = news_articles

        self.search = to_raw_response_wrapper(
            news_articles.search,
        )


class AsyncNewsArticlesResourceWithRawResponse:
    def __init__(self, news_articles: AsyncNewsArticlesResource) -> None:
        self._news_articles = news_articles

        self.search = async_to_raw_response_wrapper(
            news_articles.search,
        )


class NewsArticlesResourceWithStreamingResponse:
    def __init__(self, news_articles: NewsArticlesResource) -> None:
        self._news_articles = news_articles

        self.search = to_streamed_response_wrapper(
            news_articles.search,
        )


class AsyncNewsArticlesResourceWithStreamingResponse:
    def __init__(self, news_articles: AsyncNewsArticlesResource) -> None:
        self._news_articles = news_articles

        self.search = async_to_streamed_response_wrapper(
            news_articles.search,
        )
