# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EmailerCampaignUpdateContactStatusParams"]


class EmailerCampaignUpdateContactStatusParams(TypedDict, total=False):
    contact_ids: Required[SequenceNotStr[str]]
    """The Apollo IDs for the contacts in the sequences.

    These are the contacts whose sequence status you want to update.

    To find contact IDs, call the
    <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
    for Contacts endpoint</a> and identify the `id` value for the contact.

    Example: `66e34b81740c50074e3d1bd4`
    """

    emailer_campaign_ids: Required[SequenceNotStr[str]]
    """The Apollo IDs for the sequences that you want to update.

    If you add multiple sequences, you will update the status of the contacts across
    the chosen sequences.

    To find sequence IDs, call the
    <a href="https://docs.apollo.io/reference/search-for-sequences" target="_blank">Search
    for Sequences endpoint</a> and identify the `id` value for the sequence.

    Example: `66e9e215ece19801b219997f`
    """

    mode: Required[str]
    """
    Choose 1 of the following options to update the sequence status of the contacts:
    <ul> <li> `mark_as_finished`: Mark the contacts as having finished the sequence.
    </li> <li> `remove`: Remove the contacts from the sequence. </li> <li> `stop`:
    Indicate that the contacts progress in the sequence has halted. </li> </ul>
    """
