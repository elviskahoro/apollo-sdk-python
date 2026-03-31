# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ContactUpdateOwnersResponse", "Contact"]


class Contact(BaseModel):
    id: Optional[str] = None

    crm_owner_id: Optional[object] = None

    owner_id: Optional[str] = None


class ContactUpdateOwnersResponse(BaseModel):
    contacts: Optional[List[Contact]] = None
