# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AccountBulkUpdateResponse", "Account"]


class Account(BaseModel):
    id: Optional[str] = None

    account_stage_id: Optional[str] = None


class AccountBulkUpdateResponse(BaseModel):
    accounts: Optional[List[Account]] = None
