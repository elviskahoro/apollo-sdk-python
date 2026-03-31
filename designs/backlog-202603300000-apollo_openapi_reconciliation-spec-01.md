# Apollo SDK Consolidated Refactor + Auth Fix Spec

## 1. Purpose

Create one implementation spec that combines all remaining work:

1. Package-layout refactor (flatten generated code from `src/apollo_sdk/` to `src/` or equivalent agreed flat layout).
2. Endpoint-surface expansion (already started in current branch; formalize and validate).
3. Live API correctness fixes from investigation:
   - Default base URL must include `/api/v1`
   - Auth must use `x-api-key` header, not `Authorization: Bearer`
4. Stainless/OpenAPI alignment so regeneration preserves behavior.
5. End-to-end validation and release readiness.

---

## 2. Current State Summary

- Current repo: `/Users/elvis/Documents/elviskahoro/apollo-sdk-python`
- Branch: `main`
- Current changes include broad endpoint expansion from `people`-only to many resources.
- Requested flattening refactor is still not done.
- Another agent validated live fixes in a separate repo clone (`apollo-sdk-python-fix-auth`) and confirmed:
  - `https://app.apollo.io/api/v1` works
  - `x-api-key` works
  - bearer auth fails

---

## 3. Scope

## In scope

1. **Runtime auth/base URL correctness**
   - Update sync + async clients to default base URL `https://app.apollo.io/api/v1`.
   - Emit `x-api-key: <key>` auth header.
2. **Generation-source alignment**
   - `.stainless/stainless.yml`:
     - `environments.production: https://app.apollo.io/api/v1`
     - client auth scheme set to `ApiKeyAuth`
   - `.stainless/openapi.json`:
     - define `ApiKeyAuth` (`type: apiKey`, `in: header`, `name: x-api-key`)
     - ensure operations reference `ApiKeyAuth`.
3. **Flatten layout refactor**
   - Move package code to flat `src/` layout (exact target confirmed below in Decision D1).
   - Update build config, test config, imports, docs paths.
4. **Endpoint coverage consistency**
   - Keep expanded resource/method mapping in Stainless config.
   - Regenerate SDK and sync generated outputs.
5. **Validation and release readiness**
   - Unit/generated tests, lint/type/build, install/import smoke, minimal live checks.

## Out of scope

- New endpoint design beyond already present OpenAPI surface.
- Non-Python SDK targets.
- Feature-level changes to API semantics beyond auth/base URL fix.

---

## 4. Architecture Decisions

- **D1 (required): flat layout target**
  - Preferred: true flat package at `src/` with module names unchanged where possible.
  - Compatibility shim strategy required if `import apollo_sdk` must remain stable.
- **D2: compatibility mode**
  - `strict no-breaking`: preserve `apollo_sdk` import path via shim package.
  - `intentional migration`: publish breaking change with explicit migration guide.
- **D3: scope split**
  - Recommended: one PR with two commits:
    1. `fix(auth): api/v1 + x-api-key + Stainless security alignment`
    2. `refactor(layout): flatten src layout + regen + docs/tests`

---

## 5. Detailed Implementation Plan

## Phase A — Integrate live-call fixes first

### A1. Runtime client fixes
- Files:
  - `src/apollo_sdk/_client.py` (or flattened equivalent after Phase B)
- Changes:
  - default base URL -> `https://app.apollo.io/api/v1`
  - auth header map -> `{"x-api-key": api_key}`
- Acceptance:
  - No `Authorization: Bearer` in outbound auth headers.
  - All sync/async/raw/streaming clients inherit same base URL/auth behavior.

### A2. Test assertion updates
- Files:
  - `tests/test_client.py`
- Changes:
  - header assertions from `Authorization` to `x-api-key`.
- Acceptance:
  - Header tests pass for sync + async variants.

### A3. Stainless/OpenAPI anti-regression
- Files:
  - `.stainless/stainless.yml`
  - `.stainless/openapi.json`
- Changes:
  - production env base URL includes `/api/v1`
  - security scheme uses `ApiKeyAuth`
- Acceptance:
  - Regeneration does not revert auth/base URL behavior.

---

## Phase B — Flatten package layout

### B1. Move/reshape package files
- Move from `src/apollo_sdk/*` to flat target (decision D1).
- Update intra-package imports accordingly.

### B2. Packaging config updates
- Files:
  - `pyproject.toml`
- Update:
  - `[tool.hatch.build.targets.wheel].packages`
  - mypy exclusions and any hardcoded `src/apollo_sdk/*` paths
- Acceptance:
  - `uv build` creates valid wheel/sdist with expected module layout.

### B3. Backward compatibility (if strict mode)
- Add shim package or import redirects so existing consumers still use:
  - `from apollo_sdk import ApolloSDK`
- Acceptance:
  - existing import examples continue to run without code changes.

---

## Phase C — Endpoint surface + regeneration consistency

### C1. Keep expanded resource mapping
- File:
  - `.stainless/stainless.yml`
- Ensure resource map includes current expanded endpoints.

### C2. Regenerate and sync outputs
- Run Stainless generation.
- Sync generated `src`, `tests/api_resources`, `api.md`, `README.md`.
- Acceptance:
  - generated client exposes expanded resources.
  - no manual drift between source config and generated code.

---

## Phase D — Validation matrix

## D1. Static/quality checks
- `./scripts/lint`
- typecheck command used by repo (`pyright`/`mypy` as configured)

## D2. Tests
- mock-server suite:
  - `./scripts/test-mock` (or start Prism and run `./scripts/test`)
- targeted client tests:
  - header + auth/base URL behavior
- report exact pass/fail/skip counts

## D3. Build/install/import
- `uv build`
- install wheel in clean venv
- smoke imports + one client construction test

## D4. Live smoke (non-CI, local secret-gated)
- Minimal live call(s) against people enrichment:
  - sync + async
  - raw/streaming parse path
- Acceptance:
  - HTTP 200 for known-valid request shape (or expected non-auth response, but not 401/404 due to auth/base URL).

---

## 6. File-Level Expected Changes

- **Config/Generation**
  - `.stainless/stainless.yml`
  - `.stainless/openapi.json`
- **Runtime**
  - `_client.py` (path depends on flatten outcome)
  - possibly auth-related helpers if generated structure demands
- **Packaging**
  - `pyproject.toml`
- **Tests**
  - `tests/test_client.py`
  - generated `tests/api_resources/*` as needed
- **Docs**
  - `README.md`
  - `api.md`
  - optional migration doc `docs/migration/flatten-layout.md`

---

## 7. Risks and Mitigations

1. **Regen overwrites manual runtime fixes**
- Mitigation: encode in Stainless/OpenAPI source-of-truth first.

2. **Flattening breaks imports for existing users**
- Mitigation: compatibility shim + deprecation window (strict mode).

3. **Large generated diff obscures regressions**
- Mitigation: split commits by concern (auth fix vs layout vs regen).

4. **Mock test failures due infra (Prism not running)**
- Mitigation: make `test-mock` canonical verification step in checklist.

---

## 8. Acceptance Criteria (Release Gate)

All must be true:

1. Default base URL is `/api/v1` in generated clients.
2. Auth header is `x-api-key` everywhere.
3. Stainless config/OpenAPI reflect ApiKeyAuth and `/api/v1`.
4. Flattened layout is complete and build config matches it.
5. Backward compatibility status is explicit (preserved or intentional break with migration doc).
6. Lint/type/build pass.
7. Mock test suite passes with server running.
8. Live smoke confirms no 401/404 due to auth/base URL mismatch.
9. README/api docs match final import/layout/auth behavior.

---

## 9. Execution Order (Recommended)

1. Apply Phase A in current repo.
2. Confirm tests for auth header changes.
3. Apply Phase B flatten refactor.
4. Apply Phase C regen/sync.
5. Run Phase D validation.
6. Prepare release notes + migration notes.
7. Open PR with commit-structured review.

---

## 10. Open Questions (Need explicit decision before coding)

1. Should we preserve `import apollo_sdk` compatibility during flattening?
2. Is flatten target truly `src/` modules, or a different “flat” package structure?
3. Do you want one PR or split PRs (auth fix first, flatten second)?
4. Should endpoint expansion stay in this scope, or ship separately from flattening?

If you want, I can now turn this spec into an executable checklist file in-repo (e.g. `docs/specs/flatten-auth-refactor.md`) and then implement it step-by-step.
