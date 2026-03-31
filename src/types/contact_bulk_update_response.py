# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "ContactBulkUpdateResponse",
    "Contacts",
    "ContactsContact",
    "EntityProgressJob",
    "EntityProgressJobEntityProgressJob",
]


class ContactsContact(BaseModel):
    id: Optional[str] = None

    account_id: Optional[str] = None

    email: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    linkedin_url: Optional[str] = None

    organization_name: Optional[str] = None

    owner_id: Optional[str] = None

    present_raw_address: Optional[str] = None

    title: Optional[str] = None

    updated_at: Optional[datetime] = None


class Contacts(BaseModel):
    contacts: Optional[List[ContactsContact]] = None


class EntityProgressJobEntityProgressJob(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    entity_ids: Optional[List[str]] = None

    job_type: Optional[str] = None

    status: Optional[str] = None

    updated_at: Optional[datetime] = None


class EntityProgressJob(BaseModel):
    entity_progress_job: Optional[EntityProgressJobEntityProgressJob] = None


ContactBulkUpdateResponse: TypeAlias = Union[Contacts, EntityProgressJob]
