import pytest

from modules.app import ApplicationBootstrapper


def pytest_runtest_protocol(item, nextitem):
    pass


def pytest_sessionstart(session):
    pass


def pytest_sessionfinish(session, exitstatus):
    pass


@pytest.fixture(scope="session")
def test_session_id():
    session_id = os.environ.get("PYTEST_XDIST_SESSIONUUID")

    print("Session ID:", session_id)


@pytest.fixture(scope="module")
def app(request, testrun_uid):
    params = {
        "request": request,
        "testrun_uid": testrun_uid,
    }

    application = ApplicationBootstrapper().create_app(params)

    yield application

    application.close()
