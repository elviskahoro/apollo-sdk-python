# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import task_create_params, task_search_params, task_bulk_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.task_create_response import TaskCreateResponse
from ..types.task_search_response import TaskSearchResponse
from ..types.task_bulk_create_response import TaskBulkCreateResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        contact_id: str,
        due_at: Union[str, datetime],
        status: str,
        type: str,
        user_id: str,
        note: str | Omit = omit,
        priority: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskCreateResponse:
        """
        Use the Create a Task endpoint to create a single task in Apollo for you and
        your team. Tasks help track the upcoming actions you need to take, such as
        emailing or calling a contact.

        This endpoint returns the created task object. If you want to verify the task in
        Apollo, you can also check it in the Apollo UI or retrieve it using the
        <a href="https://docs.apollo.io/reference/search-tasks" target="_blank">Search
        for Tasks endpoint</a>.

        Apollo does not apply deduplication processes when you create a new task via the
        API. If your entry has the same task owner, contact, and other details as an
        existing task, Apollo will create a new task instead of updating the existing
        task.

        For creating multiple tasks at once, use the
        <a href="https://docs.apollo.io/reference/bulk-create-tasks" target="_blank">Bulk
        Create Tasks endpoint</a>.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          contact_id: The Apollo ID for the contact that you want to be on the receiving end of the
              action.

              To find contact IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
              for Contacts endpoint</a> and identify the `id` value for the contact.

              Example: `66e34b81740c50074e3d1bd4`

          due_at: The full date and time when the task will be due.

              Your entry should adhere to the
              <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6" target="_blank">ISO
              8601 date-time format</a>. Apollo uses Greenwich Mean Time (GMT) by default. If
              you do not account for time zone differences, you could add a task due date that
              falls on a different day than you intended.

              The value you enter can either adhere to GMT, or you can adjust the time
              manually by specifying in hours and minutes how much you want to offset GMT.

              Example: `2025-02-15T08:10:30Z`; `2025-03-25T10:15:30+05:00`

          status: The status of the task being created. For future-facing tasks, you should use
              the `scheduled` status.

              For tasks that are already completed, you can use `completed` or `skipped`.

              Example: `scheduled`

          type: Set the task to be 1 of the following task types. This enables the task owner to
              know the type of action they need to take. <ul> <li> `call`: Call the contact.
              </li> <li> `outreach_manual_email`: Email the contact. </li> <li>
              `linkedin_step_connect`: Send a LinkedIn invitation to connect with the contact.
              </li> <li> `linkedin_step_message`: Send a direct message to the contact's
              LinkedIn profile. </li> <li> `linkedin_step_view_profile`: View the contact's
              LinkedIn profile. </li> <li> `linkedin_step_interact_post`: Interact with the
              contact's recent LinkedIn posts. </li> <li> `action_item`: Take generic action
              for the contact. If you use this task type, Apollo recommends using the `note`
              parameter too. </li> </ul>

          user_id: The ID for the task owner within your team's Apollo account. This is the user
              that will take action on the contacts.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          note: Add a description for the task. This should be a human-readable message.

              This parameter is not required, but it is recommended as it provides the task
              owner with more context on the action they need to take.

              Example:
              `This contact expressed interest in the Sequences feature specifically. Be prepared to discuss.`

          priority: Assign a priority to the task you are creating: <ul> <li> `high` </li> <li>
              `medium` </li> <li> `low` </li> </ul>

          title: A title for the task. If omitted, Apollo will display an auto-generated title
              based on the task type and contact name.

              Example: `Follow up on demo request`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tasks",
            body=maybe_transform(
                {
                    "contact_id": contact_id,
                    "due_at": due_at,
                    "status": status,
                    "type": type,
                    "user_id": user_id,
                    "note": note,
                    "priority": priority,
                    "title": title,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

    def bulk_create(
        self,
        *,
        contact_ids: SequenceNotStr[str],
        due_at: Union[str, datetime],
        status: str,
        type: str,
        user_id: str,
        note: str | Omit = omit,
        priority: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskBulkCreateResponse:
        """
        Use the Bulk Create Tasks endpoint to create multiple tasks in a single API
        request. A separate task will be created for each contact provided.

        This endpoint returns a response with `success` and a `tasks` array containing
        the created tasks. If you want to verify tasks in Apollo, you can also check
        them in the Apollo UI or retrieve them using the
        <a href="https://docs.apollo.io/reference/search-tasks" target="_blank">Search
        for Tasks endpoint</a>.

        Apollo does not apply deduplication processes when you create a new task via the
        API. If your entry has the same task owner, contact, and other details as an
        existing task, Apollo will create a new task instead of updating the existing
        task.

        For creating a single task, use the
        <a href="https://docs.apollo.io/reference/create-a-task" target="_blank">Create
        a Task endpoint</a> instead.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          contact_ids: The Apollo IDs for the contacts that you want to be on the receiving end of the
              action.

              If you add multiple contact IDs, individual tasks will be created for each of
              the contacts using the same task type, due date, and other details.

              To find contact IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
              for Contacts endpoint</a> and identify the `id` value for the contact.

              Example: `66e34b81740c50074e3d1bd4`

          due_at: The full date and time when the task will be due.

              Your entry should adhere to the
              <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6" target="_blank">ISO
              8601 date-time format</a>. Apollo uses Greenwich Mean Time (GMT) by default. If
              you do not account for time zone differences, you could add a task due date that
              falls on a different day than you intended.

              The value you enter can either adhere to GMT, or you can adjust the time
              manually by specifying in hours and minutes how much you want to offset GMT.

              Example: `2025-02-15T08:10:30Z`; `2025-03-25T10:15:30+05:00`

          status: The status of the task being created. For future-facing tasks, you should use
              the `scheduled` status.

              For tasks that are already completed, you can use `completed` or `skipped`.

              Example: `scheduled`

          type: Set the task to be 1 of the following task types. This enables the task owner to
              know the type of action they need to take. <ul> <li> `call`: Call the contacts.
              </li> <li> `outreach_manual_email`: Email the contacts. </li> <li>
              `linkedin_step_connect`: Send a LinkedIn invitation to connect with the
              contacts. </li> <li> `linkedin_step_message`: Send a direct message to the
              contacts' LinkedIn profiles. </li> <li> `linkedin_step_view_profile`: View the
              contacts' LinkedIn profiles. </li> <li> `linkedin_step_interact_post`: Interact
              with the contacts' recent LinkedIn posts. </li> <li> `action_item`: Take generic
              action for the contacts. If you use this task type, Apollo recommends using the
              `note` parameter too. </li> </ul>

          user_id: The ID for the task owner within your team's Apollo account. This is the user
              that will take action on the contacts.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          note: Add a description for the task. This should be a human-readable message.

              This parameter is not required, but it is recommended as it provides the task
              owner with more context on the action they need to take.

              Example:
              `This contact expressed interest in the Sequences feature specifically. Be prepared to discuss.`

          priority: Assign a priority to the task you are creating: <ul> <li> `high` </li> <li>
              `medium` </li> <li> `low` </li> </ul>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tasks/bulk_create",
            body=maybe_transform(
                {
                    "contact_ids": contact_ids,
                    "due_at": due_at,
                    "status": status,
                    "type": type,
                    "user_id": user_id,
                    "note": note,
                    "priority": priority,
                },
                task_bulk_create_params.TaskBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskBulkCreateResponse,
        )

    def search(
        self,
        *,
        open_factor_names: SequenceNotStr[str] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort_by_field: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskSearchResponse:
        """
        Use the Search for Tasks endpoint to find tasks that your team has created in
        Apollo.

        To protect Apollo's performance for all users, this endpoint has a display limit
        of 50,000 records (100 records per page, up to 500 pages). Add more filters to
        narrow your search results as much as possible. This limitation does not
        restrict your access to Apollo's database; you just need to access the data in
        batches.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          open_factor_names: Enter `task_types` for this parameter to return a count of tasks by task type.

              When used, the response includes a `"task_types": []` array with a `"count"`
              value for each task type.

          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          sort_by_field: Sort the tasks by 1 of the following options: <ul> <li> `task_due_at`: The most
              future-dated first. </li> <li> `task_priority`: The highest priority first.
              </li> </ul>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tasks/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "open_factor_names": open_factor_names,
                        "page": page,
                        "per_page": per_page,
                        "sort_by_field": sort_by_field,
                    },
                    task_search_params.TaskSearchParams,
                ),
            ),
            cast_to=TaskSearchResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        contact_id: str,
        due_at: Union[str, datetime],
        status: str,
        type: str,
        user_id: str,
        note: str | Omit = omit,
        priority: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskCreateResponse:
        """
        Use the Create a Task endpoint to create a single task in Apollo for you and
        your team. Tasks help track the upcoming actions you need to take, such as
        emailing or calling a contact.

        This endpoint returns the created task object. If you want to verify the task in
        Apollo, you can also check it in the Apollo UI or retrieve it using the
        <a href="https://docs.apollo.io/reference/search-tasks" target="_blank">Search
        for Tasks endpoint</a>.

        Apollo does not apply deduplication processes when you create a new task via the
        API. If your entry has the same task owner, contact, and other details as an
        existing task, Apollo will create a new task instead of updating the existing
        task.

        For creating multiple tasks at once, use the
        <a href="https://docs.apollo.io/reference/bulk-create-tasks" target="_blank">Bulk
        Create Tasks endpoint</a>.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          contact_id: The Apollo ID for the contact that you want to be on the receiving end of the
              action.

              To find contact IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
              for Contacts endpoint</a> and identify the `id` value for the contact.

              Example: `66e34b81740c50074e3d1bd4`

          due_at: The full date and time when the task will be due.

              Your entry should adhere to the
              <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6" target="_blank">ISO
              8601 date-time format</a>. Apollo uses Greenwich Mean Time (GMT) by default. If
              you do not account for time zone differences, you could add a task due date that
              falls on a different day than you intended.

              The value you enter can either adhere to GMT, or you can adjust the time
              manually by specifying in hours and minutes how much you want to offset GMT.

              Example: `2025-02-15T08:10:30Z`; `2025-03-25T10:15:30+05:00`

          status: The status of the task being created. For future-facing tasks, you should use
              the `scheduled` status.

              For tasks that are already completed, you can use `completed` or `skipped`.

              Example: `scheduled`

          type: Set the task to be 1 of the following task types. This enables the task owner to
              know the type of action they need to take. <ul> <li> `call`: Call the contact.
              </li> <li> `outreach_manual_email`: Email the contact. </li> <li>
              `linkedin_step_connect`: Send a LinkedIn invitation to connect with the contact.
              </li> <li> `linkedin_step_message`: Send a direct message to the contact's
              LinkedIn profile. </li> <li> `linkedin_step_view_profile`: View the contact's
              LinkedIn profile. </li> <li> `linkedin_step_interact_post`: Interact with the
              contact's recent LinkedIn posts. </li> <li> `action_item`: Take generic action
              for the contact. If you use this task type, Apollo recommends using the `note`
              parameter too. </li> </ul>

          user_id: The ID for the task owner within your team's Apollo account. This is the user
              that will take action on the contacts.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          note: Add a description for the task. This should be a human-readable message.

              This parameter is not required, but it is recommended as it provides the task
              owner with more context on the action they need to take.

              Example:
              `This contact expressed interest in the Sequences feature specifically. Be prepared to discuss.`

          priority: Assign a priority to the task you are creating: <ul> <li> `high` </li> <li>
              `medium` </li> <li> `low` </li> </ul>

          title: A title for the task. If omitted, Apollo will display an auto-generated title
              based on the task type and contact name.

              Example: `Follow up on demo request`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tasks",
            body=await async_maybe_transform(
                {
                    "contact_id": contact_id,
                    "due_at": due_at,
                    "status": status,
                    "type": type,
                    "user_id": user_id,
                    "note": note,
                    "priority": priority,
                    "title": title,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

    async def bulk_create(
        self,
        *,
        contact_ids: SequenceNotStr[str],
        due_at: Union[str, datetime],
        status: str,
        type: str,
        user_id: str,
        note: str | Omit = omit,
        priority: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskBulkCreateResponse:
        """
        Use the Bulk Create Tasks endpoint to create multiple tasks in a single API
        request. A separate task will be created for each contact provided.

        This endpoint returns a response with `success` and a `tasks` array containing
        the created tasks. If you want to verify tasks in Apollo, you can also check
        them in the Apollo UI or retrieve them using the
        <a href="https://docs.apollo.io/reference/search-tasks" target="_blank">Search
        for Tasks endpoint</a>.

        Apollo does not apply deduplication processes when you create a new task via the
        API. If your entry has the same task owner, contact, and other details as an
        existing task, Apollo will create a new task instead of updating the existing
        task.

        For creating a single task, use the
        <a href="https://docs.apollo.io/reference/create-a-task" target="_blank">Create
        a Task endpoint</a> instead.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          contact_ids: The Apollo IDs for the contacts that you want to be on the receiving end of the
              action.

              If you add multiple contact IDs, individual tasks will be created for each of
              the contacts using the same task type, due date, and other details.

              To find contact IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
              for Contacts endpoint</a> and identify the `id` value for the contact.

              Example: `66e34b81740c50074e3d1bd4`

          due_at: The full date and time when the task will be due.

              Your entry should adhere to the
              <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6" target="_blank">ISO
              8601 date-time format</a>. Apollo uses Greenwich Mean Time (GMT) by default. If
              you do not account for time zone differences, you could add a task due date that
              falls on a different day than you intended.

              The value you enter can either adhere to GMT, or you can adjust the time
              manually by specifying in hours and minutes how much you want to offset GMT.

              Example: `2025-02-15T08:10:30Z`; `2025-03-25T10:15:30+05:00`

          status: The status of the task being created. For future-facing tasks, you should use
              the `scheduled` status.

              For tasks that are already completed, you can use `completed` or `skipped`.

              Example: `scheduled`

          type: Set the task to be 1 of the following task types. This enables the task owner to
              know the type of action they need to take. <ul> <li> `call`: Call the contacts.
              </li> <li> `outreach_manual_email`: Email the contacts. </li> <li>
              `linkedin_step_connect`: Send a LinkedIn invitation to connect with the
              contacts. </li> <li> `linkedin_step_message`: Send a direct message to the
              contacts' LinkedIn profiles. </li> <li> `linkedin_step_view_profile`: View the
              contacts' LinkedIn profiles. </li> <li> `linkedin_step_interact_post`: Interact
              with the contacts' recent LinkedIn posts. </li> <li> `action_item`: Take generic
              action for the contacts. If you use this task type, Apollo recommends using the
              `note` parameter too. </li> </ul>

          user_id: The ID for the task owner within your team's Apollo account. This is the user
              that will take action on the contacts.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> to retrieve IDs for all of the users within your
              Apollo account.

              Example: `66302798d03b9601c7934ebf`

          note: Add a description for the task. This should be a human-readable message.

              This parameter is not required, but it is recommended as it provides the task
              owner with more context on the action they need to take.

              Example:
              `This contact expressed interest in the Sequences feature specifically. Be prepared to discuss.`

          priority: Assign a priority to the task you are creating: <ul> <li> `high` </li> <li>
              `medium` </li> <li> `low` </li> </ul>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tasks/bulk_create",
            body=await async_maybe_transform(
                {
                    "contact_ids": contact_ids,
                    "due_at": due_at,
                    "status": status,
                    "type": type,
                    "user_id": user_id,
                    "note": note,
                    "priority": priority,
                },
                task_bulk_create_params.TaskBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskBulkCreateResponse,
        )

    async def search(
        self,
        *,
        open_factor_names: SequenceNotStr[str] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort_by_field: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskSearchResponse:
        """
        Use the Search for Tasks endpoint to find tasks that your team has created in
        Apollo.

        To protect Apollo's performance for all users, this endpoint has a display limit
        of 50,000 records (100 records per page, up to 500 pages). Add more filters to
        narrow your search results as much as possible. This limitation does not
        restrict your access to Apollo's database; you just need to access the data in
        batches.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          open_factor_names: Enter `task_types` for this parameter to return a count of tasks by task type.

              When used, the response includes a `"task_types": []` array with a `"count"`
              value for each task type.

          page: The page number of the Apollo data that you want to retrieve.

              Use this parameter in combination with the `per_page` parameter to make search
              results for navigable and improve the performance of the endpoint.

              Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance.

              Use the `page` parameter to search the different pages of data.

              Example: `10`

          sort_by_field: Sort the tasks by 1 of the following options: <ul> <li> `task_due_at`: The most
              future-dated first. </li> <li> `task_priority`: The highest priority first.
              </li> </ul>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tasks/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "open_factor_names": open_factor_names,
                        "page": page,
                        "per_page": per_page,
                        "sort_by_field": sort_by_field,
                    },
                    task_search_params.TaskSearchParams,
                ),
            ),
            cast_to=TaskSearchResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.bulk_create = to_raw_response_wrapper(
            tasks.bulk_create,
        )
        self.search = to_raw_response_wrapper(
            tasks.search,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            tasks.bulk_create,
        )
        self.search = async_to_raw_response_wrapper(
            tasks.search,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.bulk_create = to_streamed_response_wrapper(
            tasks.bulk_create,
        )
        self.search = to_streamed_response_wrapper(
            tasks.search,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            tasks.bulk_create,
        )
        self.search = async_to_streamed_response_wrapper(
            tasks.search,
        )
