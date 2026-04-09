# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EmailerCampaignSearchParams"]


class EmailerCampaignSearchParams(TypedDict, total=False):
    page: str
    """The page number of the Apollo data that you want to retrieve.

    Use this parameter in combination with the `per_page` parameter to make search
    results for navigable and improve the performance of the endpoint.

    Example: `4`
    """

    per_page: str
    """The number of search results that should be returned for each page.

    Limiting the number of results per page improves the endpoint's performance.

    Use the `page` parameter to search the different pages of data.

    Example: `10`
    """

    q_name: str
    """Add keywords to narrow the search of the sequences in your team's Apollo
    account.

    Keywords should directly match at least part of a sequence's name. For example,
    searching the keyword `marketing` might return the result
    `NY Marketing Sequence`, but not `NY Marketer Conference 2025 attendees`.

    This parameter only searches sequence names, not other sequence fields.

    Example: `marketing conference attendees`
    """
