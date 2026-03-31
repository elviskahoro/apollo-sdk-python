# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["AccountUpdateParams"]


class AccountUpdateParams(TypedDict, total=False):
    account_stage_id: str
    """The Apollo ID for the account stage to which you want to assign the account.

    Enter a different ID to update the account stage.

    Call the
    <a href="https://docs.apollo.io/reference/list-account-stages" target="_blank">List
    Account Stages endpoint</a> to retrieve a list of all the account stage IDs
    available in your Apollo account.

    If you do not specify the account stage, Apollo automatically assigns the
    account to a stage as determined by your team's Apollo account. To change the
    order of account stages, launch the Apollo product and go to <b>Settings</b> >
    <b>Objects</b> >
    <a href="https://app.apollo.io/#/settings/accounts/stages" target="_blank"><b>Accounts</b></a>.
    Then, access the <b>Triggers</b> tab and change the stage for when an account is
    created.

    Example: `61b8e913e0f4d2012e3af74e`
    """

    domain: str
    """Update the domain name for the account. Do not include `www.` or similar.

    Example: `apollo.io` or `microsoft.com`
    """

    name: str
    """Update the account's name. This should be a human-readable name.

    Example: `The Fast Irish Copywriters`
    """

    owner_id: str
    """The ID for the account owner within your team's Apollo account.

    Enter a different ID to update the owner of the account.

    Use the
    <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
    a List of Users endpoint</a> to retrieve IDs for all of the users within your
    Apollo account.

    Example: `66302798d03b9601c7934ebf`
    """

    phone: str
    """Update the primary phone number for the account.

    This can be the phone number for the corporate headquarters, a branch location,
    or a direct dial to the primary point of contact for the account.

    Apollo sanitizes phone numbers, so you can enter them in any format. The
    sanitized number can be viewed in the endpoint response.

    Examples: `555-303-1234`; `+44 7911 123456`
    """

    raw_address: str
    """Update the corporate location for the account.

    This can include a city, US state, and country.

    Apollo matches the location you provide to the most applicable pre-defined
    location.

    Examples: `Belfield, Dublin 4, Ireland`; `Dallas, United States`
    """

    typed_custom_fields: Dict[str, str]
    """
    Add information to
    <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498754445-Create-Custom-Account-Fields" target="_blank">custom
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
