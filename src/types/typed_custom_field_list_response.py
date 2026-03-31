# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TypedCustomFieldListResponse", "TypedCustomField"]


class TypedCustomField(BaseModel):
    id: Optional[str] = None

    additional_mapped_crm_field: Optional[object] = None

    finder_view_ids: Optional[List[object]] = None

    is_local: Optional[bool] = None

    is_readonly_mapped_crm_field: Optional[object] = None

    mapped_crm_field: Optional[object] = None

    mirrored: Optional[bool] = None

    modality: Optional[str] = None

    name: Optional[str] = None

    picklist_options: Optional[List[object]] = None

    picklist_options_last_synced_at: Optional[str] = None

    picklist_value_set_id: Optional[object] = None

    system_name: Optional[object] = None

    text_field_max_length: Optional[object] = None

    type: Optional[str] = None


class TypedCustomFieldListResponse(BaseModel):
    typed_custom_fields: Optional[List[TypedCustomField]] = None
