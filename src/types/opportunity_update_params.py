# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OpportunityUpdateParams"]


class OpportunityUpdateParams(TypedDict, total=False):
    amount: str
    """The monetary value of the deal.

    Enter a different value to update the deal amount.

    Do not enter commas or currency symbols for the value. The currency is
    automatically populated by the settings within your Apollo account. Commas are
    not accepted and result in the deal amount being left blank.

    Example: `55123478` (results in a deal value of `$55,123,478` if the default
    currency is USD)
    """

    closed_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Update the estimated close date for the deal. This can be a future or past date.

    The date should be formatted as `YYYY-MM-DD`.

    Example: `2025-10-30`
    """

    name: str
    """Update the name of the deal. This should be a human-readable name.

    Example: `Massive Q3 Deal`
    """

    opportunity_stage_id: str
    """The ID for the deal stage within your team's Apollo account.

    Enter a different ID to update the deal stage.

    Each deal stage is assigned a unique ID. To find deal stage IDs, call the
    <a href="https://docs.apollo.io/reference/get-a-list-of-opportunity-stages" target="_blank">List
    Deal Stages endpoint</a> and identify the value for `id` for each stage.

    Example: `6095a710bd01d100a506d4bd`
    """

    owner_id: str
    """The ID for the deal owner within your team's Apollo account.

    Enter a different ID to update the owner of the deal.

    Use the
    <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
    a List of Users endpoint</a> to retrieve IDs for all of the users within your
    Apollo account.

    Example: `66302798d03b9601c7934ebf`
    """

    typed_custom_fields: Dict[str, str]
    """
    Add information to
    <a href="https://knowledge.apollo.io/hc/en-us/articles/4415062486669-Create-a-Deal" target="_blank">custom
    fields</a> in Apollo.

    <b>Your custom fields are unique to your team's Apollo account. This means that
    the examples in this documentation may not work for your testing purposes.</b>

    To utilize this parameter successfully, call the
    <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
    List of All Custom Fields</a> endpoint and identify the `id` value for the
    custom field, as well as the appropriate data type. For example, if a custom
    field accepts picklist entries, you need to pass the accompanying `id` value for
    the picklist entry that you want to use as the input value.

    <b>Example</b>: When the
    <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
    List of All Custom Fields</a> endpoint returns an `id` of field:

    - `"60c39ed82bd02f01154c470a"` (datetime)

    then the value passed should be:

    `{"60c39ed82bd02f01154c470a": "2025-08-07"}`
    """
