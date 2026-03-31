# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["TaskSearchParams"]


class TaskSearchParams(TypedDict, total=False):
    open_factor_names: SequenceNotStr[str]
    """Enter `task_types` for this parameter to return a count of tasks by task type.

    When used, the response includes a `"task_types": []` array with a `"count"`
    value for each task type.
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

    sort_by_field: str
    """
    Sort the tasks by 1 of the following options: <ul> <li> `task_due_at`: The most
    future-dated first. </li> <li> `task_priority`: The highest priority first.
    </li> </ul>
    """
