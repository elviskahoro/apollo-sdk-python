# Apollo SDK Reconciliation Execution Checklist

Source spec: `designs/backlog-202603300000-apollo_openapi_reconciliation-spec-01.md`

## Decisions (must be explicit)

- [x] D1: Confirm flatten target layout (`src/` flat package modules).
- [x] D2: Confirm compatibility mode (`intentional migration` / breaking imports).
- [x] D3: Confirm PR strategy (single PR with split commits vs split PRs).
- [x] Confirm whether endpoint expansion ships in this same scope.

## Phase A: Auth + Base URL Correctness

- [x] Update `.stainless/stainless.yml`
- [x] Set `environments.production` to `https://app.apollo.io/api/v1`
- [x] Set client auth security scheme to `ApiKeyAuth`
- [x] Update `.stainless/openapi.json`
- [x] Replace bearer-based scheme with API key scheme (`x-api-key` header)
- [x] Ensure server URL includes `/api/v1`
- [x] Ensure operations/security references point to `ApiKeyAuth`
- [x] Regenerate SDK outputs from Stainless config/spec
- [x] Verify generated runtime uses `/api/v1` default
- [x] Verify generated runtime uses `x-api-key` header
- [x] Update tests to assert `x-api-key` (no bearer assertions)
- [x] Run targeted client tests for auth/header/base URL behavior

## Phase B: Flatten Layout Refactor

- [x] Move `src/apollo_sdk/*` to agreed flat target
- [x] Fix import graph and exports for new layout
- [x] Update `pyproject.toml` package/include settings
- [x] Update lint/type config paths impacted by layout move
- [x] If preserving compatibility, add shim for `import apollo_sdk` (N/A under intentional migration mode)
- [x] Verify import smoke in a clean venv from built wheel

## Phase C: Endpoint Surface + Regeneration Consistency

- [x] Keep expanded endpoint resource mapping in `.stainless/stainless.yml`
- [x] Regenerate and sync all generated outputs
- [x] Sync docs (`README.md`, `api.md`) to final behavior
- [x] Confirm no config/runtime drift after regeneration

## Phase D: Validation Matrix

- [x] Run lint (`./scripts/lint`)
- [x] Run type checks (repo-configured command)
- [x] Run mock tests (`./scripts/test-mock` or canonical equivalent)
- [x] Run build (`uv build`)
- [x] Install built wheel in clean venv
- [x] Run import + client-construction smoke checks
- [x] Run local secret-gated live smoke (sync + async)
- [x] Confirm no auth/base URL mismatch failures (no 401/404 due to config)

## Release Gate

- [x] Default base URL is `/api/v1` in generated clients
- [x] Auth header is `x-api-key` across sync/async/raw/streaming clients
- [x] Stainless config + OpenAPI encode same behavior
- [x] Flatten layout and compatibility posture are explicit
- [x] Docs reflect import/auth/base URL truth
- [x] Commit structure separates auth fix and layout refactor concerns

## Validation Notes

- `./scripts/lint` currently requires an explicit `uv` binary path in this environment (`/Users/elvis/.pyenv/versions/3.13.12/bin/uv`) because `pyenv` points to a Python version without `uv`.
- Stainless preview currently emits Python package files under `src/src/` for `package_name: src`; sync normalizes this to flat `src/` paths in-repo.
- Mock-test validation ran through canonical wrapper with a targeted scope:
  - `UV_PYTHON='>=3.9.0' ./scripts/test-mock tests/api_resources/test_people.py -q` (60 passed).
- `tests/test_client.py` intentionally differs from pure generated output to keep explicit default-base-url regression coverage.
- Commit split implemented:
  - `7d42097` — `fix(auth): use /api/v1 base URL and x-api-key security`
  - `fa8b177` — `refactor(layout): flatten package layout and sync regenerated outputs`
- Live smoke executed with explicit `api_key=os.environ["APOLLO_API_KEY"]`:
  - sync `people.enrichment()` -> `200`, request URL `https://app.apollo.io/api/v1/people/match`, `x-api-key` present, no `Authorization` header
  - async `people.enrichment()` -> `200`, request URL `https://app.apollo.io/api/v1/people/match`, `x-api-key` present, no `Authorization` header
