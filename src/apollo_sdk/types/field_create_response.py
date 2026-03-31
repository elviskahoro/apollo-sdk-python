# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["FieldCreateResponse", "TypedCustomField"]


class TypedCustomField(BaseModel):
    id: Optional[str] = None

    modality: Optional[str] = None

    name: Optional[str] = None

    text_field_max_length: Optional[float] = None


class FieldCreateResponse(BaseModel):
    typed_custom_fields: Optional[List[TypedCustomField]] = None
