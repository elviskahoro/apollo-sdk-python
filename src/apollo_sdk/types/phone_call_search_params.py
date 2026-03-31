# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PhoneCallSearchParams"]


class PhoneCallSearchParams(TypedDict, total=False):
    contact_label_ids: SequenceNotStr[str]
    """Find calls that included specific contacts. You can add multiple contacts.

    In Apollo terminology, a contact is a person that your team has explicitly added
    to your database.

    Use the
    <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
    a List of Users endpoint</a> to retrieve IDs for all of the users within your
    Apollo account.

    Example: `67e33d527de088000daa60c4` 6708415f59d9c70001b2f852
    """

    date_range_max: Annotated[Union[str, date], PropertyInfo(alias="date_range[max]", format="iso8601")]
    """Set the upper bound of the date range you want to search.

    Use this parameter in combination with the `date_range[min]` parameter. This
    date should fall after the `date_range[min]` date.

    The date should be formatted as `YYYY-MM-DD`.

    Example: `2025-06-12`
    """

    date_range_min: Annotated[Union[str, date], PropertyInfo(alias="date_range[min]", format="iso8601")]
    """Set the lower bound of the date range you want to search.

    Use this parameter in combination with the `date_range[max]` parameter. This
    date should fall before the `date_range[max]` date.

    The date should be formatted as `YYYY-MM-DD`.

    Example: `2025-04-01`
    """

    duration_max: Annotated[int, PropertyInfo(alias="duration[max]")]
    """Set the upper bound for the call duration you want to search.

    The duration should be seconds, not minutes or hours.

    Use this parameter in combination with the `duration[min]` parameter. This
    number should be larger than `duration[min]`.

    Example: `180`
    """

    duration_min: Annotated[int, PropertyInfo(alias="duration[min]")]
    """Set the lower bound for the call duration you want to search.

    The duration should be seconds, not minutes or hours.

    Use this parameter in combination with the `duration[max]` parameter. This
    number should be smallerr than `duration[min]`.

    Example: `30`
    """

    inbound: str
    """
    Search for calls based on whether they were `incoming` (the prospect called your
    team) or `outgoing` (your team called the prospect).
    """

    page: str
    """The page number of the Apollo data that you want to retrieve.

    Use this parameter in combination with the `per_page` parameter to make search
    results for navigable and improve the performance of the endpoint.

    Example: `4`
    """

    per_page: str
    """The number of search results that should be returned for each page.

    Limiting the number of results per page improves the endpoint's performance.

    Use the page parameter to search the different pages of data.

    Example: `10`
    """

    phone_call_outcome_ids: SequenceNotStr[str]
    """Filter calls based on their outcome.

    Call outcomes are unique to your team's Apollo account. When you use the
    <b>Disposition</b> search filter for calls in the Apollo product, you can find
    the corresponding call outcome ID in the URL.

    Example: `6095a710bd01d100a506d4c5`
    """

    phone_call_purpose_ids: SequenceNotStr[str]
    """Filter calls based on their purpose.

    Call purposes are unique to your team's Apollo account. When you use the
    <b>Purpose</b> search filter for calls in the Apollo product, you can find the
    corresponding call purpose ID in the URL.

    Example: `6095a710bd01d100a506d4cf`
    """

    q_keywords: str
    """Add keywords to narrow the search of the calls in your team's Apollo account.

    Example: `marketing conference attendees`
    """

    user_ids: SequenceNotStr[str]
    """Find calls that included specific users in your team's Apollo account.

    You can add multiple users.

    Use the
    <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
    a List of Users endpoint</a> to retrieve IDs for all of the users within your
    Apollo account.

    Example: `67e33d527de088000daa60c4`
    """
