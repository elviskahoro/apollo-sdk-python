# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FieldListResponse", "Field"]


class Field(BaseModel):
    id: str

    label: str

    modality: str
    """
    Entity type this field belongs to (contact, account, opportunity, lead,
    custom_object)
    """

    type: str
    """
    Field data type (text, number, date, datetime, boolean, picklist, multi_select,
    url, email, phone, currency)
    """

    context: Optional[str] = None
    """
    High‑level context for the field (contact, account, opportunity, lead,
    custom_object)
    """

    created_at: Optional[datetime] = None

    meta: Optional[Dict[str, object]] = None
    """Extended configuration for the field"""

    project_workspace_id: Optional[str] = None

    source: Optional[str] = None
    """Field source (system, custom, crm_synced)"""

    updated_at: Optional[datetime] = None


class FieldListResponse(BaseModel):
    fields: Optional[List[Field]] = None
