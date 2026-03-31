# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AccountBulkUpdateParams", "AccountAttribute"]


class AccountBulkUpdateParams(TypedDict, total=False):
    account_attributes: Iterable[AccountAttribute]
    """Array of account objects with individual updates.

    Use this for applying different updates to each account.
    """

    account_ids: SequenceNotStr[str]
    """Array of account IDs to update with the same values.

    Use this for applying the same updates to multiple accounts.
    """

    account_stage_id: str
    """When using account_ids, apply this account stage to all accounts"""

    async_: Annotated[bool, PropertyInfo(alias="async")]
    """Set to true to process updates asynchronously.

    Only available when using account_ids. Not supported with account_attributes.
    """

    name: str
    """When using account_ids, apply this name to all accounts"""

    owner_id: str
    """When using account_ids, apply this owner to all accounts"""


class AccountAttribute(TypedDict, total=False):
    id: Required[str]
    """The account ID to update"""

    account_stage_id: str
    """The Apollo account stage ID"""

    name: str
    """The account name"""

    owner_id: str
    """The Apollo user ID to assign as owner"""

    typed_custom_fields: Dict[str, str]
    """Custom field values as key-value pairs"""
