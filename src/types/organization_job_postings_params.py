# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OrganizationJobPostingsParams"]


class OrganizationJobPostingsParams(TypedDict, total=False):
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
