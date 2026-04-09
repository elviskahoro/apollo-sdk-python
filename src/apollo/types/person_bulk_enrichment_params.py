# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PersonBulkEnrichmentParams", "Detail"]


class PersonBulkEnrichmentParams(TypedDict, total=False):
    details: Required[Iterable[Detail]]
    """Provide info for each person you want to enrich as an object within this array.

    Add up to 10 people.
    """

    reveal_personal_emails: bool
    """Set to `true` if you want to enrich all matched people with personal emails.

    This potentially consumes credits as part of your
    <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
    plan</a>. The default value is `false`.

    If a person resides in a
    <a href="https://knowledge.apollo.io/hc/en-us/articles/4409141087757" target="_blank">GDPR</a>-compliant
    region, Apollo will not reveal their personal email.
    """

    reveal_phone_number: bool
    """
    Set to `true` if you want to enrich the data of all matched people with all
    available phone numbers, including mobile phone numbers. This potentially
    consumes credits as part of your
    <a href="https://docs.apollo.io/docs/api-pricing" target="_blank">Apollo pricing
    plan</a>. The default value is `false`.

    If this parameter is set to `true`, you must enter a webhook URL for the
    `webhook_url` parameter. Apollo will asynchronously verify phone numbers for
    you, then send a JSON response that includes only details about the phone
    numbers to the webhook URL you provide. It can take several minutes for the
    phone numbers to be delivered.
    """

    run_waterfall_email: bool
    """Set to true to enable email waterfall enrichment"""

    run_waterfall_phone: bool
    """Set to true to enable phone waterfall enrichment"""

    webhook_url: str
    """
    If you set the `reveal_phone_number` parameter to `true`, this parameter becomes
    mandatory. Otherwise, do not use this parameter.

    Enter the webhook URL that specifies where Apollo should send a JSON response
    that includes the phone number you requested. Apollo suggests testing this flow
    to ensure you receive the separate response with the phone number.

    If phone numbers are not revealed delivered to the webhook URL, try applying
    UTF-8 encoding to the webhook URL.

    Example: `https://webhook.site/cc4cf44e-e047-4774-8dac-473d28474e40`;
    `https%3A%2F%2Fwebhook.site%2Fcc4cf44e-e047-4774-8dac-473d28474e40`
    """


class Detail(TypedDict, total=False):
    id: str
    """The Apollo ID for the person.

    Each person in the Apollo database is assigned a unique ID.

    To find IDs, call the
    <a href="https://docs.apollo.io/reference/people-api-search" target="_blank">People
    API Search endpoint</a> and identify the values for `person_id`.

    Example: `587cf802f65125cad923a266`
    """

    domain: str
    """The domain name for the person's employer.

    This can be the current employer or a previous employer. Do not include `www.`,
    the `@` symbol, or similar.

    Example: `apollo.io` or `microsoft.com`
    """

    email: str
    """The email address of the person.

    Example: `example@email.com`
    """

    first_name: str
    """The first name of the person.

    This is typically used in combination with the `last_name` parameter.

    Example: `tim`
    """

    hashed_email: str
    """The hashed email of the person.

    The email should adhere to either the MD5 or SHA-256 hash format.

    Example: `8d935115b9ff4489f2d1f9249503cadf` (MD5) or
    `97817c0c49994eb500ad0a5e7e2d8aed51977b26424d508f66e4e8887746a152` (SHA-256)
    """

    last_name: str
    """The last name of the person.

    This is typically used in combination with the `first_name` parameter.

    Example: `zheng`
    """

    linkedin_url: str
    """The URL for the person's LinkedIn profile.

    Example: `http://www.linkedin.com/in/tim-zheng-677ba010`
    """

    name: str
    """The full name of the person.

    This will typically be a first name and last name separated by a space. If you
    use this parameter, you do not need to use the `first_name` and `last_name`
    parameters.

    Example: `tim zheng`
    """

    organization_name: str
    """The name of the person's employer.

    This can be the current employer or a previous employer.

    Example: `apollo`
    """
