# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["AccountSearchParams"]


class AccountSearchParams(TypedDict, total=False):
    account_label_ids: SequenceNotStr[str]
    """The Apollo IDs for the labels that you want to include in your search results.

    If you add multiple labels, Apollo will include all accounts connected to any of
    the labels, along with the other parameters, in the search results. Example:
    `['6095a710bd01d100a506d4ae']`
    """

    account_stage_ids: SequenceNotStr[str]
    """
    The Apollo IDs for the account stages that you want to include in your search
    results. If you add multiple account stages, Apollo will include all accounts
    that match any of the stages, along with the other parameters, in the search
    results. Call the
    [List Account Stages endpoint](https://docs.apollo.io/reference/list-account-stages)
    to retrieve a list of all the account stage IDs available in your Apollo
    account. Example: `61b8e913e0f4d2012e3af74e`
    """

    page: int
    """The page number of the Apollo data that you want to retrieve.

    Use this parameter in combination with the `per_page` parameter to make search
    results navigable and improve the performance of the endpoint. Example: `4`
    """

    per_page: int
    """The number of search results that should be returned for each page.

    Limiting the number of results per page improves the endpoint's performance. Use
    the `page` parameter to navigate through the different pages of data. Example:
    `10`
    """

    q_organization_name: str
    """Add keywords to narrow the search of the accounts in your team's Apollo account.

    Keywords should directly match at least part of an account's name. For example,
    searching the keyword `marketing` might return the result
    `NY Marketing Unlimited`, but not `NY Market Analysts`. This parameter only
    searches account names, not other account fields. Examples: `apollo`;
    `microsoft`; `marketing`
    """

    sort_ascending: bool
    """Set to `true` to sort the matching accounts in ascending order.

    This parameter must be used with `sort_by_field`. Otherwise, the sorting logic
    is not applied. Example: `true`
    """

    sort_by_field: Literal["account_last_activity_date", "account_created_at", "account_updated_at"]
    """Sort the matching accounts by 1 of the following options:

    - `account_last_activity_date`: The most recent activity date recorded first.
    - `account_created_at`: The most recently created first.
    - `account_updated_at`: The most recently updated first.
    """
