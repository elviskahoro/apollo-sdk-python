# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ContactBulkCreateResponse", "CreatedContact", "ExistingContact"]


class CreatedContact(BaseModel):
    id: Optional[str] = None
    """Contact ID"""

    contact_stage_id: Optional[str] = None
    """Contact stage ID"""

    created_at: Optional[datetime] = None
    """Contact creation timestamp"""

    email: Optional[str] = None
    """Contact's email address"""

    first_name: Optional[str] = None
    """Contact's first name"""

    last_name: Optional[str] = None
    """Contact's last name"""

    organization_name: Optional[str] = None
    """Company/organization name"""

    owner_id: Optional[str] = None
    """Contact owner ID"""

    team_id: Optional[str] = None
    """Team ID"""

    title: Optional[str] = None
    """Contact's job title"""

    updated_at: Optional[datetime] = None
    """Contact last update timestamp"""


class ExistingContact(BaseModel):
    id: Optional[str] = None
    """Contact ID"""

    created_at: Optional[datetime] = None
    """Contact creation timestamp"""

    email: Optional[str] = None
    """Contact's email address"""

    first_name: Optional[str] = None
    """Contact's first name"""

    last_name: Optional[str] = None
    """Contact's last name"""

    owner_id: Optional[str] = None
    """Contact owner ID"""

    team_id: Optional[str] = None
    """Team ID"""

    title: Optional[str] = None
    """Contact's job title"""

    updated_at: Optional[datetime] = None
    """Contact last update timestamp"""


class ContactBulkCreateResponse(BaseModel):
    created_contacts: Optional[List[CreatedContact]] = None
    """Array of newly created contacts"""

    existing_contacts: Optional[List[ExistingContact]] = None
    """
    Array of existing contacts that matched deduplication criteria (returned without
    modification, except for email_import placeholders which may be merged)
    """
