# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .organization_enrich_response import Organization

__all__ = ["OrganizationRetrieveResponse", "Organization"]


class OrganizationRetrieveResponse(BaseModel):
    organization: Optional[Organization] = None
