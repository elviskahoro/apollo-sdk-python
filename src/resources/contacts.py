# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Iterable, cast

import httpx

from ..types import (
    contact_create_params,
    contact_search_params,
    contact_update_params,
    contact_bulk_create_params,
    contact_bulk_update_params,
    contact_update_owners_params,
    contact_update_stages_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform, bracket_array_query_param
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.contact_create_response import ContactCreateResponse
from ..types.contact_search_response import ContactSearchResponse
from ..types.contact_update_response import ContactUpdateResponse
from ..types.contact_retrieve_response import ContactRetrieveResponse
from ..types.contact_bulk_create_response import ContactBulkCreateResponse
from ..types.contact_bulk_update_response import ContactBulkUpdateResponse
from ..types.contact_update_owners_response import ContactUpdateOwnersResponse
from ..types.contact_update_stages_response import ContactUpdateStagesResponse

__all__ = ["ContactsResource", "AsyncContactsResource"]


class ContactsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return ContactsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str | Omit = omit,
        contact_stage_id: str | Omit = omit,
        corporate_phone: str | Omit = omit,
        direct_phone: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        home_phone: str | Omit = omit,
        label_names: SequenceNotStr[str] | Omit = omit,
        last_name: str | Omit = omit,
        mobile_phone: str | Omit = omit,
        organization_name: str | Omit = omit,
        other_phone: str | Omit = omit,
        present_raw_address: str | Omit = omit,
        run_dedupe: bool | Omit = omit,
        title: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        website_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCreateResponse:
        """
        Use the Create a Contact endpoint to add a new contact to your team's Apollo
        account.

        In Apollo terminology, a contact is a person that your team has explicitly added
        to your database. A contact will have their data enriched in some way, such as
        accessing an email address or a phone number.

        By default, Apollo does not apply deduplication processes when you create a new
        contact via the API. If your entry has the same name, email address, or other
        details as an existing contact, Apollo will create a new contact instead of
        updating the existing contact. To enable deduplication and prevent duplicate
        contacts, set the `run_dedupe` parameter to `true`.

        To update an existing contact, use the
        <a href="https://docs.apollo.io/reference/update-a-contact" target="_blank">Update
        a Contact endpoint</a> instead.

        Args:
          account_id: The Apollo ID for the account. Example: `63f53afe4ceeca00016bdd2f`

          contact_stage_id: The Apollo ID for the contact stage. Example: `6095a710bd01d100a506d4ae`

          corporate_phone: The work/office phone number. Example: `+44 7911 123456`

          direct_phone: The primary phone number. Example: `555-303-1234`

          email: The email address of the contact. Example: `example@email.com`

          first_name: The first name of the contact you want to create. Example: `Tim`

          home_phone: The home phone number. Example: `555-303-1234`

          label_names: Lists to which the contact belongs.

          last_name: The last name of the contact you want to create. Example: `Zheng`

          mobile_phone: The mobile phone number. Example: `555-303-1234`

          organization_name: The name of the contact's employer (company). Example: `apollo`

          other_phone: Alternative phone number. Example: `555-303-1234`

          present_raw_address: The personal location for the contact. Example: `Atlanta, United States`

          run_dedupe: Set to `true` to enable deduplication logic that prevents creating duplicate
              contacts. When enabled, Apollo will check for existing contacts with matching
              email addresses, names, or other identifying information and return the existing
              contact instead of creating a duplicate. The default value is `false`.

              When deduplication is enabled, performance may be slightly impacted due to the
              additional validation checks, but this ensures data integrity and prevents
              duplicate entries in your database.

          title: The current job title that the contact holds. Example: `senior research analyst`

          typed_custom_fields: Add information to
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498825869-Create-Custom-Contact-Fields" target="_blank">custom
              fields</a> in Apollo.

              <b>Your custom fields are unique to your team's Apollo account. This means that
              the examples in this documentation may not work for your testing purposes.</b>

              To utilize this parameter successfully, call the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint and identify the `id` value for the
              custom field, as well as the appropriate data type. For example, if a custom
              field accepts picklist entries, you need to pass the accompanying `id` value for
              the picklist entry that you want to use as the input value.

              <b>Example</b>: When the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint returns an `id` of field:

              - `"60c39ed82bd02f01154c470a"` (datetime)

              then the value passed should be:

              `{"60c39ed82bd02f01154c470a": "2025-08-07"}`

          website_url: The corporate website URL. Example: `https://www.apollo.io/`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contacts",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "contact_stage_id": contact_stage_id,
                    "corporate_phone": corporate_phone,
                    "direct_phone": direct_phone,
                    "email": email,
                    "first_name": first_name,
                    "home_phone": home_phone,
                    "label_names": label_names,
                    "last_name": last_name,
                    "mobile_phone": mobile_phone,
                    "organization_name": organization_name,
                    "other_phone": other_phone,
                    "present_raw_address": present_raw_address,
                    "run_dedupe": run_dedupe,
                    "title": title,
                    "typed_custom_fields": typed_custom_fields,
                    "website_url": website_url,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCreateResponse,
        )

    def retrieve(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactRetrieveResponse:
        """
        Use the View a Contact endpoint to retrieve details for an existing contact in
        your team's Apollo database. In Apollo terminology, a contact is a person that
        your team has explicitly added to your database.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._get(
            path_template("/contacts/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactRetrieveResponse,
        )

    def update(
        self,
        contact_id: str,
        *,
        account_id: str | Omit = omit,
        contact_stage_id: str | Omit = omit,
        corporate_phone: str | Omit = omit,
        direct_phone: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        home_phone: str | Omit = omit,
        label_names: SequenceNotStr[str] | Omit = omit,
        last_name: str | Omit = omit,
        mobile_phone: str | Omit = omit,
        organization_name: str | Omit = omit,
        other_phone: str | Omit = omit,
        present_raw_address: str | Omit = omit,
        title: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        website_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactUpdateResponse:
        """
        Use the Update a Contact endpoint to update existing contacts in your team's
        Apollo account.

        In Apollo terminology, a contact is a person that your team has explicitly added
        to your database. A contact will have their data enriched in some way, such as
        accessing an email address or a phone number.

        To create a new contact, use the
        <a href="https://docs.apollo.io/reference/create-a-contact" target="_blank">Create
        a Contact endpoint</a> instead. To update the contact stage for multiple
        contacts, use the
        <a href="https://docs.apollo.io/reference/update-contact-stage" target="_blank">Update
        Contact Stage for Multiple Contacts</a> endpoint.

        Args:
          account_id: Update the account ID. Example: `63f53afe4ceeca00016bdd2f`

          contact_stage_id: Update the contact stage ID. Example: `6095a710bd01d100a506d4af`

          corporate_phone: Work/office phone.

          direct_phone: Primary phone.

          email: Update the contact email. Example: `example@email.com`

          first_name: Update the contact's first name. Example: `Tim`

          home_phone: Home phone.

          label_names: Replace lists this contact belongs to. (Passing new values will overwrite
              existing lists.)

          last_name: Update the contact's last name. Example: `Zheng`

          mobile_phone: Mobile phone.

          organization_name: Update the employer (company) name. Example: `apollo`

          other_phone: Alternate phone.

          present_raw_address: Update location (city/state/country). Example: `Atlanta, United States`

          title: Update the job title. Example: `senior research analyst`

          typed_custom_fields: Add information to
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498825869-Create-Custom-Contact-Fields" target="_blank">custom
              fields</a> in Apollo.

              <b>Your custom fields are unique to your team's Apollo account. This means that
              the examples in this documentation may not work for your testing purposes.</b>

              To utilize this parameter successfully, call the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint and identify the `id` value for the
              custom field, as well as the appropriate data type. For example, if a custom
              field accepts picklist entries, you need to pass the accompanying `id` value for
              the picklist entry that you want to use as the input value.

              <b>Example</b>: When the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint returns an `id` of field:

              - `"60c39ed82bd02f01154c470a"` (datetime)

              then the value passed should be:

              `{"60c39ed82bd02f01154c470a": "2025-08-07"}`

          website_url: Update the employer website URL. Example: `https://www.apollo.io/`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._patch(
            path_template("/contacts/{contact_id}", contact_id=contact_id),
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "contact_stage_id": contact_stage_id,
                    "corporate_phone": corporate_phone,
                    "direct_phone": direct_phone,
                    "email": email,
                    "first_name": first_name,
                    "home_phone": home_phone,
                    "label_names": label_names,
                    "last_name": last_name,
                    "mobile_phone": mobile_phone,
                    "organization_name": organization_name,
                    "other_phone": other_phone,
                    "present_raw_address": present_raw_address,
                    "title": title,
                    "typed_custom_fields": typed_custom_fields,
                    "website_url": website_url,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactUpdateResponse,
        )

    def bulk_create(
        self,
        *,
        contacts: Iterable[contact_bulk_create_params.Contact],
        append_label_names: SequenceNotStr[str] | Omit = omit,
        run_dedupe: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactBulkCreateResponse:
        """
        Use the Bulk Create Contacts endpoint to create up to 100 contacts in a single
        API request. This endpoint supports intelligent deduplication and returns
        separate arrays for newly created and existing contacts.

        <strong>Important:</strong> This endpoint creates new contacts but does NOT
        update existing ones (except for placeholder contacts from email imports).
        Existing contacts that match the criteria will be returned in the
        existing_contacts array without modification. To update existing contacts, use
        the
        <a href="https://docs.apollo.io/reference/bulk-update-contacts" target="_blank">Bulk
        Update Contacts endpoint</a>.

        The endpoint can operate in two modes: default mode (creates duplicates for
        non-email_import sources, merges with email_import placeholders only) or full
        deduplication mode (returns existing contacts without modifying them).

        For creating individual contacts, use the
        <a href="https://docs.apollo.io/reference/create-a-contact" target="_blank">Create
        a Contact endpoint</a> instead.

        Args:
          contacts: Array of contact objects to create (maximum 100 contacts per request)

          append_label_names: Array of label names to add to ALL contacts in this request

          run_dedupe: Enable full deduplication across all sources. When false (default), creates
              duplicates for non-email_import sources and merges with email_import
              placeholders only. When true, returns existing contacts without modifying them
              (except email_import placeholders which are still merged). Matches by email, CRM
              IDs, or name + organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contacts/bulk_create",
            body=maybe_transform(
                {
                    "contacts": contacts,
                    "append_label_names": append_label_names,
                    "run_dedupe": run_dedupe,
                },
                contact_bulk_create_params.ContactBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactBulkCreateResponse,
        )

    def bulk_update(
        self,
        *,
        account_id: str | Omit = omit,
        async_: bool | Omit = omit,
        contact_attributes: Iterable[contact_bulk_update_params.ContactAttribute] | Omit = omit,
        contact_ids: SequenceNotStr[str] | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        linkedin_url: str | Omit = omit,
        organization_name: str | Omit = omit,
        owner_id: str | Omit = omit,
        present_raw_address: str | Omit = omit,
        title: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        visible_entity_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactBulkUpdateResponse:
        """
        Use the Bulk Update Contacts endpoint to update multiple contacts in your team's
        Apollo account simultaneously.

        This endpoint allows you to update common fields across multiple contacts
        efficiently, such as contact stages, owners, custom fields, and other contact
        attributes.

        You can update up to 1000 contacts per request. For batches larger than 100
        contacts, the system will process the updates asynchronously and return a job ID
        to track progress.

        For updating individual contacts, use the
        <a href="https://docs.apollo.io/reference/update-a-contact" target="_blank">Update
        a Contact endpoint</a> instead.

        Args:
          account_id: When using contact_ids, apply this account ID to all contacts

          async_: Force asynchronous processing. Automatically enabled for >100 contacts.

          contact_attributes: Array of contact objects with individual updates. Use this for applying
              different updates to each contact.

          contact_ids: Array of contact IDs to update with the same values. Use this for applying the
              same updates to multiple contacts.

          email: When using contact_ids, apply this email to all contacts

          first_name: When using contact_ids, apply this first name to all contacts

          last_name: When using contact_ids, apply this last name to all contacts

          linkedin_url: When using contact_ids, apply this LinkedIn URL to all contacts

          organization_name: When using contact_ids, apply this organization name to all contacts

          owner_id: When using contact_ids, apply this owner to all contacts

          present_raw_address: When using contact_ids, apply this address to all contacts

          title: When using contact_ids, apply this title to all contacts

          typed_custom_fields: When using contact_ids, apply these custom fields to all contacts

          visible_entity_ids: Specific contact IDs to return in the response (for performance)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body_data = {
            "account_id": account_id,
            "async_": async_,
            "contact_attributes": contact_attributes,
            "contact_ids": contact_ids,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "linkedin_url": linkedin_url,
            "organization_name": organization_name,
            "owner_id": owner_id,
            "present_raw_address": present_raw_address,
            "title": title,
            "typed_custom_fields": typed_custom_fields,
            "visible_entity_ids": visible_entity_ids,
        }
        if contact_attributes is omit and contact_ids is omit:
            body_data["contact_ids"] = ["string"]

        return cast(
            ContactBulkUpdateResponse,
            self._post(
                "/contacts/bulk_update",
                body=maybe_transform(
                    body_data,
                    contact_bulk_update_params.ContactBulkUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ContactBulkUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def search(
        self,
        *,
        contact_label_ids: SequenceNotStr[str] | Omit = omit,
        contact_stage_ids: SequenceNotStr[str] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        q_keywords: str | Omit = omit,
        sort_ascending: bool | Omit = omit,
        sort_by_field: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactSearchResponse:
        """
        Use the Search for Contacts endpoint to search for the contacts that have been
        added to your team's Apollo account.

        In Apollo terminology, a contact is a person that your team has explicitly added
        to your database. A contact will have their data enriched in some way, such as
        accessing an email address or a phone number.

        This endpoint only returns contacts in the search results. To search for people
        in the Apollo database, call the
        <a href="https://docs.apollo.io/reference/people-api-search" target="_blank">People
        API Search endpoint</a>.

        To protect Apollo's performance for all users, this endpoint has a display limit
        of 50,000 records (100 records per page, up to 500 pages). Add more filters to
        narrow your search results as much as possible. This limitation does not
        restrict your access to Apollo's database; you just need to access the data in
        batches.

        Args:
          contact_label_ids: The Apollo IDs for the labels that you want to include in your search results.
              If you add multiple labels, Apollo will include all contacts connected to any of
              the labels, along with the other parameters, in the search results. Example:
              `['6095a710bd01d100a506d4ae']`

          contact_stage_ids: The Apollo IDs for the contact stages that you want to include in your search
              results. If you add multiple contact stages, Apollo will include all contacts
              that match any of the stages, along with the other parameters, in the search
              results. Call the
              [List Contact Stages endpoint](https://docs.apollo.io/reference/list-contact-stages)
              to retrieve a list of all the contact stage IDs available in your Apollo
              account. Example: `6095a710bd01d100a506d4ae`

          page: The page number of the Apollo data that you want to retrieve. Use this parameter
              in combination with the `per_page` parameter to make search results navigable
              and improve the performance of the endpoint. Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance. Use the `page`
              parameter to search the different pages of data. Example: `10`

          q_keywords: Add keywords to narrow the search of the contacts in your team's Apollo account.
              Keywords can include combinations of names, job titles, employers (company
              names), and email addresses. Examples: `tim zheng`; `senior research analyst`;
              `microsoft`

          sort_ascending: Set to `true` to sort the matching contacts in ascending order. This parameter
              must be used with `sort_by_field`. Otherwise, the sorting logic is not applied.
              Example: `true`

          sort_by_field:
              Sort the matching contacts by 1 of the following options:

              - `contact_last_activity_date`: The most recent activity date recorded first.
              - `contact_email_last_opened_at`: The most recent email opened date first.
              - `contact_email_last_clicked_at`: The most recent email clicked first.
              - `contact_created_at`: The most recently created first.
              - `contact_updated_at`: The most recently updated first.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contacts/search",
            body=maybe_transform(
                {
                    "contact_label_ids": contact_label_ids,
                    "contact_stage_ids": contact_stage_ids,
                    "page": page,
                    "per_page": per_page,
                    "q_keywords": q_keywords,
                    "sort_ascending": sort_ascending,
                    "sort_by_field": sort_by_field,
                },
                contact_search_params.ContactSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactSearchResponse,
        )

    def update_owners(
        self,
        *,
        contact_ids: SequenceNotStr[str],
        owner_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactUpdateOwnersResponse:
        """
        Use the Update Contact Owner for Multiple Contacts endpoint to assign multiple
        contacts to a different user in your team's Apollo account.

        To update more than the contact's owner, such as job titles or contact details,
        use the
        <a href="https://docs.apollo.io/reference/update-a-contact" target="_blank">Update
        a Contact endpoint</a> instead.

        Args:
          contact_ids: The Apollo IDs for the contacts that you want assign to an owner.

              To find contact IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
              for Contacts endpoint</a> and identify the `id` value for the contact.

              Example: `66e34b81740c50074e3d1bd4`

          owner_id: The ID for the contact owner within your team's Apollo account. This user will
              be assigned ownership of the contacts.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> endpoint to retrieve IDs for all of the users
              within your Apollo account.

              Example: `66302798d03b9601c7934ebf`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contacts/update_owners",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query={**bracket_array_query_param("contact_ids", contact_ids), "owner_id": owner_id},
            ),
            cast_to=ContactUpdateOwnersResponse,
        )

    def update_stages(
        self,
        *,
        contact_ids: SequenceNotStr[str],
        contact_stage_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactUpdateStagesResponse:
        """
        Use the Update Contact Stage for Multiple Contacts endpoint to update the
        contact stage for several contacts in your team's Apollo account.

        To update more than the contact stage, such as job titles or contact details,
        use the
        <a href="https://docs.apollo.io/reference/update-a-contact" target="_blank">Update
        a Contact endpoint</a> instead.

        Args:
          contact_ids: The Apollo IDs for the contacts that you want to update.

              To find contact IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
              for Contacts endpoint</a> and identify the `id` value for the contact.

              Example: `66e34b81740c50074e3d1bd4`

          contact_stage_id: The Apollo ID for the contact stage to which you want to assign the contacts.
              Call the
              <a href="https://docs.apollo.io/reference/list-contact-stages" target="_blank">List
              Contact Stages endpoint</a> to retrieve a list of all the contact stage IDs
              available in your Apollo account.

              Example: `6095a710bd01d100a506d4af`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contacts/update_stages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query={
                    **bracket_array_query_param("contact_ids", contact_ids),
                    "contact_stage_id": contact_stage_id,
                },
            ),
            cast_to=ContactUpdateStagesResponse,
        )


class AsyncContactsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/apollo-sdk-python#with_streaming_response
        """
        return AsyncContactsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str | Omit = omit,
        contact_stage_id: str | Omit = omit,
        corporate_phone: str | Omit = omit,
        direct_phone: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        home_phone: str | Omit = omit,
        label_names: SequenceNotStr[str] | Omit = omit,
        last_name: str | Omit = omit,
        mobile_phone: str | Omit = omit,
        organization_name: str | Omit = omit,
        other_phone: str | Omit = omit,
        present_raw_address: str | Omit = omit,
        run_dedupe: bool | Omit = omit,
        title: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        website_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCreateResponse:
        """
        Use the Create a Contact endpoint to add a new contact to your team's Apollo
        account.

        In Apollo terminology, a contact is a person that your team has explicitly added
        to your database. A contact will have their data enriched in some way, such as
        accessing an email address or a phone number.

        By default, Apollo does not apply deduplication processes when you create a new
        contact via the API. If your entry has the same name, email address, or other
        details as an existing contact, Apollo will create a new contact instead of
        updating the existing contact. To enable deduplication and prevent duplicate
        contacts, set the `run_dedupe` parameter to `true`.

        To update an existing contact, use the
        <a href="https://docs.apollo.io/reference/update-a-contact" target="_blank">Update
        a Contact endpoint</a> instead.

        Args:
          account_id: The Apollo ID for the account. Example: `63f53afe4ceeca00016bdd2f`

          contact_stage_id: The Apollo ID for the contact stage. Example: `6095a710bd01d100a506d4ae`

          corporate_phone: The work/office phone number. Example: `+44 7911 123456`

          direct_phone: The primary phone number. Example: `555-303-1234`

          email: The email address of the contact. Example: `example@email.com`

          first_name: The first name of the contact you want to create. Example: `Tim`

          home_phone: The home phone number. Example: `555-303-1234`

          label_names: Lists to which the contact belongs.

          last_name: The last name of the contact you want to create. Example: `Zheng`

          mobile_phone: The mobile phone number. Example: `555-303-1234`

          organization_name: The name of the contact's employer (company). Example: `apollo`

          other_phone: Alternative phone number. Example: `555-303-1234`

          present_raw_address: The personal location for the contact. Example: `Atlanta, United States`

          run_dedupe: Set to `true` to enable deduplication logic that prevents creating duplicate
              contacts. When enabled, Apollo will check for existing contacts with matching
              email addresses, names, or other identifying information and return the existing
              contact instead of creating a duplicate. The default value is `false`.

              When deduplication is enabled, performance may be slightly impacted due to the
              additional validation checks, but this ensures data integrity and prevents
              duplicate entries in your database.

          title: The current job title that the contact holds. Example: `senior research analyst`

          typed_custom_fields: Add information to
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498825869-Create-Custom-Contact-Fields" target="_blank">custom
              fields</a> in Apollo.

              <b>Your custom fields are unique to your team's Apollo account. This means that
              the examples in this documentation may not work for your testing purposes.</b>

              To utilize this parameter successfully, call the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint and identify the `id` value for the
              custom field, as well as the appropriate data type. For example, if a custom
              field accepts picklist entries, you need to pass the accompanying `id` value for
              the picklist entry that you want to use as the input value.

              <b>Example</b>: When the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint returns an `id` of field:

              - `"60c39ed82bd02f01154c470a"` (datetime)

              then the value passed should be:

              `{"60c39ed82bd02f01154c470a": "2025-08-07"}`

          website_url: The corporate website URL. Example: `https://www.apollo.io/`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contacts",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "contact_stage_id": contact_stage_id,
                    "corporate_phone": corporate_phone,
                    "direct_phone": direct_phone,
                    "email": email,
                    "first_name": first_name,
                    "home_phone": home_phone,
                    "label_names": label_names,
                    "last_name": last_name,
                    "mobile_phone": mobile_phone,
                    "organization_name": organization_name,
                    "other_phone": other_phone,
                    "present_raw_address": present_raw_address,
                    "run_dedupe": run_dedupe,
                    "title": title,
                    "typed_custom_fields": typed_custom_fields,
                    "website_url": website_url,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCreateResponse,
        )

    async def retrieve(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactRetrieveResponse:
        """
        Use the View a Contact endpoint to retrieve details for an existing contact in
        your team's Apollo database. In Apollo terminology, a contact is a person that
        your team has explicitly added to your database.

        This endpoint requires a master API key. If you attempt to call the endpoint
        without a master key, you will receive a `403` response. Refer to
        <a href="https://docs.apollo.io/docs/create-api-key" target="_blank">Create API
        Keys</a> to learn how to create a master API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._get(
            path_template("/contacts/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactRetrieveResponse,
        )

    async def update(
        self,
        contact_id: str,
        *,
        account_id: str | Omit = omit,
        contact_stage_id: str | Omit = omit,
        corporate_phone: str | Omit = omit,
        direct_phone: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        home_phone: str | Omit = omit,
        label_names: SequenceNotStr[str] | Omit = omit,
        last_name: str | Omit = omit,
        mobile_phone: str | Omit = omit,
        organization_name: str | Omit = omit,
        other_phone: str | Omit = omit,
        present_raw_address: str | Omit = omit,
        title: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        website_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactUpdateResponse:
        """
        Use the Update a Contact endpoint to update existing contacts in your team's
        Apollo account.

        In Apollo terminology, a contact is a person that your team has explicitly added
        to your database. A contact will have their data enriched in some way, such as
        accessing an email address or a phone number.

        To create a new contact, use the
        <a href="https://docs.apollo.io/reference/create-a-contact" target="_blank">Create
        a Contact endpoint</a> instead. To update the contact stage for multiple
        contacts, use the
        <a href="https://docs.apollo.io/reference/update-contact-stage" target="_blank">Update
        Contact Stage for Multiple Contacts</a> endpoint.

        Args:
          account_id: Update the account ID. Example: `63f53afe4ceeca00016bdd2f`

          contact_stage_id: Update the contact stage ID. Example: `6095a710bd01d100a506d4af`

          corporate_phone: Work/office phone.

          direct_phone: Primary phone.

          email: Update the contact email. Example: `example@email.com`

          first_name: Update the contact's first name. Example: `Tim`

          home_phone: Home phone.

          label_names: Replace lists this contact belongs to. (Passing new values will overwrite
              existing lists.)

          last_name: Update the contact's last name. Example: `Zheng`

          mobile_phone: Mobile phone.

          organization_name: Update the employer (company) name. Example: `apollo`

          other_phone: Alternate phone.

          present_raw_address: Update location (city/state/country). Example: `Atlanta, United States`

          title: Update the job title. Example: `senior research analyst`

          typed_custom_fields: Add information to
              <a href="https://knowledge.apollo.io/hc/en-us/articles/4412498825869-Create-Custom-Contact-Fields" target="_blank">custom
              fields</a> in Apollo.

              <b>Your custom fields are unique to your team's Apollo account. This means that
              the examples in this documentation may not work for your testing purposes.</b>

              To utilize this parameter successfully, call the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint and identify the `id` value for the
              custom field, as well as the appropriate data type. For example, if a custom
              field accepts picklist entries, you need to pass the accompanying `id` value for
              the picklist entry that you want to use as the input value.

              <b>Example</b>: When the
              <a href="https://docs.apollo.io/reference/get-a-list-of-all-custom-fields">Get a
              List of All Custom Fields</a> endpoint returns an `id` of field:

              - `"60c39ed82bd02f01154c470a"` (datetime)

              then the value passed should be:

              `{"60c39ed82bd02f01154c470a": "2025-08-07"}`

          website_url: Update the employer website URL. Example: `https://www.apollo.io/`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._patch(
            path_template("/contacts/{contact_id}", contact_id=contact_id),
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "contact_stage_id": contact_stage_id,
                    "corporate_phone": corporate_phone,
                    "direct_phone": direct_phone,
                    "email": email,
                    "first_name": first_name,
                    "home_phone": home_phone,
                    "label_names": label_names,
                    "last_name": last_name,
                    "mobile_phone": mobile_phone,
                    "organization_name": organization_name,
                    "other_phone": other_phone,
                    "present_raw_address": present_raw_address,
                    "title": title,
                    "typed_custom_fields": typed_custom_fields,
                    "website_url": website_url,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactUpdateResponse,
        )

    async def bulk_create(
        self,
        *,
        contacts: Iterable[contact_bulk_create_params.Contact],
        append_label_names: SequenceNotStr[str] | Omit = omit,
        run_dedupe: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactBulkCreateResponse:
        """
        Use the Bulk Create Contacts endpoint to create up to 100 contacts in a single
        API request. This endpoint supports intelligent deduplication and returns
        separate arrays for newly created and existing contacts.

        <strong>Important:</strong> This endpoint creates new contacts but does NOT
        update existing ones (except for placeholder contacts from email imports).
        Existing contacts that match the criteria will be returned in the
        existing_contacts array without modification. To update existing contacts, use
        the
        <a href="https://docs.apollo.io/reference/bulk-update-contacts" target="_blank">Bulk
        Update Contacts endpoint</a>.

        The endpoint can operate in two modes: default mode (creates duplicates for
        non-email_import sources, merges with email_import placeholders only) or full
        deduplication mode (returns existing contacts without modifying them).

        For creating individual contacts, use the
        <a href="https://docs.apollo.io/reference/create-a-contact" target="_blank">Create
        a Contact endpoint</a> instead.

        Args:
          contacts: Array of contact objects to create (maximum 100 contacts per request)

          append_label_names: Array of label names to add to ALL contacts in this request

          run_dedupe: Enable full deduplication across all sources. When false (default), creates
              duplicates for non-email_import sources and merges with email_import
              placeholders only. When true, returns existing contacts without modifying them
              (except email_import placeholders which are still merged). Matches by email, CRM
              IDs, or name + organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contacts/bulk_create",
            body=await async_maybe_transform(
                {
                    "contacts": contacts,
                    "append_label_names": append_label_names,
                    "run_dedupe": run_dedupe,
                },
                contact_bulk_create_params.ContactBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactBulkCreateResponse,
        )

    async def bulk_update(
        self,
        *,
        account_id: str | Omit = omit,
        async_: bool | Omit = omit,
        contact_attributes: Iterable[contact_bulk_update_params.ContactAttribute] | Omit = omit,
        contact_ids: SequenceNotStr[str] | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        linkedin_url: str | Omit = omit,
        organization_name: str | Omit = omit,
        owner_id: str | Omit = omit,
        present_raw_address: str | Omit = omit,
        title: str | Omit = omit,
        typed_custom_fields: Dict[str, str] | Omit = omit,
        visible_entity_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactBulkUpdateResponse:
        """
        Use the Bulk Update Contacts endpoint to update multiple contacts in your team's
        Apollo account simultaneously.

        This endpoint allows you to update common fields across multiple contacts
        efficiently, such as contact stages, owners, custom fields, and other contact
        attributes.

        You can update up to 1000 contacts per request. For batches larger than 100
        contacts, the system will process the updates asynchronously and return a job ID
        to track progress.

        For updating individual contacts, use the
        <a href="https://docs.apollo.io/reference/update-a-contact" target="_blank">Update
        a Contact endpoint</a> instead.

        Args:
          account_id: When using contact_ids, apply this account ID to all contacts

          async_: Force asynchronous processing. Automatically enabled for >100 contacts.

          contact_attributes: Array of contact objects with individual updates. Use this for applying
              different updates to each contact.

          contact_ids: Array of contact IDs to update with the same values. Use this for applying the
              same updates to multiple contacts.

          email: When using contact_ids, apply this email to all contacts

          first_name: When using contact_ids, apply this first name to all contacts

          last_name: When using contact_ids, apply this last name to all contacts

          linkedin_url: When using contact_ids, apply this LinkedIn URL to all contacts

          organization_name: When using contact_ids, apply this organization name to all contacts

          owner_id: When using contact_ids, apply this owner to all contacts

          present_raw_address: When using contact_ids, apply this address to all contacts

          title: When using contact_ids, apply this title to all contacts

          typed_custom_fields: When using contact_ids, apply these custom fields to all contacts

          visible_entity_ids: Specific contact IDs to return in the response (for performance)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body_data = {
            "account_id": account_id,
            "async_": async_,
            "contact_attributes": contact_attributes,
            "contact_ids": contact_ids,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "linkedin_url": linkedin_url,
            "organization_name": organization_name,
            "owner_id": owner_id,
            "present_raw_address": present_raw_address,
            "title": title,
            "typed_custom_fields": typed_custom_fields,
            "visible_entity_ids": visible_entity_ids,
        }
        if contact_attributes is omit and contact_ids is omit:
            body_data["contact_ids"] = ["string"]

        return cast(
            ContactBulkUpdateResponse,
            await self._post(
                "/contacts/bulk_update",
                body=await async_maybe_transform(
                    body_data,
                    contact_bulk_update_params.ContactBulkUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ContactBulkUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def search(
        self,
        *,
        contact_label_ids: SequenceNotStr[str] | Omit = omit,
        contact_stage_ids: SequenceNotStr[str] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        q_keywords: str | Omit = omit,
        sort_ascending: bool | Omit = omit,
        sort_by_field: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactSearchResponse:
        """
        Use the Search for Contacts endpoint to search for the contacts that have been
        added to your team's Apollo account.

        In Apollo terminology, a contact is a person that your team has explicitly added
        to your database. A contact will have their data enriched in some way, such as
        accessing an email address or a phone number.

        This endpoint only returns contacts in the search results. To search for people
        in the Apollo database, call the
        <a href="https://docs.apollo.io/reference/people-api-search" target="_blank">People
        API Search endpoint</a>.

        To protect Apollo's performance for all users, this endpoint has a display limit
        of 50,000 records (100 records per page, up to 500 pages). Add more filters to
        narrow your search results as much as possible. This limitation does not
        restrict your access to Apollo's database; you just need to access the data in
        batches.

        Args:
          contact_label_ids: The Apollo IDs for the labels that you want to include in your search results.
              If you add multiple labels, Apollo will include all contacts connected to any of
              the labels, along with the other parameters, in the search results. Example:
              `['6095a710bd01d100a506d4ae']`

          contact_stage_ids: The Apollo IDs for the contact stages that you want to include in your search
              results. If you add multiple contact stages, Apollo will include all contacts
              that match any of the stages, along with the other parameters, in the search
              results. Call the
              [List Contact Stages endpoint](https://docs.apollo.io/reference/list-contact-stages)
              to retrieve a list of all the contact stage IDs available in your Apollo
              account. Example: `6095a710bd01d100a506d4ae`

          page: The page number of the Apollo data that you want to retrieve. Use this parameter
              in combination with the `per_page` parameter to make search results navigable
              and improve the performance of the endpoint. Example: `4`

          per_page: The number of search results that should be returned for each page. Limiting the
              number of results per page improves the endpoint's performance. Use the `page`
              parameter to search the different pages of data. Example: `10`

          q_keywords: Add keywords to narrow the search of the contacts in your team's Apollo account.
              Keywords can include combinations of names, job titles, employers (company
              names), and email addresses. Examples: `tim zheng`; `senior research analyst`;
              `microsoft`

          sort_ascending: Set to `true` to sort the matching contacts in ascending order. This parameter
              must be used with `sort_by_field`. Otherwise, the sorting logic is not applied.
              Example: `true`

          sort_by_field:
              Sort the matching contacts by 1 of the following options:

              - `contact_last_activity_date`: The most recent activity date recorded first.
              - `contact_email_last_opened_at`: The most recent email opened date first.
              - `contact_email_last_clicked_at`: The most recent email clicked first.
              - `contact_created_at`: The most recently created first.
              - `contact_updated_at`: The most recently updated first.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contacts/search",
            body=await async_maybe_transform(
                {
                    "contact_label_ids": contact_label_ids,
                    "contact_stage_ids": contact_stage_ids,
                    "page": page,
                    "per_page": per_page,
                    "q_keywords": q_keywords,
                    "sort_ascending": sort_ascending,
                    "sort_by_field": sort_by_field,
                },
                contact_search_params.ContactSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactSearchResponse,
        )

    async def update_owners(
        self,
        *,
        contact_ids: SequenceNotStr[str],
        owner_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactUpdateOwnersResponse:
        """
        Use the Update Contact Owner for Multiple Contacts endpoint to assign multiple
        contacts to a different user in your team's Apollo account.

        To update more than the contact's owner, such as job titles or contact details,
        use the
        <a href="https://docs.apollo.io/reference/update-a-contact" target="_blank">Update
        a Contact endpoint</a> instead.

        Args:
          contact_ids: The Apollo IDs for the contacts that you want assign to an owner.

              To find contact IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
              for Contacts endpoint</a> and identify the `id` value for the contact.

              Example: `66e34b81740c50074e3d1bd4`

          owner_id: The ID for the contact owner within your team's Apollo account. This user will
              be assigned ownership of the contacts.

              Use the
              <a href="https://docs.apollo.io/reference/get-a-list-of-users" target="_blank">Get
              a List of Users endpoint</a> endpoint to retrieve IDs for all of the users
              within your Apollo account.

              Example: `66302798d03b9601c7934ebf`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contacts/update_owners",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query={**bracket_array_query_param("contact_ids", contact_ids), "owner_id": owner_id},
            ),
            cast_to=ContactUpdateOwnersResponse,
        )

    async def update_stages(
        self,
        *,
        contact_ids: SequenceNotStr[str],
        contact_stage_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactUpdateStagesResponse:
        """
        Use the Update Contact Stage for Multiple Contacts endpoint to update the
        contact stage for several contacts in your team's Apollo account.

        To update more than the contact stage, such as job titles or contact details,
        use the
        <a href="https://docs.apollo.io/reference/update-a-contact" target="_blank">Update
        a Contact endpoint</a> instead.

        Args:
          contact_ids: The Apollo IDs for the contacts that you want to update.

              To find contact IDs, call the
              <a href="https://docs.apollo.io/reference/search-for-contacts" target="_blank">Search
              for Contacts endpoint</a> and identify the `id` value for the contact.

              Example: `66e34b81740c50074e3d1bd4`

          contact_stage_id: The Apollo ID for the contact stage to which you want to assign the contacts.
              Call the
              <a href="https://docs.apollo.io/reference/list-contact-stages" target="_blank">List
              Contact Stages endpoint</a> to retrieve a list of all the contact stage IDs
              available in your Apollo account.

              Example: `6095a710bd01d100a506d4af`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contacts/update_stages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query={
                    **bracket_array_query_param("contact_ids", contact_ids),
                    "contact_stage_id": contact_stage_id,
                },
            ),
            cast_to=ContactUpdateStagesResponse,
        )


class ContactsResourceWithRawResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.create = to_raw_response_wrapper(
            contacts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            contacts.update,
        )
        self.bulk_create = to_raw_response_wrapper(
            contacts.bulk_create,
        )
        self.bulk_update = to_raw_response_wrapper(
            contacts.bulk_update,
        )
        self.search = to_raw_response_wrapper(
            contacts.search,
        )
        self.update_owners = to_raw_response_wrapper(
            contacts.update_owners,
        )
        self.update_stages = to_raw_response_wrapper(
            contacts.update_stages,
        )


class AsyncContactsResourceWithRawResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.create = async_to_raw_response_wrapper(
            contacts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            contacts.update,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            contacts.bulk_create,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            contacts.bulk_update,
        )
        self.search = async_to_raw_response_wrapper(
            contacts.search,
        )
        self.update_owners = async_to_raw_response_wrapper(
            contacts.update_owners,
        )
        self.update_stages = async_to_raw_response_wrapper(
            contacts.update_stages,
        )


class ContactsResourceWithStreamingResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.create = to_streamed_response_wrapper(
            contacts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            contacts.update,
        )
        self.bulk_create = to_streamed_response_wrapper(
            contacts.bulk_create,
        )
        self.bulk_update = to_streamed_response_wrapper(
            contacts.bulk_update,
        )
        self.search = to_streamed_response_wrapper(
            contacts.search,
        )
        self.update_owners = to_streamed_response_wrapper(
            contacts.update_owners,
        )
        self.update_stages = to_streamed_response_wrapper(
            contacts.update_stages,
        )


class AsyncContactsResourceWithStreamingResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.create = async_to_streamed_response_wrapper(
            contacts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            contacts.update,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            contacts.bulk_create,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            contacts.bulk_update,
        )
        self.search = async_to_streamed_response_wrapper(
            contacts.search,
        )
        self.update_owners = async_to_streamed_response_wrapper(
            contacts.update_owners,
        )
        self.update_stages = async_to_streamed_response_wrapper(
            contacts.update_stages,
        )
