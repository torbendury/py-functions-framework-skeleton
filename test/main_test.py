import mock
from app import main
import pytest


@pytest.fixture
def mockrequest() -> mock.Mock:
    mock_req = mock.Mock()
    mock_req.args = {}
    return mock_req


def test_named_reques(mockrequest):
    mockrequest.args["name"] = "torbendury"
    resp = main.entrypoint(mockrequest)
    assert 200 in resp
    assert "Hello torbendury" in resp


def test_anon_request(mockrequest):
    resp = main.entrypoint(mockrequest)
    assert 200 in resp
    assert "Hello stranger" in resp
