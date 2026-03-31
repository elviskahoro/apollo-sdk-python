# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AccountStageListResponse", "AccountStage"]


class AccountStage(BaseModel):
    id: Optional[str] = None

    category: Optional[object] = None

    default_exclude_for_leadgen: Optional[bool] = None

    display_name: Optional[str] = None

    display_order: Optional[int] = None

    is_meeting_set: Optional[object] = None

    name: Optional[str] = None

    team_id: Optional[str] = None


class AccountStageListResponse(BaseModel):
    account_stages: Optional[List[AccountStage]] = None
