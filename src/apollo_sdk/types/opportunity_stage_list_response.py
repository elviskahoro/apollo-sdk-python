# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OpportunityStageListResponse", "OpportunityStage"]


class OpportunityStage(BaseModel):
    id: Optional[str] = None

    description: Optional[str] = None

    display_order: Optional[int] = None

    forecast_category_cd: Optional[str] = None

    is_closed: Optional[bool] = None

    is_editable: Optional[object] = None

    is_meeting_set: Optional[object] = None

    is_won: Optional[bool] = None

    name: Optional[str] = None

    opportunity_pipeline_id: Optional[str] = None

    probability: Optional[int] = None

    salesforce_id: Optional[str] = None

    team_id: Optional[str] = None

    type: Optional[str] = None


class OpportunityStageListResponse(BaseModel):
    opportunity_stages: Optional[List[OpportunityStage]] = None
