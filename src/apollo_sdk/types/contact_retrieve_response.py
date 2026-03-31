# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ContactRetrieveResponse", "Contact", "ContactPhoneNumber"]


class ContactPhoneNumber(BaseModel):
    raw_number: Optional[str] = None

    sanitized_number: Optional[str] = None

    type: Optional[str] = None


class Contact(BaseModel):
    id: Optional[str] = None

    account_id: Optional[str] = None

    contact_stage_id: Optional[str] = None

    created_at: Optional[str] = None

    email: Optional[str] = None

    first_name: Optional[str] = None

    label_ids: Optional[List[str]] = None

    last_name: Optional[str] = None

    linkedin_url: Optional[str] = None

    name: Optional[str] = None

    organization_name: Optional[str] = None

    owner_id: Optional[str] = None

    phone_numbers: Optional[List[ContactPhoneNumber]] = None

    title: Optional[str] = None

    typed_custom_fields: Optional[Dict[str, str]] = None

    updated_at: Optional[str] = None


class ContactRetrieveResponse(BaseModel):
    contact: Optional[Contact] = None
