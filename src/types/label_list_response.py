# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LabelListResponse", "LabelListResponseItem"]


class LabelListResponseItem(BaseModel):
    id: Optional[str] = None

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    cached_count: Optional[int] = None

    concurrency_locks: Optional[object] = None

    created_at: Optional[str] = None

    key: Optional[str] = None

    modality: Optional[str] = None

    name: Optional[str] = None

    need_cached_count_update: Optional[bool] = None

    needs_count_update_at: Optional[str] = None

    rule_config_template_id: Optional[object] = None

    team_id: Optional[str] = None

    updated_at: Optional[str] = None

    user_id: Optional[str] = None


LabelListResponse: TypeAlias = List[LabelListResponseItem]
