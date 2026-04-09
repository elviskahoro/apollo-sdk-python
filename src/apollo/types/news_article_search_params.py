# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["NewsArticleSearchParams"]


class NewsArticleSearchParams(TypedDict, total=False):
    organization_ids: Required[SequenceNotStr[str]]
    """The Apollo IDs for the companies you want to include in your search results.

    Each company in the Apollo database is assigned a unique ID.

    To find IDs, call the
    <a href="https://docs.apollo.io/reference/organization-search" target="_blank">Organization
    Search endpoint</a> and identify the values for `organization_id`.

    Example: `5e66b6381e05b4008c8331b8`
    """

    categories: SequenceNotStr[str]
    """Filter your search to include only certain categories or sub-categories of news.

    Use the <b>News</b> search filter for companies within Apollo to uncover all
    possible categories and sub-categories.

    Examples: `hires`; `investment`; `contract`
    """

    page: int
    """The page number of the Apollo data that you want to retrieve.

    Use this parameter in combination with the `per_page` parameter to make search
    results for navigable and improve the performance of the endpoint.

    Example: `4`
    """

    per_page: int
    """The number of search results that should be returned for each page.

    Limiting the number of results per page improves the endpoint's performance.

    Use the `page` parameter to search the different pages of data.

    Example: `10`
    """

    published_at_max: Annotated[Union[str, date], PropertyInfo(alias="published_at[max]", format="iso8601")]
    """Set the upper bound of the date range you want to search.

    Use this parameter in combination with the `published_at[min]` parameter. This
    date should fall after the `published_at[min]` date.

    The date should be formatted as `YYYY-MM-DD`.

    Example: `2025-05-15`
    """

    published_at_min: Annotated[Union[str, date], PropertyInfo(alias="published_at[min]", format="iso8601")]
    """Set the lower bound of the date range you want to search.

    Use this parameter in combination with the `published_at[max]` parameter. This
    date should fall before the `published_at[max]` date.

    The date should be formatted as `YYYY-MM-DD`.

    Example: `2025-02-15`
    """
