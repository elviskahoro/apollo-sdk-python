# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ContactUpdateOwnersParams"]


class ContactUpdateOwnersParams(TypedDict, total=False):
    contact_ids: Required[SequenceNotStr[str]]
    """The Apollo IDs for the contacts that you want assign to an owner.

    To find contact IDs, call the
    <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
    for Contacts endpoint</a> and identify the `id` value for the contact.

    Example: `66e34b81740c50074e3d1bd4`
    """

    owner_id: Required[str]
    """The ID for the contact owner within your team's Apollo account.

    This user will be assigned ownership of the contacts.

    Use the
    <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
    a List of Users endpoint</a> endpoint to retrieve IDs for all of the users
    within your Apollo account.

    Example: `66302798d03b9601c7934ebf`
    """
