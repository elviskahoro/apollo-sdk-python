# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ContactUpdateParams"]


class ContactUpdateParams(TypedDict, total=False):
    account_id: str
    """Update the account ID. Example: `63f53afe4ceeca00016bdd2f`"""

    contact_stage_id: str
    """Update the contact stage ID. Example: `6095a710bd01d100a506d4af`"""

    corporate_phone: str
    """Work/office phone."""

    direct_phone: str
    """Primary phone."""

    email: str
    """Update the contact email. Example: `example@email.com`"""

    first_name: str
    """Update the contact's first name. Example: `Tim`"""

    home_phone: str
    """Home phone."""

    label_names: SequenceNotStr[str]
    """Replace lists this contact belongs to.

    (Passing new values will overwrite existing lists.)
    """

    last_name: str
    """Update the contact's last name. Example: `Zheng`"""

    mobile_phone: str
    """Mobile phone."""

    organization_name: str
    """Update the employer (company) name. Example: `apollo`"""

    other_phone: str
    """Alternate phone."""

    present_raw_address: str
    """Update location (city/state/country). Example: `Atlanta, United States`"""

    title: str
    """Update the job title. Example: `senior research analyst`"""

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
    """Update the employer website URL. Example: `https://www.apollo.io/`"""
