# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PersonSearchResponse", "Person", "PersonOrganization"]


class PersonOrganization(BaseModel):
    """Information about the person's current employer organization."""

    has_city: Optional[bool] = None
    """
    Indicates whether Apollo has city location data for the organization's
    headquarters.
    """

    has_country: Optional[bool] = None
    """
    Indicates whether Apollo has country location data for the organization's
    headquarters.
    """

    has_employee_count: Optional[bool] = None
    """Indicates whether Apollo has employee count data for this organization."""

    has_industry: Optional[bool] = None
    """
    Indicates whether Apollo has industry classification data for this organization.
    """

    has_phone: Optional[bool] = None
    """Indicates whether Apollo has phone number data for this organization."""

    has_revenue: Optional[bool] = None
    """Indicates whether Apollo has revenue data for this organization."""

    has_state: Optional[bool] = None
    """
    Indicates whether Apollo has state location data for the organization's
    headquarters.
    """

    has_zip_code: Optional[bool] = None
    """
    Indicates whether Apollo has postal/zip code data for the organization's
    headquarters.
    """

    name: Optional[str] = None
    """The name of the organization."""


class Person(BaseModel):
    id: Optional[str] = None
    """The Apollo ID for the person."""

    first_name: Optional[str] = None
    """The first name of the person."""

    has_city: Optional[bool] = None
    """Indicates whether Apollo has city location data for this person."""

    has_country: Optional[bool] = None
    """Indicates whether Apollo has country location data for this person."""

    has_direct_phone: Optional[str] = None
    """Indicates whether Apollo has direct phone number data for this person.

    Returns `Yes` if available, or
    `Maybe: please request direct dial via people/bulk_match` if uncertain.
    """

    has_email: Optional[bool] = None
    """Indicates whether Apollo has a verified email address for this person."""

    has_state: Optional[bool] = None
    """Indicates whether Apollo has state location data for this person."""

    last_name_obfuscated: Optional[str] = None
    """The last name of the person with the middle characters obfuscated for privacy.

    The format shows the first 2 characters, followed by asterisks, and then the
    last character.
    """

    last_refreshed_at: Optional[datetime] = None
    """
    The date and time when the person's data was last refreshed in Apollo's
    database.
    """

    organization: Optional[PersonOrganization] = None
    """Information about the person's current employer organization."""

    title: Optional[str] = None
    """The job title of the person.

    This field may be null if the person's title is not available.
    """


class PersonSearchResponse(BaseModel):
    people: Optional[List[Person]] = None
    """An array of people that match your search criteria."""

    total_entries: Optional[int] = None
    """The total number of people that match your search criteria."""
