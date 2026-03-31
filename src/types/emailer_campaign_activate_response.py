# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EmailerCampaignActivateResponse", "EmailerCampaign", "EmailerStep"]


class EmailerCampaign(BaseModel):
    id: Optional[str] = None

    active: Optional[bool] = None

    unique_scheduled: Optional[int] = None


class EmailerStep(BaseModel):
    id: Optional[str] = None

    emailer_campaign_id: Optional[str] = None

    note: Optional[str] = None

    position: Optional[int] = None

    type: Optional[str] = None

    wait_time: Optional[int] = None


class EmailerCampaignActivateResponse(BaseModel):
    emailer_campaign: Optional[EmailerCampaign] = None

    emailer_steps: Optional[List[EmailerStep]] = None
