# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PhoneCallCreateParams"]


class PhoneCallCreateParams(TypedDict, total=False):
    account_id: str
    """Associate the call with an account.

    Use the
    <a href="https://docs.apollo.io/reference/search-for-accounts#/" target="_blank">Search
    for Accounts endpoint</a> to retrieve IDs for all of the accounts within your
    Apollo account.

    Example: `66e9abf95ac32901b20d1a0d`
    """

    contact_id: str
    """Designate the contact that was called.

    Use the
    <a href="https://docs.apollo.io/reference/search-for-contacts#/" target="_blank">Search
    for Contacts endpoint</a> to retrieve IDs for all of the contacts within your
    Apollo account.

    Example: `66e34b81740c50074e3d1bd4`
    """

    duration: int
    """The duration of the call in seconds. Do not enter minutes.

    Examples: `120`; `205`
    """

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time when the call ended.

    Your entry should adhere to the ISO 8601 date-time format. Apollo uses Greenwich
    Mean Time (GMT) by default. If you do not account for time zone differences, you
    could add a end time that falls on a different day than you intended.

    The value you enter can either adhere to GMT, or you can adjust the time
    manually by specifiying in hours and minutes how much you want to offset GMT.

    Example: `2025-05-15T08:10:30Z`; `2025-05-25T10:15:30+05:00Z`
    """

    from_number: str
    """The phone number that dialed you.

    Example: `5551234567`
    """

    logged: bool
    """
    Set to `true` if you want to create an individual record for the phone call in
    Apollo.
    """

    note: str
    """Add a note to the call record.

    Example: `This lead is interested in learning more about our new product line.`
    """

    phone_call_outcome_id: str
    """Assign a call outcome to the record.

    Call outcomes are unique to your team's Apollo account. When you use the
    <b>Disposition</b> search filter for calls in the Apollo product, you can find
    the corresponding call outcome ID in the URL.

    Examples: `6095a710bd01d100a506d4c5`
    """

    phone_call_purpose_id: str
    """Assign a call purpose to the record.

    Call purposes are unique to your team's Apollo account. When you use the
    <b>Purpose</b> search filter for calls in the Apollo product, you can find the
    corresponding call purpose ID in the URL.

    Examples: `6095a710bd01d100a506d4cd`
    """

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time when the call started.

    Your entry should adhere to the ISO 8601 date-time format. Apollo uses Greenwich
    Mean Time (GMT) by default. If you do not account for time zone differences, you
    could add a start time that falls on a different day than you intended.

    The value you enter can either adhere to GMT, or you can adjust the time
    manually by specifiying in hours and minutes how much you want to offset GMT.

    Example: `2025-02-15T08:10:30Z`; `2025-03-25T10:15:30+05:00Z`
    """

    status: str
    """The status of the phone call.

    Possible values include: <ul> <li>`queued`</li> <li>`ringing`</li>
    <li>`in-progress`</li> <li>`completed`</li> <li>`no_answer`</li>
    <li>`failed`</li> <li>`busy`</li></ul>
    """

    to_number: str
    """The phone number that you dialed.

    Example: `5551234567`
    """

    user_id: SequenceNotStr[str]
    """Designate the caller in your team's Apollo account.

    Use the
    <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
    a List of Users endpoint</a> to retrieve IDs for all of the users within your
    Apollo account.

    Example: `67e33d527de088000daa60c4`
    """
