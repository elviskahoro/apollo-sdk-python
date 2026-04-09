# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .account_update_response import Account

__all__ = ["AccountRetrieveResponse", "Account"]


class AccountRetrieveResponse(BaseModel):
    account: Optional[Account] = None

    labels: Optional[List[object]] = None
