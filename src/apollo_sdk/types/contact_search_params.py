# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ContactSearchParams"]


class ContactSearchParams(TypedDict, total=False):
    contact_label_ids: SequenceNotStr[str]
    """The Apollo IDs for the labels that you want to include in your search results.

    If you add multiple labels, Apollo will include all contacts connected to any of
    the labels, along with the other parameters, in the search results. Example:
    `['6095a710bd01d100a506d4ae']`
    """

    contact_stage_ids: SequenceNotStr[str]
    """
    The Apollo IDs for the contact stages that you want to include in your search
    results. If you add multiple contact stages, Apollo will include all contacts
    that match any of the stages, along with the other parameters, in the search
    results. Call the
    [List Contact Stages endpoint](https://docs.apollo.io/reference/list-contact-stages)
    to retrieve a list of all the contact stage IDs available in your Apollo
    account. Example: `6095a710bd01d100a506d4ae`
    """

    page: int
    """The page number of the Apollo data that you want to retrieve.

    Use this parameter in combination with the `per_page` parameter to make search
    results navigable and improve the performance of the endpoint. Example: `4`
    """

    per_page: int
    """The number of search results that should be returned for each page.

    Limiting the number of results per page improves the endpoint's performance. Use
    the `page` parameter to search the different pages of data. Example: `10`
    """

    q_keywords: str
    """Add keywords to narrow the search of the contacts in your team's Apollo account.

    Keywords can include combinations of names, job titles, employers (company
    names), and email addresses. Examples: `tim zheng`; `senior research analyst`;
    `microsoft`
    """

    sort_ascending: bool
    """Set to `true` to sort the matching contacts in ascending order.

    This parameter must be used with `sort_by_field`. Otherwise, the sorting logic
    is not applied. Example: `true`
    """

    sort_by_field: str
    """Sort the matching contacts by 1 of the following options:

    - `contact_last_activity_date`: The most recent activity date recorded first.
    - `contact_email_last_opened_at`: The most recent email opened date first.
    - `contact_email_last_clicked_at`: The most recent email clicked first.
    - `contact_created_at`: The most recently created first.
    - `contact_updated_at`: The most recently updated first.
    """
