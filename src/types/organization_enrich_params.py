# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrganizationEnrichParams"]


class OrganizationEnrichParams(TypedDict, total=False):
    domain: Required[str]
    """The domain of the company that you want to enrich.

    Do not include `www.`, the `@` symbol, or similar.

    Example: `apollo.io` or `microsoft.com`
    """
