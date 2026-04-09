# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AccountUpdateOwnersParams"]


class AccountUpdateOwnersParams(TypedDict, total=False):
    account_ids: Required[SequenceNotStr[str]]
    """The Apollo IDs for the account that you want to assign to an owner.

    To find account IDs, call the
    <a href="https://docs.apollo.io/reference/search-for-accounts" target="_blank">Search
    for Accounts endpoint</a> and identify the `id` value for the account.

    Example: `66e9abf95ac32901b20d1a0d`
    """

    owner_id: Required[str]
    """The ID for the account owner within your team's Apollo account.

    This user will be assigned ownership of the accounts.

    Use the
    <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
    a List of Users endpoint</a> to retrieve IDs for all of the users within your
    Apollo account.

    Example: `66302798d03b9601c7934ebf`
    """
