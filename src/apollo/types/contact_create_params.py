# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ContactCreateParams"]


class ContactCreateParams(TypedDict, total=False):
    account_id: str
    """The Apollo ID for the account. Example: `63f53afe4ceeca00016bdd2f`"""

    contact_stage_id: str
    """The Apollo ID for the contact stage. Example: `6095a710bd01d100a506d4ae`"""

    corporate_phone: str
    """The work/office phone number. Example: `+44 7911 123456`"""

    direct_phone: str
    """The primary phone number. Example: `555-303-1234`"""

    email: str
    """The email address of the contact. Example: `example@email.com`"""

    first_name: str
    """The first name of the contact you want to create. Example: `Tim`"""

    home_phone: str
    """The home phone number. Example: `555-303-1234`"""

    label_names: SequenceNotStr[str]
    """Lists to which the contact belongs."""

    last_name: str
    """The last name of the contact you want to create. Example: `Zheng`"""

    mobile_phone: str
    """The mobile phone number. Example: `555-303-1234`"""

    organization_name: str
    """The name of the contact's employer (company). Example: `apollo`"""

    other_phone: str
    """Alternative phone number. Example: `555-303-1234`"""

    present_raw_address: str
    """The personal location for the contact. Example: `Atlanta, United States`"""

    run_dedupe: bool
    """
    Set to `true` to enable deduplication logic that prevents creating duplicate
    contacts. When enabled, Apollo will check for existing contacts with matching
    email addresses, names, or other identifying information and return the existing
    contact instead of creating a duplicate. The default value is `false`.

    When deduplication is enabled, performance may be slightly impacted due to the
    additional validation checks, but this ensures data integrity and prevents
    duplicate entries in your database.
    """

    title: str
    """The current job title that the contact holds.

    Example: `senior research analyst`
    """

    typed_custom_fields: Dict[str, str]
    """
    Add information to
    <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498825869-Create-Custom-Contact-Fields" target="_blank">custom
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

    website_url: str
    """The corporate website URL. Example: `https://www.apollo.io/`"""
