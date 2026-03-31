# AccountStages

Types:

```python
from src.types import AccountStageListResponse
```

Methods:

- <code title="get /account_stages">client.account_stages.<a href="./src/resources/account_stages.py">list</a>() -> <a href="./src/types/account_stage_list_response.py">AccountStageListResponse</a></code>

# Accounts

Types:

```python
from src.types import (
    AccountCreateResponse,
    AccountUpdateResponse,
    AccountBulkCreateResponse,
    AccountBulkUpdateResponse,
    AccountSearchResponse,
    AccountUpdateOwnersResponse,
)
```

Methods:

- <code title="post /accounts">client.accounts.<a href="./src/resources/accounts.py">create</a>(\*\*<a href="src/types/account_create_params.py">params</a>) -> <a href="./src/types/account_create_response.py">AccountCreateResponse</a></code>
- <code title="patch /accounts/{account_id}">client.accounts.<a href="./src/resources/accounts.py">update</a>(account_id, \*\*<a href="src/types/account_update_params.py">params</a>) -> <a href="./src/types/account_update_response.py">AccountUpdateResponse</a></code>
- <code title="post /accounts/bulk_create">client.accounts.<a href="./src/resources/accounts.py">bulk_create</a>(\*\*<a href="src/types/account_bulk_create_params.py">params</a>) -> <a href="./src/types/account_bulk_create_response.py">AccountBulkCreateResponse</a></code>
- <code title="post /accounts/bulk_update">client.accounts.<a href="./src/resources/accounts.py">bulk_update</a>(\*\*<a href="src/types/account_bulk_update_params.py">params</a>) -> <a href="./src/types/account_bulk_update_response.py">AccountBulkUpdateResponse</a></code>
- <code title="post /accounts/search">client.accounts.<a href="./src/resources/accounts.py">search</a>(\*\*<a href="src/types/account_search_params.py">params</a>) -> <a href="./src/types/account_search_response.py">AccountSearchResponse</a></code>
- <code title="post /accounts/update_owners">client.accounts.<a href="./src/resources/accounts.py">update_owners</a>(\*\*<a href="src/types/account_update_owners_params.py">params</a>) -> <a href="./src/types/account_update_owners_response.py">AccountUpdateOwnersResponse</a></code>

# ContactStages

Methods:

- <code title="get /contact_stages">client.contact_stages.<a href="./src/resources/contact_stages.py">list</a>() -> None</code>

# Contacts

Types:

```python
from src.types import (
    ContactCreateResponse,
    ContactRetrieveResponse,
    ContactUpdateResponse,
    ContactBulkCreateResponse,
    ContactBulkUpdateResponse,
    ContactSearchResponse,
    ContactUpdateOwnersResponse,
    ContactUpdateStagesResponse,
)
```

Methods:

- <code title="post /contacts">client.contacts.<a href="./src/resources/contacts.py">create</a>(\*\*<a href="src/types/contact_create_params.py">params</a>) -> <a href="./src/types/contact_create_response.py">ContactCreateResponse</a></code>
- <code title="get /contacts/{contact_id}">client.contacts.<a href="./src/resources/contacts.py">retrieve</a>(contact_id) -> <a href="./src/types/contact_retrieve_response.py">ContactRetrieveResponse</a></code>
- <code title="patch /contacts/{contact_id}">client.contacts.<a href="./src/resources/contacts.py">update</a>(contact_id, \*\*<a href="src/types/contact_update_params.py">params</a>) -> <a href="./src/types/contact_update_response.py">ContactUpdateResponse</a></code>
- <code title="post /contacts/bulk_create">client.contacts.<a href="./src/resources/contacts.py">bulk_create</a>(\*\*<a href="src/types/contact_bulk_create_params.py">params</a>) -> <a href="./src/types/contact_bulk_create_response.py">ContactBulkCreateResponse</a></code>
- <code title="post /contacts/bulk_update">client.contacts.<a href="./src/resources/contacts.py">bulk_update</a>(\*\*<a href="src/types/contact_bulk_update_params.py">params</a>) -> <a href="./src/types/contact_bulk_update_response.py">ContactBulkUpdateResponse</a></code>
- <code title="post /contacts/search">client.contacts.<a href="./src/resources/contacts.py">search</a>(\*\*<a href="src/types/contact_search_params.py">params</a>) -> <a href="./src/types/contact_search_response.py">ContactSearchResponse</a></code>
- <code title="post /contacts/update_owners">client.contacts.<a href="./src/resources/contacts.py">update_owners</a>(\*\*<a href="src/types/contact_update_owners_params.py">params</a>) -> <a href="./src/types/contact_update_owners_response.py">ContactUpdateOwnersResponse</a></code>
- <code title="post /contacts/update_stages">client.contacts.<a href="./src/resources/contacts.py">update_stages</a>(\*\*<a href="src/types/contact_update_stages_params.py">params</a>) -> <a href="./src/types/contact_update_stages_response.py">ContactUpdateStagesResponse</a></code>

# EmailAccounts

Types:

```python
from src.types import EmailAccountListResponse
```

Methods:

- <code title="get /email_accounts">client.email_accounts.<a href="./src/resources/email_accounts.py">list</a>() -> <a href="./src/types/email_account_list_response.py">EmailAccountListResponse</a></code>

# EmailerCampaigns

Types:

```python
from src.types import (
    EmailerCampaignActivateResponse,
    EmailerCampaignAddContactsResponse,
    EmailerCampaignArchiveResponse,
    EmailerCampaignDeactivateResponse,
    EmailerCampaignSearchResponse,
    EmailerCampaignUpdateContactStatusResponse,
)
```

Methods:

- <code title="post /emailer_campaigns/{sequence_id}/approve">client.emailer_campaigns.<a href="./src/resources/emailer_campaigns.py">activate</a>(sequence_id) -> <a href="./src/types/emailer_campaign_activate_response.py">EmailerCampaignActivateResponse</a></code>
- <code title="post /emailer_campaigns/{sequence_id}/add_contact_ids">client.emailer_campaigns.<a href="./src/resources/emailer_campaigns.py">add_contacts</a>(sequence_id, \*\*<a href="src/types/emailer_campaign_add_contacts_params.py">params</a>) -> <a href="./src/types/emailer_campaign_add_contacts_response.py">EmailerCampaignAddContactsResponse</a></code>
- <code title="post /emailer_campaigns/{sequence_id}/archive">client.emailer_campaigns.<a href="./src/resources/emailer_campaigns.py">archive</a>(sequence_id) -> <a href="./src/types/emailer_campaign_archive_response.py">EmailerCampaignArchiveResponse</a></code>
- <code title="post /emailer_campaigns/{sequence_id}/abort">client.emailer_campaigns.<a href="./src/resources/emailer_campaigns.py">deactivate</a>(sequence_id) -> <a href="./src/types/emailer_campaign_deactivate_response.py">EmailerCampaignDeactivateResponse</a></code>
- <code title="post /emailer_campaigns/search">client.emailer_campaigns.<a href="./src/resources/emailer_campaigns.py">search</a>(\*\*<a href="src/types/emailer_campaign_search_params.py">params</a>) -> <a href="./src/types/emailer_campaign_search_response.py">EmailerCampaignSearchResponse</a></code>
- <code title="post /emailer_campaigns/remove_or_stop_contact_ids">client.emailer_campaigns.<a href="./src/resources/emailer_campaigns.py">update_contact_status</a>(\*\*<a href="src/types/emailer_campaign_update_contact_status_params.py">params</a>) -> <a href="./src/types/emailer_campaign_update_contact_status_response.py">EmailerCampaignUpdateContactStatusResponse</a></code>

# EmailerMessages

Methods:

- <code title="get /emailer_messages/{id}/activities">client.emailer_messages.<a href="./src/resources/emailer_messages.py">activities</a>(id) -> None</code>
- <code title="get /emailer_messages/search">client.emailer_messages.<a href="./src/resources/emailer_messages.py">search</a>(\*\*<a href="src/types/emailer_message_search_params.py">params</a>) -> None</code>

# Fields

Types:

```python
from src.types import FieldCreateResponse, FieldListResponse
```

Methods:

- <code title="post /fields">client.fields.<a href="./src/resources/fields.py">create</a>(\*\*<a href="src/types/field_create_params.py">params</a>) -> <a href="./src/types/field_create_response.py">FieldCreateResponse</a></code>
- <code title="get /fields">client.fields.<a href="./src/resources/fields.py">list</a>(\*\*<a href="src/types/field_list_params.py">params</a>) -> <a href="./src/types/field_list_response.py">FieldListResponse</a></code>

# Labels

Types:

```python
from src.types import LabelListResponse
```

Methods:

- <code title="get /labels">client.labels.<a href="./src/resources/labels.py">list</a>() -> <a href="./src/types/label_list_response.py">LabelListResponse</a></code>

# Notes

Types:

```python
from src.types import NoteListResponse
```

Methods:

- <code title="get /notes">client.notes.<a href="./src/resources/notes.py">list</a>(\*\*<a href="src/types/note_list_params.py">params</a>) -> <a href="./src/types/note_list_response.py">NoteListResponse</a></code>

# Opportunities

Types:

```python
from src.types import (
    OpportunityCreateResponse,
    OpportunityRetrieveResponse,
    OpportunityUpdateResponse,
    OpportunityListResponse,
)
```

Methods:

- <code title="post /opportunities">client.opportunities.<a href="./src/resources/opportunities.py">create</a>(\*\*<a href="src/types/opportunity_create_params.py">params</a>) -> <a href="./src/types/opportunity_create_response.py">OpportunityCreateResponse</a></code>
- <code title="get /opportunities/{opportunity_id}">client.opportunities.<a href="./src/resources/opportunities.py">retrieve</a>(opportunity_id) -> <a href="./src/types/opportunity_retrieve_response.py">OpportunityRetrieveResponse</a></code>
- <code title="patch /opportunities/{opportunity_id}">client.opportunities.<a href="./src/resources/opportunities.py">update</a>(opportunity_id, \*\*<a href="src/types/opportunity_update_params.py">params</a>) -> <a href="./src/types/opportunity_update_response.py">OpportunityUpdateResponse</a></code>
- <code title="get /opportunities/search">client.opportunities.<a href="./src/resources/opportunities.py">list</a>(\*\*<a href="src/types/opportunity_list_params.py">params</a>) -> <a href="./src/types/opportunity_list_response.py">OpportunityListResponse</a></code>

# OpportunityStages

Types:

```python
from src.types import OpportunityStageListResponse
```

Methods:

- <code title="get /opportunity_stages">client.opportunity_stages.<a href="./src/resources/opportunity_stages.py">list</a>() -> <a href="./src/types/opportunity_stage_list_response.py">OpportunityStageListResponse</a></code>

# Organizations

Types:

```python
from src.types import (
    OrganizationBulkEnrichResponse,
    OrganizationEnrichResponse,
    OrganizationJobPostingsResponse,
    OrganizationSearchResponse,
)
```

Methods:

- <code title="post /organizations/bulk_enrich">client.organizations.<a href="./src/resources/organizations.py">bulk_enrich</a>(\*\*<a href="src/types/organization_bulk_enrich_params.py">params</a>) -> <a href="./src/types/organization_bulk_enrich_response.py">OrganizationBulkEnrichResponse</a></code>
- <code title="get /organizations/enrich">client.organizations.<a href="./src/resources/organizations.py">enrich</a>(\*\*<a href="src/types/organization_enrich_params.py">params</a>) -> <a href="./src/types/organization_enrich_response.py">OrganizationEnrichResponse</a></code>
- <code title="get /organizations/{organization_id}/job_postings">client.organizations.<a href="./src/resources/organizations.py">job_postings</a>(organization_id, \*\*<a href="src/types/organization_job_postings_params.py">params</a>) -> <a href="./src/types/organization_job_postings_response.py">OrganizationJobPostingsResponse</a></code>
- <code title="post /mixed_companies/search">client.organizations.<a href="./src/resources/organizations.py">search</a>(\*\*<a href="src/types/organization_search_params.py">params</a>) -> <a href="./src/types/organization_search_response.py">OrganizationSearchResponse</a></code>

# People

Types:

```python
from src.types import PersonBulkEnrichmentResponse, PersonEnrichmentResponse, PersonSearchResponse
```

Methods:

- <code title="post /people/bulk_match">client.people.<a href="./src/resources/people.py">bulk_enrichment</a>(\*\*<a href="src/types/person_bulk_enrichment_params.py">params</a>) -> <a href="./src/types/person_bulk_enrichment_response.py">PersonBulkEnrichmentResponse</a></code>
- <code title="post /people/match">client.people.<a href="./src/resources/people.py">enrichment</a>(\*\*<a href="src/types/person_enrichment_params.py">params</a>) -> <a href="./src/types/person_enrichment_response.py">PersonEnrichmentResponse</a></code>
- <code title="post /mixed_people/api_search">client.people.<a href="./src/resources/people.py">search</a>(\*\*<a href="src/types/person_search_params.py">params</a>) -> <a href="./src/types/person_search_response.py">PersonSearchResponse</a></code>

# PhoneCalls

Methods:

- <code title="post /phone_calls">client.phone_calls.<a href="./src/resources/phone_calls.py">create</a>(\*\*<a href="src/types/phone_call_create_params.py">params</a>) -> None</code>
- <code title="put /phone_calls/{id}">client.phone_calls.<a href="./src/resources/phone_calls.py">update</a>(id, \*\*<a href="src/types/phone_call_update_params.py">params</a>) -> None</code>
- <code title="get /phone_calls/search">client.phone_calls.<a href="./src/resources/phone_calls.py">search</a>(\*\*<a href="src/types/phone_call_search_params.py">params</a>) -> None</code>

# Tasks

Types:

```python
from src.types import TaskCreateResponse, TaskBulkCreateResponse, TaskSearchResponse
```

Methods:

- <code title="post /tasks">client.tasks.<a href="./src/resources/tasks.py">create</a>(\*\*<a href="src/types/task_create_params.py">params</a>) -> <a href="./src/types/task_create_response.py">TaskCreateResponse</a></code>
- <code title="post /tasks/bulk_create">client.tasks.<a href="./src/resources/tasks.py">bulk_create</a>(\*\*<a href="src/types/task_bulk_create_params.py">params</a>) -> <a href="./src/types/task_bulk_create_response.py">TaskBulkCreateResponse</a></code>
- <code title="post /tasks/search">client.tasks.<a href="./src/resources/tasks.py">search</a>(\*\*<a href="src/types/task_search_params.py">params</a>) -> <a href="./src/types/task_search_response.py">TaskSearchResponse</a></code>

# TypedCustomFields

Types:

```python
from src.types import TypedCustomFieldListResponse
```

Methods:

- <code title="get /typed_custom_fields">client.typed_custom_fields.<a href="./src/resources/typed_custom_fields.py">list</a>() -> <a href="./src/types/typed_custom_field_list_response.py">TypedCustomFieldListResponse</a></code>

# UsageStats

Methods:

- <code title="post /usage_stats/api_usage_stats">client.usage_stats.<a href="./src/resources/usage_stats.py">api_usage_stats</a>() -> None</code>

# Users

Types:

```python
from src.types import UserSearchResponse
```

Methods:

- <code title="get /users/search">client.users.<a href="./src/resources/users.py">search</a>(\*\*<a href="src/types/user_search_params.py">params</a>) -> <a href="./src/types/user_search_response.py">UserSearchResponse</a></code>

# NewsArticles

Methods:

- <code title="post /news_articles/search">client.news_articles.<a href="./src/resources/news_articles.py">search</a>(\*\*<a href="src/types/news_article_search_params.py">params</a>) -> None</code>
