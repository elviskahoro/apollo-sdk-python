# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import time
import atexit
import logging
import subprocess
from typing import TYPE_CHECKING, Iterator, AsyncIterator

import httpx
import pytest
from pytest_asyncio import is_async_test

from apollo import ApolloSDK, AsyncApolloSDK, DefaultAioHttpClient
from apollo._utils import is_dict

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest  # pyright: ignore[reportPrivateImportUsage]

pytest.register_assert_rewrite("tests.utils")

logging.getLogger("apollo").setLevel(logging.DEBUG)

try:
    import httpx_aiohttp  # noqa: F401

    HAS_HTTPX_AIOHTTP = True
except ImportError:
    HAS_HTTPX_AIOHTTP = False


# automatically add `pytest.mark.asyncio()` to all of our async tests
# so we don't have to add that boilerplate everywhere
def pytest_collection_modifyitems(items: list[pytest.Function]) -> None:
    pytest_asyncio_tests = (item for item in items if is_async_test(item))
    session_scope_marker = pytest.mark.asyncio(loop_scope="session")
    for async_test in pytest_asyncio_tests:
        async_test.add_marker(session_scope_marker, append=False)

    # API resource tests and aiohttp variants run by default.
    # If no mock/live server is available, `_ensure_mock_server()` below will
    # attempt to start Prism automatically.
    if not HAS_HTTPX_AIOHTTP:
        for item in items:
            if "async_client" not in item.fixturenames or not hasattr(item, "callspec"):
                continue
            async_client_param = item.callspec.params.get("async_client")
            if is_dict(async_client_param) and async_client_param.get("http_client") == "aiohttp":
                item.add_marker(pytest.mark.skip(reason="aiohttp transport adapter is not installed"))


base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

api_key = "My API Key"


def _is_server_reachable(url: str) -> bool:
    try:
        with httpx.Client(timeout=0.5) as client:
            client.get(url)
        return True
    except Exception:
        return False


_MOCK_PROCESS: subprocess.Popen[str] | None = None


def _ensure_mock_server() -> None:
    global _MOCK_PROCESS

    if _is_server_reachable(base_url):
        return

    repo_root = os.path.dirname(os.path.dirname(__file__))
    script_path = os.path.join(repo_root, "scripts", "mock")
    env = os.environ.copy()
    env.setdefault("TEST_API_BASE_URL", base_url)
    _MOCK_PROCESS = subprocess.Popen([script_path], cwd=repo_root, env=env)  # noqa: S603

    deadline = time.time() + 20
    while time.time() < deadline:
        if _is_server_reachable(base_url):
            break
        if _MOCK_PROCESS.poll() is not None and not _is_server_reachable(base_url):
            time.sleep(0.2)
            continue
        time.sleep(0.2)
    else:
        raise RuntimeError("Prism mock server did not become ready in time")

    def _cleanup() -> None:
        global _MOCK_PROCESS
        if _MOCK_PROCESS is not None and _MOCK_PROCESS.poll() is None:
            _MOCK_PROCESS.terminate()
            try:
                _MOCK_PROCESS.wait(timeout=5)
            except subprocess.TimeoutExpired:
                _MOCK_PROCESS.kill()
        _MOCK_PROCESS = None

    atexit.register(_cleanup)


@pytest.fixture(scope="session", autouse=True)
def _start_mock_server_for_api_resource_tests(request: FixtureRequest) -> Iterator[None]:
    selected = request.config.option.keyword or ""
    if "api_resources" in selected or selected == "":
        _ensure_mock_server()
    yield



@pytest.fixture(scope="session")
def client(request: FixtureRequest) -> Iterator[ApolloSDK]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    with ApolloSDK(base_url=base_url, api_key=api_key, _strict_response_validation=strict) as client:
        yield client


@pytest.fixture(scope="session")
async def async_client(request: FixtureRequest) -> AsyncIterator[AsyncApolloSDK]:
    param = getattr(request, "param", True)

    # defaults
    strict = True
    http_client: None | httpx.AsyncClient = None

    if isinstance(param, bool):
        strict = param
    elif is_dict(param):
        strict = param.get("strict", True)
        assert isinstance(strict, bool)

        http_client_type = param.get("http_client", "httpx")
        if http_client_type == "aiohttp":
            try:
                http_client = DefaultAioHttpClient()
            except RuntimeError:
                # If aiohttp transport isn't installed, fall back to default
                # httpx transport so the parametrized tests still execute.
                http_client = None
    else:
        raise TypeError(f"Unexpected fixture parameter type {type(param)}, expected bool or dict")

    async with AsyncApolloSDK(
        base_url=base_url, api_key=api_key, _strict_response_validation=strict, http_client=http_client
    ) as client:
        yield client
