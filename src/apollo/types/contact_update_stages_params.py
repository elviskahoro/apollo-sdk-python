# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ContactUpdateStagesParams"]


class ContactUpdateStagesParams(TypedDict, total=False):
    contact_ids: Required[SequenceNotStr[str]]
    """The Apollo IDs for the contacts that you want to update.

    To find contact IDs, call the
    <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
    for Contacts endpoint</a> and identify the `id` value for the contact.

    Example: `66e34b81740c50074e3d1bd4`
    """

    contact_stage_id: Required[str]
    """The Apollo ID for the contact stage to which you want to assign the contacts.

    Call the
    <a href="https://docs.apollo.io/reference/list-contact-stages" target="_blank">List
    Contact Stages endpoint</a> to retrieve a list of all the contact stage IDs
    available in your Apollo account.

    Example: `6095a710bd01d100a506d4af`
    """
