# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["OrganizationBulkEnrichParams"]


class OrganizationBulkEnrichParams(TypedDict, total=False):
    domains: Required[SequenceNotStr[str]]
    """The domain of each company that you want to enrich.

    Do not include `www.`, the `@` symbol, or similar.

    Example: `apollo.io` and `microsoft.com`
    """
