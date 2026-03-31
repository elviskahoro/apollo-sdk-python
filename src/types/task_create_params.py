# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    contact_id: Required[str]
    """
    The Apollo ID for the contact that you want to be on the receiving end of the
    action.

    To find contact IDs, call the
    <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
    for Contacts endpoint</a> and identify the `id` value for the contact.

    Example: `66e34b81740c50074e3d1bd4`
    """

    due_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The full date and time when the task will be due.

    Your entry should adhere to the
    <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6" target="_blank">ISO
    8601 date-time format</a>. Apollo uses Greenwich Mean Time (GMT) by default. If
    you do not account for time zone differences, you could add a task due date that
    falls on a different day than you intended.

    The value you enter can either adhere to GMT, or you can adjust the time
    manually by specifying in hours and minutes how much you want to offset GMT.

    Example: `2025-02-15T08:10:30Z`; `2025-03-25T10:15:30+05:00`
    """

    status: Required[str]
    """The status of the task being created.

    For future-facing tasks, you should use the `scheduled` status.

    For tasks that are already completed, you can use `completed` or `skipped`.

    Example: `scheduled`
    """

    type: Required[str]
    """Set the task to be 1 of the following task types.

    This enables the task owner to know the type of action they need to take. <ul>
    <li> `call`: Call the contact. </li> <li> `outreach_manual_email`: Email the
    contact. </li> <li> `linkedin_step_connect`: Send a LinkedIn invitation to
    connect with the contact. </li> <li> `linkedin_step_message`: Send a direct
    message to the contact's LinkedIn profile. </li> <li>
    `linkedin_step_view_profile`: View the contact's LinkedIn profile. </li> <li>
    `linkedin_step_interact_post`: Interact with the contact's recent LinkedIn
    posts. </li> <li> `action_item`: Take generic action for the contact. If you use
    this task type, Apollo recommends using the `note` parameter too. </li> </ul>
    """

    user_id: Required[str]
    """The ID for the task owner within your team's Apollo account.

    This is the user that will take action on the contacts.

    Use the
    <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
    a List of Users endpoint</a> to retrieve IDs for all of the users within your
    Apollo account.

    Example: `66302798d03b9601c7934ebf`
    """

    note: str
    """Add a description for the task. This should be a human-readable message.

    This parameter is not required, but it is recommended as it provides the task
    owner with more context on the action they need to take.

    Example:
    `This contact expressed interest in the Sequences feature specifically. Be prepared to discuss.`
    """

    priority: str
    """
    Assign a priority to the task you are creating: <ul> <li> `high` </li> <li>
    `medium` </li> <li> `low` </li> </ul>
    """

    title: str
    """A title for the task.

    If omitted, Apollo will display an auto-generated title based on the task type
    and contact name.

    Example: `Follow up on demo request`
    """
