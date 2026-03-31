# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["EmailerCampaignArchiveResponse", "EmailerCampaign"]


class EmailerCampaign(BaseModel):
    id: Optional[str] = None

    active: Optional[bool] = None

    archived: Optional[bool] = None

    deleted: Optional[bool] = None


class EmailerCampaignArchiveResponse(BaseModel):
    emailer_campaign: Optional[EmailerCampaign] = None
