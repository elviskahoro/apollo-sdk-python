# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PersonSearchParams"]


class PersonSearchParams(TypedDict, total=False):
    contact_email_status: SequenceNotStr[str]
    """The email statuses for the people you want to find.

    You can add multiple statuses to expand your search.

    The statuses you can search include: <ul> <li> <code>verified</code> </li> <li>
    <code>unverified</code> </li> <li> <code>likely to engage</code> </li> <li>
    <code>unavailable</code> </li> </ul>
    """

    currently_not_using_any_of_technology_uids: SequenceNotStr[str]
    """
    Exclude people from your search based on any of the technologies their current
    employer uses. Apollo supports filtering by 1,500+ technologies.

    Apollo calculates technologies data from multiple sources. This data is updated
    regularly. Check out the full list of supported technologies by
    <a href="https://api.apollo.io/v1/auth/supported_technologies_csv" target="_blank">downloading
    this CSV file</a>.

    Use underscores (`_`) to replace spaces and periods for the technologies listed
    in the CSV file.

    Examples: `salesforce`; `google_analytics`; `wordpress_org`
    """

    currently_using_all_of_technology_uids: SequenceNotStr[str]
    """Find people based on all of the technologies their current employer uses.

    Apollo supports filtering by 1,500+ technologies.

    Apollo calculates technologies data from multiple sources. This data is updated
    regularly. Check out the full list of supported technologies by
    <a href="https://api.apollo.io/v1/auth/supported_technologies_csv" target="_blank">downloading
    this CSV file</a>.

    Use underscores (`_`) to replace spaces and periods for the technologies listed
    in the CSV file.

    Examples: `salesforce`; `google_analytics`; `wordpress_org`
    """

    currently_using_any_of_technology_uids: SequenceNotStr[str]
    """Find people based on any of the technologies their current employer uses.

    Apollo supports filtering by 1,500+ technologies.

    Apollo calculates technologies data from multiple sources. This data is updated
    regularly. Check out the full list of supported technologies by
    <a href="https://api.apollo.io/v1/auth/supported_technologies_csv" target="_blank">downloading
    this CSV file</a>.

    Use underscores (`_`) to replace spaces and periods for the technologies listed
    in the CSV file.

    Examples: `salesforce`; `google_analytics`; `wordpress_org`
    """

    include_similar_titles: bool
    """
    This parameter determines whether people with job titles similar to the titles
    you define in the `person_titles[]` parameter are returned in the response.

    Set this parameter to `false` when using `person_titles[]` to return only strict
    matches for job titles.
    """

    organization_ids: SequenceNotStr[str]
    """
    The Apollo IDs for the companies (employers) you want to include in your search
    results. Each company in the Apollo database is assigned a unique ID.

    To find IDs, call the
    <a href="https://docs.apollo.io/reference/organization-search" target="_blank">Organization
    Search endpoint</a> and identify the values for `organization_id`.

    Example: `5e66b6381e05b4008c8331b8`
    """

    organization_job_locations: SequenceNotStr[str]
    """The locations of the jobs being actively recruited by the person's employer.

    Examples: `atlanta`; `japan`
    """

    organization_job_posted_at_range_max: Annotated[
        Union[str, date], PropertyInfo(alias="organization_job_posted_at_range[max]", format="iso8601")
    ]
    """The latest date when jobs were posted by the person's current employer.

    Use this parameter in combination with `organization_job_posted_at_range[min]`
    to set a date range for when jobs posted.

    Example: `2025-09-25`
    """

    organization_job_posted_at_range_min: Annotated[
        Union[str, date], PropertyInfo(alias="organization_job_posted_at_range[min]", format="iso8601")
    ]
    """The earliest date when jobs were posted by the person's current employer.

    Use this parameter in combination with `organization_job_posted_at_range[max]`
    to set a date range for when jobs posted.

    Example: `2025-07-25`
    """

    organization_locations: SequenceNotStr[str]
    """The location of the company headquarters for a person's current employer.

    You can search across cities, US states, and countries.

    If a company has several office locations, results are still based on the
    headquarters location. For example, if you search `chicago` but a company's HQ
    location is in `boston`, people that work for the Boston-based company will not
    appear in your results, even if they match other \\pparameters.

    To find people based on their personal location, use the `person_locations`
    parameter.

    Examples: `texas`; `tokyo`; `spain`
    """

    organization_num_employees_ranges: SequenceNotStr[str]
    """The number range of employees working for the person's current company.

    This enables you to find people based on the headcount of their employer. You
    can add multiple ranges to expand your search results.

    Each range you add needs to be a string, with the upper and lower numbers of the
    range separated only by a comma.

    Examples: `1,10`; `250,500`; `10000,20000`
    """

    organization_num_jobs_range_max: Annotated[int, PropertyInfo(alias="organization_num_jobs_range[max]")]
    """The maximum number of job postings active at the person's current empployer.

    Use this parameter in combination with `organization_num_jobs_range[min]` to set
    a job postings range.

    Examples: `50`; `500`
    """

    organization_num_jobs_range_min: Annotated[int, PropertyInfo(alias="organization_num_jobs_range[min]")]
    """The minimum number of job postings active at the person's current empployer.

    Use this parameter in combination with `organization_num_jobs_range[max]` to set
    a job postings range.

    Examples: `50`; `500`
    """

    page: int
    """The page number of the Apollo data that you want to retrieve.

    Use this parameter in combination with the `per_page` parameter to make search
    results for navigable and improve the performance of the endpoint.

    Example: `4`
    """

    per_page: int
    """The number of search results that should be returned for each page.

    Limiting the number of results per page improves the endpoint's performance.

    Use the `page` parameter to search the different pages of data.

    Example: `10`
    """

    person_locations: SequenceNotStr[str]
    """The location where people live.

    You can search across cities, US states, and countries.

    To find people based on the headquarters locations of their current employer,
    use the `organization_locations` parameter.

    Examples: `california`; `ireland`; `chicago`
    """

    person_seniorities: SequenceNotStr[str]
    """The job seniority that people hold within their current employer.

    This enables you to find people that currently hold positions at certain
    reporting levels, such as Director level or senior IC level.

    For a person to be included in search results, they only need to match 1 of the
    seniorities you add. Adding more seniorities expands your search results.

    Searches only return results based on their current job title, so searching for
    Director-level employees only returns people that currently hold a
    Director-level title. If someone was previously a Director, but is currently a
    VP, they would not be included in your search results.

    Use this parameter in combination with the `person_titles[]` parameter to find
    people based on specific job functions and seniority levels.

    The following options can be used for this parameter:

    <ul><li><code>owner</code></li><li><code>founder</code></li><li><code>c_suite</code></li><li><code>partner</code></li><li><code>vp</code></li><li><code>head</code></li><li><code>director</code></li><li><code>manager</code></li><li><code>senior</code></li><li><code>entry</code></li><li><code>intern</code></li></ul>
    """

    person_titles: SequenceNotStr[str]
    """Job titles held by the people you want to find.

    For a person to be included in search results, they only need to match 1 of the
    job titles you add. Adding more job titles expands your search results.

    Results also include job titles with the same terms, even if they are not exact
    matches. For example, searching for `marketing manager` might return people with
    the job title `content marketing manager`.

    Use this parameter in combination with the `person_seniorities[]` parameter to
    find people based on specific job functions and seniority levels.

    Examples: `sales development representative`; `marketing manager`;
    `research analyst`
    """

    q_keywords: str
    """A string of words over which we want to filter the results."""

    q_organization_domains_list: SequenceNotStr[str]
    """The domain name for the person's employer.

    This can be the current employer or a previous employer. Do not include `www.`,
    the `@` symbol, or similar.

    This parameter accepts up to 1,000 domains in a single request.

    Examples: `apollo.io`; `microsoft.com`
    """

    q_organization_job_titles: SequenceNotStr[str]
    """
    The job titles that are listed in active job postings at the person's current
    employer.

    Examples: `sales manager`; `research analyst`
    """

    revenue_range_max: Annotated[int, PropertyInfo(alias="revenue_range[max]")]
    """The maximum revenue the person's current employer generates.

    Use this parameter in combination with `revenue_range[min]` to set a revenue
    range.

    Do not enter currency symbols, commas, or decimal points in the figure.

    Examples: `500000`; `1500000`
    """

    revenue_range_min: Annotated[int, PropertyInfo(alias="revenue_range[min]")]
    """The minimum revenue the person's current employer generates.

    Use this parameter in combination with `revenue_range[max]` to set a revenue
    range.

    Do not enter currency symbols, commas, or decimal points in the figure.

    Examples: `500000`; `1500000`
    """
