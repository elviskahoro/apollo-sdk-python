# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ApolloSDKError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        notes,
        tasks,
        users,
        fields,
        labels,
        people,
        accounts,
        contacts,
        phone_calls,
        usage_stats,
        news_articles,
        opportunities,
        organizations,
        account_stages,
        contact_stages,
        email_accounts,
        emailer_messages,
        emailer_campaigns,
        opportunity_stages,
        typed_custom_fields,
    )
    from .resources.notes import NotesResource, AsyncNotesResource
    from .resources.tasks import TasksResource, AsyncTasksResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.fields import FieldsResource, AsyncFieldsResource
    from .resources.labels import LabelsResource, AsyncLabelsResource
    from .resources.people import PeopleResource, AsyncPeopleResource
    from .resources.accounts import AccountsResource, AsyncAccountsResource
    from .resources.contacts import ContactsResource, AsyncContactsResource
    from .resources.phone_calls import PhoneCallsResource, AsyncPhoneCallsResource
    from .resources.usage_stats import UsageStatsResource, AsyncUsageStatsResource
    from .resources.news_articles import NewsArticlesResource, AsyncNewsArticlesResource
    from .resources.opportunities import OpportunitiesResource, AsyncOpportunitiesResource
    from .resources.organizations import OrganizationsResource, AsyncOrganizationsResource
    from .resources.account_stages import AccountStagesResource, AsyncAccountStagesResource
    from .resources.contact_stages import ContactStagesResource, AsyncContactStagesResource
    from .resources.email_accounts import EmailAccountsResource, AsyncEmailAccountsResource
    from .resources.emailer_messages import EmailerMessagesResource, AsyncEmailerMessagesResource
    from .resources.emailer_campaigns import EmailerCampaignsResource, AsyncEmailerCampaignsResource
    from .resources.opportunity_stages import OpportunityStagesResource, AsyncOpportunityStagesResource
    from .resources.typed_custom_fields import TypedCustomFieldsResource, AsyncTypedCustomFieldsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "ApolloSDK",
    "AsyncApolloSDK",
    "Client",
    "AsyncClient",
]


class ApolloSDK(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous ApolloSDK client instance.

        This automatically infers the `api_key` argument from the `APOLLO_SDK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("APOLLO_SDK_API_KEY")
        if api_key is None:
            raise ApolloSDKError(
                "The api_key client option must be set either by passing api_key to the client or by setting the APOLLO_SDK_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("APOLLO_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://app.apollo.io"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def account_stages(self) -> AccountStagesResource:
        from .resources.account_stages import AccountStagesResource

        return AccountStagesResource(self)

    @cached_property
    def accounts(self) -> AccountsResource:
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def contact_stages(self) -> ContactStagesResource:
        from .resources.contact_stages import ContactStagesResource

        return ContactStagesResource(self)

    @cached_property
    def contacts(self) -> ContactsResource:
        from .resources.contacts import ContactsResource

        return ContactsResource(self)

    @cached_property
    def email_accounts(self) -> EmailAccountsResource:
        from .resources.email_accounts import EmailAccountsResource

        return EmailAccountsResource(self)

    @cached_property
    def emailer_campaigns(self) -> EmailerCampaignsResource:
        from .resources.emailer_campaigns import EmailerCampaignsResource

        return EmailerCampaignsResource(self)

    @cached_property
    def emailer_messages(self) -> EmailerMessagesResource:
        from .resources.emailer_messages import EmailerMessagesResource

        return EmailerMessagesResource(self)

    @cached_property
    def fields(self) -> FieldsResource:
        from .resources.fields import FieldsResource

        return FieldsResource(self)

    @cached_property
    def labels(self) -> LabelsResource:
        from .resources.labels import LabelsResource

        return LabelsResource(self)

    @cached_property
    def notes(self) -> NotesResource:
        from .resources.notes import NotesResource

        return NotesResource(self)

    @cached_property
    def opportunities(self) -> OpportunitiesResource:
        from .resources.opportunities import OpportunitiesResource

        return OpportunitiesResource(self)

    @cached_property
    def opportunity_stages(self) -> OpportunityStagesResource:
        from .resources.opportunity_stages import OpportunityStagesResource

        return OpportunityStagesResource(self)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        from .resources.organizations import OrganizationsResource

        return OrganizationsResource(self)

    @cached_property
    def people(self) -> PeopleResource:
        from .resources.people import PeopleResource

        return PeopleResource(self)

    @cached_property
    def phone_calls(self) -> PhoneCallsResource:
        from .resources.phone_calls import PhoneCallsResource

        return PhoneCallsResource(self)

    @cached_property
    def tasks(self) -> TasksResource:
        from .resources.tasks import TasksResource

        return TasksResource(self)

    @cached_property
    def typed_custom_fields(self) -> TypedCustomFieldsResource:
        from .resources.typed_custom_fields import TypedCustomFieldsResource

        return TypedCustomFieldsResource(self)

    @cached_property
    def usage_stats(self) -> UsageStatsResource:
        from .resources.usage_stats import UsageStatsResource

        return UsageStatsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def news_articles(self) -> NewsArticlesResource:
        from .resources.news_articles import NewsArticlesResource

        return NewsArticlesResource(self)

    @cached_property
    def with_raw_response(self) -> ApolloSDKWithRawResponse:
        return ApolloSDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApolloSDKWithStreamedResponse:
        return ApolloSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncApolloSDK(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncApolloSDK client instance.

        This automatically infers the `api_key` argument from the `APOLLO_SDK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("APOLLO_SDK_API_KEY")
        if api_key is None:
            raise ApolloSDKError(
                "The api_key client option must be set either by passing api_key to the client or by setting the APOLLO_SDK_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("APOLLO_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://app.apollo.io"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def account_stages(self) -> AsyncAccountStagesResource:
        from .resources.account_stages import AsyncAccountStagesResource

        return AsyncAccountStagesResource(self)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def contact_stages(self) -> AsyncContactStagesResource:
        from .resources.contact_stages import AsyncContactStagesResource

        return AsyncContactStagesResource(self)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        from .resources.contacts import AsyncContactsResource

        return AsyncContactsResource(self)

    @cached_property
    def email_accounts(self) -> AsyncEmailAccountsResource:
        from .resources.email_accounts import AsyncEmailAccountsResource

        return AsyncEmailAccountsResource(self)

    @cached_property
    def emailer_campaigns(self) -> AsyncEmailerCampaignsResource:
        from .resources.emailer_campaigns import AsyncEmailerCampaignsResource

        return AsyncEmailerCampaignsResource(self)

    @cached_property
    def emailer_messages(self) -> AsyncEmailerMessagesResource:
        from .resources.emailer_messages import AsyncEmailerMessagesResource

        return AsyncEmailerMessagesResource(self)

    @cached_property
    def fields(self) -> AsyncFieldsResource:
        from .resources.fields import AsyncFieldsResource

        return AsyncFieldsResource(self)

    @cached_property
    def labels(self) -> AsyncLabelsResource:
        from .resources.labels import AsyncLabelsResource

        return AsyncLabelsResource(self)

    @cached_property
    def notes(self) -> AsyncNotesResource:
        from .resources.notes import AsyncNotesResource

        return AsyncNotesResource(self)

    @cached_property
    def opportunities(self) -> AsyncOpportunitiesResource:
        from .resources.opportunities import AsyncOpportunitiesResource

        return AsyncOpportunitiesResource(self)

    @cached_property
    def opportunity_stages(self) -> AsyncOpportunityStagesResource:
        from .resources.opportunity_stages import AsyncOpportunityStagesResource

        return AsyncOpportunityStagesResource(self)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        from .resources.organizations import AsyncOrganizationsResource

        return AsyncOrganizationsResource(self)

    @cached_property
    def people(self) -> AsyncPeopleResource:
        from .resources.people import AsyncPeopleResource

        return AsyncPeopleResource(self)

    @cached_property
    def phone_calls(self) -> AsyncPhoneCallsResource:
        from .resources.phone_calls import AsyncPhoneCallsResource

        return AsyncPhoneCallsResource(self)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        from .resources.tasks import AsyncTasksResource

        return AsyncTasksResource(self)

    @cached_property
    def typed_custom_fields(self) -> AsyncTypedCustomFieldsResource:
        from .resources.typed_custom_fields import AsyncTypedCustomFieldsResource

        return AsyncTypedCustomFieldsResource(self)

    @cached_property
    def usage_stats(self) -> AsyncUsageStatsResource:
        from .resources.usage_stats import AsyncUsageStatsResource

        return AsyncUsageStatsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def news_articles(self) -> AsyncNewsArticlesResource:
        from .resources.news_articles import AsyncNewsArticlesResource

        return AsyncNewsArticlesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncApolloSDKWithRawResponse:
        return AsyncApolloSDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApolloSDKWithStreamedResponse:
        return AsyncApolloSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ApolloSDKWithRawResponse:
    _client: ApolloSDK

    def __init__(self, client: ApolloSDK) -> None:
        self._client = client

    @cached_property
    def account_stages(self) -> account_stages.AccountStagesResourceWithRawResponse:
        from .resources.account_stages import AccountStagesResourceWithRawResponse

        return AccountStagesResourceWithRawResponse(self._client.account_stages)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def contact_stages(self) -> contact_stages.ContactStagesResourceWithRawResponse:
        from .resources.contact_stages import ContactStagesResourceWithRawResponse

        return ContactStagesResourceWithRawResponse(self._client.contact_stages)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithRawResponse:
        from .resources.contacts import ContactsResourceWithRawResponse

        return ContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def email_accounts(self) -> email_accounts.EmailAccountsResourceWithRawResponse:
        from .resources.email_accounts import EmailAccountsResourceWithRawResponse

        return EmailAccountsResourceWithRawResponse(self._client.email_accounts)

    @cached_property
    def emailer_campaigns(self) -> emailer_campaigns.EmailerCampaignsResourceWithRawResponse:
        from .resources.emailer_campaigns import EmailerCampaignsResourceWithRawResponse

        return EmailerCampaignsResourceWithRawResponse(self._client.emailer_campaigns)

    @cached_property
    def emailer_messages(self) -> emailer_messages.EmailerMessagesResourceWithRawResponse:
        from .resources.emailer_messages import EmailerMessagesResourceWithRawResponse

        return EmailerMessagesResourceWithRawResponse(self._client.emailer_messages)

    @cached_property
    def fields(self) -> fields.FieldsResourceWithRawResponse:
        from .resources.fields import FieldsResourceWithRawResponse

        return FieldsResourceWithRawResponse(self._client.fields)

    @cached_property
    def labels(self) -> labels.LabelsResourceWithRawResponse:
        from .resources.labels import LabelsResourceWithRawResponse

        return LabelsResourceWithRawResponse(self._client.labels)

    @cached_property
    def notes(self) -> notes.NotesResourceWithRawResponse:
        from .resources.notes import NotesResourceWithRawResponse

        return NotesResourceWithRawResponse(self._client.notes)

    @cached_property
    def opportunities(self) -> opportunities.OpportunitiesResourceWithRawResponse:
        from .resources.opportunities import OpportunitiesResourceWithRawResponse

        return OpportunitiesResourceWithRawResponse(self._client.opportunities)

    @cached_property
    def opportunity_stages(self) -> opportunity_stages.OpportunityStagesResourceWithRawResponse:
        from .resources.opportunity_stages import OpportunityStagesResourceWithRawResponse

        return OpportunityStagesResourceWithRawResponse(self._client.opportunity_stages)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithRawResponse:
        from .resources.organizations import OrganizationsResourceWithRawResponse

        return OrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def people(self) -> people.PeopleResourceWithRawResponse:
        from .resources.people import PeopleResourceWithRawResponse

        return PeopleResourceWithRawResponse(self._client.people)

    @cached_property
    def phone_calls(self) -> phone_calls.PhoneCallsResourceWithRawResponse:
        from .resources.phone_calls import PhoneCallsResourceWithRawResponse

        return PhoneCallsResourceWithRawResponse(self._client.phone_calls)

    @cached_property
    def tasks(self) -> tasks.TasksResourceWithRawResponse:
        from .resources.tasks import TasksResourceWithRawResponse

        return TasksResourceWithRawResponse(self._client.tasks)

    @cached_property
    def typed_custom_fields(self) -> typed_custom_fields.TypedCustomFieldsResourceWithRawResponse:
        from .resources.typed_custom_fields import TypedCustomFieldsResourceWithRawResponse

        return TypedCustomFieldsResourceWithRawResponse(self._client.typed_custom_fields)

    @cached_property
    def usage_stats(self) -> usage_stats.UsageStatsResourceWithRawResponse:
        from .resources.usage_stats import UsageStatsResourceWithRawResponse

        return UsageStatsResourceWithRawResponse(self._client.usage_stats)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def news_articles(self) -> news_articles.NewsArticlesResourceWithRawResponse:
        from .resources.news_articles import NewsArticlesResourceWithRawResponse

        return NewsArticlesResourceWithRawResponse(self._client.news_articles)


class AsyncApolloSDKWithRawResponse:
    _client: AsyncApolloSDK

    def __init__(self, client: AsyncApolloSDK) -> None:
        self._client = client

    @cached_property
    def account_stages(self) -> account_stages.AsyncAccountStagesResourceWithRawResponse:
        from .resources.account_stages import AsyncAccountStagesResourceWithRawResponse

        return AsyncAccountStagesResourceWithRawResponse(self._client.account_stages)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def contact_stages(self) -> contact_stages.AsyncContactStagesResourceWithRawResponse:
        from .resources.contact_stages import AsyncContactStagesResourceWithRawResponse

        return AsyncContactStagesResourceWithRawResponse(self._client.contact_stages)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithRawResponse:
        from .resources.contacts import AsyncContactsResourceWithRawResponse

        return AsyncContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def email_accounts(self) -> email_accounts.AsyncEmailAccountsResourceWithRawResponse:
        from .resources.email_accounts import AsyncEmailAccountsResourceWithRawResponse

        return AsyncEmailAccountsResourceWithRawResponse(self._client.email_accounts)

    @cached_property
    def emailer_campaigns(self) -> emailer_campaigns.AsyncEmailerCampaignsResourceWithRawResponse:
        from .resources.emailer_campaigns import AsyncEmailerCampaignsResourceWithRawResponse

        return AsyncEmailerCampaignsResourceWithRawResponse(self._client.emailer_campaigns)

    @cached_property
    def emailer_messages(self) -> emailer_messages.AsyncEmailerMessagesResourceWithRawResponse:
        from .resources.emailer_messages import AsyncEmailerMessagesResourceWithRawResponse

        return AsyncEmailerMessagesResourceWithRawResponse(self._client.emailer_messages)

    @cached_property
    def fields(self) -> fields.AsyncFieldsResourceWithRawResponse:
        from .resources.fields import AsyncFieldsResourceWithRawResponse

        return AsyncFieldsResourceWithRawResponse(self._client.fields)

    @cached_property
    def labels(self) -> labels.AsyncLabelsResourceWithRawResponse:
        from .resources.labels import AsyncLabelsResourceWithRawResponse

        return AsyncLabelsResourceWithRawResponse(self._client.labels)

    @cached_property
    def notes(self) -> notes.AsyncNotesResourceWithRawResponse:
        from .resources.notes import AsyncNotesResourceWithRawResponse

        return AsyncNotesResourceWithRawResponse(self._client.notes)

    @cached_property
    def opportunities(self) -> opportunities.AsyncOpportunitiesResourceWithRawResponse:
        from .resources.opportunities import AsyncOpportunitiesResourceWithRawResponse

        return AsyncOpportunitiesResourceWithRawResponse(self._client.opportunities)

    @cached_property
    def opportunity_stages(self) -> opportunity_stages.AsyncOpportunityStagesResourceWithRawResponse:
        from .resources.opportunity_stages import AsyncOpportunityStagesResourceWithRawResponse

        return AsyncOpportunityStagesResourceWithRawResponse(self._client.opportunity_stages)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithRawResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithRawResponse

        return AsyncOrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def people(self) -> people.AsyncPeopleResourceWithRawResponse:
        from .resources.people import AsyncPeopleResourceWithRawResponse

        return AsyncPeopleResourceWithRawResponse(self._client.people)

    @cached_property
    def phone_calls(self) -> phone_calls.AsyncPhoneCallsResourceWithRawResponse:
        from .resources.phone_calls import AsyncPhoneCallsResourceWithRawResponse

        return AsyncPhoneCallsResourceWithRawResponse(self._client.phone_calls)

    @cached_property
    def tasks(self) -> tasks.AsyncTasksResourceWithRawResponse:
        from .resources.tasks import AsyncTasksResourceWithRawResponse

        return AsyncTasksResourceWithRawResponse(self._client.tasks)

    @cached_property
    def typed_custom_fields(self) -> typed_custom_fields.AsyncTypedCustomFieldsResourceWithRawResponse:
        from .resources.typed_custom_fields import AsyncTypedCustomFieldsResourceWithRawResponse

        return AsyncTypedCustomFieldsResourceWithRawResponse(self._client.typed_custom_fields)

    @cached_property
    def usage_stats(self) -> usage_stats.AsyncUsageStatsResourceWithRawResponse:
        from .resources.usage_stats import AsyncUsageStatsResourceWithRawResponse

        return AsyncUsageStatsResourceWithRawResponse(self._client.usage_stats)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def news_articles(self) -> news_articles.AsyncNewsArticlesResourceWithRawResponse:
        from .resources.news_articles import AsyncNewsArticlesResourceWithRawResponse

        return AsyncNewsArticlesResourceWithRawResponse(self._client.news_articles)


class ApolloSDKWithStreamedResponse:
    _client: ApolloSDK

    def __init__(self, client: ApolloSDK) -> None:
        self._client = client

    @cached_property
    def account_stages(self) -> account_stages.AccountStagesResourceWithStreamingResponse:
        from .resources.account_stages import AccountStagesResourceWithStreamingResponse

        return AccountStagesResourceWithStreamingResponse(self._client.account_stages)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def contact_stages(self) -> contact_stages.ContactStagesResourceWithStreamingResponse:
        from .resources.contact_stages import ContactStagesResourceWithStreamingResponse

        return ContactStagesResourceWithStreamingResponse(self._client.contact_stages)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithStreamingResponse:
        from .resources.contacts import ContactsResourceWithStreamingResponse

        return ContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def email_accounts(self) -> email_accounts.EmailAccountsResourceWithStreamingResponse:
        from .resources.email_accounts import EmailAccountsResourceWithStreamingResponse

        return EmailAccountsResourceWithStreamingResponse(self._client.email_accounts)

    @cached_property
    def emailer_campaigns(self) -> emailer_campaigns.EmailerCampaignsResourceWithStreamingResponse:
        from .resources.emailer_campaigns import EmailerCampaignsResourceWithStreamingResponse

        return EmailerCampaignsResourceWithStreamingResponse(self._client.emailer_campaigns)

    @cached_property
    def emailer_messages(self) -> emailer_messages.EmailerMessagesResourceWithStreamingResponse:
        from .resources.emailer_messages import EmailerMessagesResourceWithStreamingResponse

        return EmailerMessagesResourceWithStreamingResponse(self._client.emailer_messages)

    @cached_property
    def fields(self) -> fields.FieldsResourceWithStreamingResponse:
        from .resources.fields import FieldsResourceWithStreamingResponse

        return FieldsResourceWithStreamingResponse(self._client.fields)

    @cached_property
    def labels(self) -> labels.LabelsResourceWithStreamingResponse:
        from .resources.labels import LabelsResourceWithStreamingResponse

        return LabelsResourceWithStreamingResponse(self._client.labels)

    @cached_property
    def notes(self) -> notes.NotesResourceWithStreamingResponse:
        from .resources.notes import NotesResourceWithStreamingResponse

        return NotesResourceWithStreamingResponse(self._client.notes)

    @cached_property
    def opportunities(self) -> opportunities.OpportunitiesResourceWithStreamingResponse:
        from .resources.opportunities import OpportunitiesResourceWithStreamingResponse

        return OpportunitiesResourceWithStreamingResponse(self._client.opportunities)

    @cached_property
    def opportunity_stages(self) -> opportunity_stages.OpportunityStagesResourceWithStreamingResponse:
        from .resources.opportunity_stages import OpportunityStagesResourceWithStreamingResponse

        return OpportunityStagesResourceWithStreamingResponse(self._client.opportunity_stages)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithStreamingResponse:
        from .resources.organizations import OrganizationsResourceWithStreamingResponse

        return OrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def people(self) -> people.PeopleResourceWithStreamingResponse:
        from .resources.people import PeopleResourceWithStreamingResponse

        return PeopleResourceWithStreamingResponse(self._client.people)

    @cached_property
    def phone_calls(self) -> phone_calls.PhoneCallsResourceWithStreamingResponse:
        from .resources.phone_calls import PhoneCallsResourceWithStreamingResponse

        return PhoneCallsResourceWithStreamingResponse(self._client.phone_calls)

    @cached_property
    def tasks(self) -> tasks.TasksResourceWithStreamingResponse:
        from .resources.tasks import TasksResourceWithStreamingResponse

        return TasksResourceWithStreamingResponse(self._client.tasks)

    @cached_property
    def typed_custom_fields(self) -> typed_custom_fields.TypedCustomFieldsResourceWithStreamingResponse:
        from .resources.typed_custom_fields import TypedCustomFieldsResourceWithStreamingResponse

        return TypedCustomFieldsResourceWithStreamingResponse(self._client.typed_custom_fields)

    @cached_property
    def usage_stats(self) -> usage_stats.UsageStatsResourceWithStreamingResponse:
        from .resources.usage_stats import UsageStatsResourceWithStreamingResponse

        return UsageStatsResourceWithStreamingResponse(self._client.usage_stats)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def news_articles(self) -> news_articles.NewsArticlesResourceWithStreamingResponse:
        from .resources.news_articles import NewsArticlesResourceWithStreamingResponse

        return NewsArticlesResourceWithStreamingResponse(self._client.news_articles)


class AsyncApolloSDKWithStreamedResponse:
    _client: AsyncApolloSDK

    def __init__(self, client: AsyncApolloSDK) -> None:
        self._client = client

    @cached_property
    def account_stages(self) -> account_stages.AsyncAccountStagesResourceWithStreamingResponse:
        from .resources.account_stages import AsyncAccountStagesResourceWithStreamingResponse

        return AsyncAccountStagesResourceWithStreamingResponse(self._client.account_stages)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def contact_stages(self) -> contact_stages.AsyncContactStagesResourceWithStreamingResponse:
        from .resources.contact_stages import AsyncContactStagesResourceWithStreamingResponse

        return AsyncContactStagesResourceWithStreamingResponse(self._client.contact_stages)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithStreamingResponse:
        from .resources.contacts import AsyncContactsResourceWithStreamingResponse

        return AsyncContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def email_accounts(self) -> email_accounts.AsyncEmailAccountsResourceWithStreamingResponse:
        from .resources.email_accounts import AsyncEmailAccountsResourceWithStreamingResponse

        return AsyncEmailAccountsResourceWithStreamingResponse(self._client.email_accounts)

    @cached_property
    def emailer_campaigns(self) -> emailer_campaigns.AsyncEmailerCampaignsResourceWithStreamingResponse:
        from .resources.emailer_campaigns import AsyncEmailerCampaignsResourceWithStreamingResponse

        return AsyncEmailerCampaignsResourceWithStreamingResponse(self._client.emailer_campaigns)

    @cached_property
    def emailer_messages(self) -> emailer_messages.AsyncEmailerMessagesResourceWithStreamingResponse:
        from .resources.emailer_messages import AsyncEmailerMessagesResourceWithStreamingResponse

        return AsyncEmailerMessagesResourceWithStreamingResponse(self._client.emailer_messages)

    @cached_property
    def fields(self) -> fields.AsyncFieldsResourceWithStreamingResponse:
        from .resources.fields import AsyncFieldsResourceWithStreamingResponse

        return AsyncFieldsResourceWithStreamingResponse(self._client.fields)

    @cached_property
    def labels(self) -> labels.AsyncLabelsResourceWithStreamingResponse:
        from .resources.labels import AsyncLabelsResourceWithStreamingResponse

        return AsyncLabelsResourceWithStreamingResponse(self._client.labels)

    @cached_property
    def notes(self) -> notes.AsyncNotesResourceWithStreamingResponse:
        from .resources.notes import AsyncNotesResourceWithStreamingResponse

        return AsyncNotesResourceWithStreamingResponse(self._client.notes)

    @cached_property
    def opportunities(self) -> opportunities.AsyncOpportunitiesResourceWithStreamingResponse:
        from .resources.opportunities import AsyncOpportunitiesResourceWithStreamingResponse

        return AsyncOpportunitiesResourceWithStreamingResponse(self._client.opportunities)

    @cached_property
    def opportunity_stages(self) -> opportunity_stages.AsyncOpportunityStagesResourceWithStreamingResponse:
        from .resources.opportunity_stages import AsyncOpportunityStagesResourceWithStreamingResponse

        return AsyncOpportunityStagesResourceWithStreamingResponse(self._client.opportunity_stages)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithStreamingResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithStreamingResponse

        return AsyncOrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def people(self) -> people.AsyncPeopleResourceWithStreamingResponse:
        from .resources.people import AsyncPeopleResourceWithStreamingResponse

        return AsyncPeopleResourceWithStreamingResponse(self._client.people)

    @cached_property
    def phone_calls(self) -> phone_calls.AsyncPhoneCallsResourceWithStreamingResponse:
        from .resources.phone_calls import AsyncPhoneCallsResourceWithStreamingResponse

        return AsyncPhoneCallsResourceWithStreamingResponse(self._client.phone_calls)

    @cached_property
    def tasks(self) -> tasks.AsyncTasksResourceWithStreamingResponse:
        from .resources.tasks import AsyncTasksResourceWithStreamingResponse

        return AsyncTasksResourceWithStreamingResponse(self._client.tasks)

    @cached_property
    def typed_custom_fields(self) -> typed_custom_fields.AsyncTypedCustomFieldsResourceWithStreamingResponse:
        from .resources.typed_custom_fields import AsyncTypedCustomFieldsResourceWithStreamingResponse

        return AsyncTypedCustomFieldsResourceWithStreamingResponse(self._client.typed_custom_fields)

    @cached_property
    def usage_stats(self) -> usage_stats.AsyncUsageStatsResourceWithStreamingResponse:
        from .resources.usage_stats import AsyncUsageStatsResourceWithStreamingResponse

        return AsyncUsageStatsResourceWithStreamingResponse(self._client.usage_stats)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def news_articles(self) -> news_articles.AsyncNewsArticlesResourceWithStreamingResponse:
        from .resources.news_articles import AsyncNewsArticlesResourceWithStreamingResponse

        return AsyncNewsArticlesResourceWithStreamingResponse(self._client.news_articles)


Client = ApolloSDK

AsyncClient = AsyncApolloSDK
