# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EmailerCampaignAddContactsParams"]


class EmailerCampaignAddContactsParams(TypedDict, total=False):
    emailer_campaign_id: Required[str]
    """The same ID as the `sequence_id`.

    Example: `66e9e215ece19801b219997f`
    """

    send_email_from_email_account_id: Required[str]
    """
    The Apollo ID for the email account that you want to use to send emails to the
    contacts you are adding to the sequence.

    To find email account IDs, call the
    <a href="https://docs.apollo.io/reference/get-a-list-of-email-accounts" target="_blank">Get
    a List of Email Accounts endpoint</a> and identify the `id` value for the email
    account.

    Example: `6633baaece5fbd01c791d7ca`
    """

    add_if_in_queue: bool
    """
    Set to `true` if you want to add contacts even if they are currently in the
    queue for processing.
    """

    auto_unpause_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """DateTime when paused contacts should be automatically unpaused.

    Must be used with `status=paused`. Format: ISO 8601 datetime string.
    """

    contact_ids: SequenceNotStr[str]
    """The Apollo IDs for the contacts that you want to add to the sequence.

    To find contact IDs, call the
    <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
    for Contacts endpoint</a> and identify the `id` value for the contact.

    Example: `66e34b81740c50074e3d1bd4`

    Note: Either `contact_ids[]` or `label_names[]` must be provided.
    """

    contact_verification_skipped: bool
    """
    Set to `true` if you want to skip contact verification during the addition
    process.
    """

    contacts_without_ownership_permission: bool
    """
    Set to `true` if you want to add contacts even if you don't have ownership
    permission for them.
    """

    label_names: SequenceNotStr[str]
    """Alternative to `contact_ids[]`.

    Array of label names to identify contacts to add to the sequence. Contacts with
    these labels will be added to the sequence.

    Note: Either `contact_ids[]` or `label_names[]` must be provided.
    """

    send_email_from_email_address: str
    """Optional specific email address to send from within the email account."""

    sequence_active_in_other_campaigns: bool
    """
    Set to `true` if you want to add contacts to the sequence even if they have been
    added to other sequences. This parameter does not differentiate between active
    and paused sequences.
    """

    sequence_finished_in_other_campaigns: bool
    """
    Set to `true` if you want to add contacts to the sequence if they have been
    marked as `finished` in another sequence.
    """

    sequence_job_change: bool
    """
    Set to `true` if you want to add contacts to the sequence even if they have
    recently changed jobs.
    """

    sequence_no_email: bool
    """
    Set to `true` if you want to add contacts to the sequence even if they do not
    have an email address.
    """

    sequence_same_company_in_same_campaign: bool
    """
    Set to `true` if you want to add contacts to the sequence even if other contacts
    from the same company are already in the sequence.
    """

    sequence_unverified_email: bool
    """
    Set to `true` if you want to add contacts to the sequence if they have an
    unverified email address.
    """

    status: Literal["active", "paused"]
    """Initial status for added contacts.

    When set to `paused` along with `auto_unpause_at`, enables scheduled addition of
    contacts.
    """

    user_id: str
    """The ID for the user in your team's Apollo account.

    This is the user taking the action to add contacts to a sequence. When the
    sequence is updated, the activity log shows the user that added the contacts.

    Use the
    <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
    a List of Users endpoint</a> to retrieve IDs for all of the users within your
    Apollo account.

    Example: `66302798d03b9601c7934ebf`
    """
