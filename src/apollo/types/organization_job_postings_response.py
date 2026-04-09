# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OrganizationJobPostingsResponse", "OrganizationJobPosting"]


class OrganizationJobPosting(BaseModel):
    id: Optional[str] = None

    city: Optional[object] = None

    country: Optional[str] = None

    last_seen_at: Optional[str] = None

    posted_at: Optional[str] = None

    state: Optional[object] = None

    title: Optional[str] = None

    url: Optional[str] = None


class OrganizationJobPostingsResponse(BaseModel):
    organization_job_postings: Optional[List[OrganizationJobPosting]] = None
