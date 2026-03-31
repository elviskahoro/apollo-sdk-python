# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FieldCreateParams", "Meta"]


class FieldCreateParams(TypedDict, total=False):
    label: str
    """Name of the custom field you want to create. Example: `Test Name`"""

    meta: Meta

    modality: Literal["contact", "account", "opportunity"]
    """The modality of the custom field you want to create. Example: `contact`"""

    type: Literal["string", "textarea", "number", "date", "datetime", "boolean"]
    """What kind of custom field you want to create. Example: `textarea`"""


class Meta(TypedDict, total=False):
    max_length: float
