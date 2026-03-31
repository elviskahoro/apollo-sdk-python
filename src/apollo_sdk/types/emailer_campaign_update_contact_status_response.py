# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EmailerCampaignUpdateContactStatusResponse", "EntityProgressJob", "EntityProgressJobParams"]


class EntityProgressJobParams(BaseModel):
    access_token: Optional[object] = None

    api_key: Optional[str] = None

    mode: Optional[str] = None

    sequence_ids: Optional[List[str]] = None

    stop_reason: Optional[object] = None


class EntityProgressJob(BaseModel):
    id: Optional[str] = None

    batch_size: Optional[int] = None

    entity_ids: Optional[List[str]] = None

    job_type: Optional[str] = None

    params: Optional[EntityProgressJobParams] = None

    progress: Optional[int] = None

    user_id: Optional[str] = None


class EmailerCampaignUpdateContactStatusResponse(BaseModel):
    entity_progress_job: Optional[EntityProgressJob] = None
