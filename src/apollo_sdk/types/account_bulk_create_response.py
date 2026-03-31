# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AccountBulkCreateResponse", "CreatedAccount", "ExistingAccount"]


class CreatedAccount(BaseModel):
    id: Optional[str] = None
    """Account ID"""

    account_stage_id: Optional[str] = None
    """Account stage ID"""

    created_at: Optional[datetime] = None
    """Account creation timestamp"""

    domain: Optional[str] = None
    """Company domain"""

    name: Optional[str] = None
    """Account name"""

    owner_id: Optional[str] = None
    """Account owner ID"""

    phone: Optional[str] = None
    """Company phone number"""

    team_id: Optional[str] = None
    """Team ID"""

    updated_at: Optional[datetime] = None
    """Account last update timestamp"""


class ExistingAccount(BaseModel):
    id: Optional[str] = None
    """Account ID"""

    created_at: Optional[datetime] = None
    """Account creation timestamp"""

    domain: Optional[str] = None
    """Company domain"""

    name: Optional[str] = None
    """Account name"""

    owner_id: Optional[str] = None
    """Account owner ID"""

    team_id: Optional[str] = None
    """Team ID"""

    updated_at: Optional[datetime] = None
    """Account last update timestamp"""


class AccountBulkCreateResponse(BaseModel):
    created_accounts: Optional[List[CreatedAccount]] = None
    """Array of newly created accounts"""

    existing_accounts: Optional[List[ExistingAccount]] = None
    """
    Array of existing accounts that matched deduplication criteria (returned without
    modification)
    """
