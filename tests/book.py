import pytest

from src.utils.api_client import APIClient
from src.utils import config, get


@pytest.fixture
def api():
    return APIClient()


def test_get_book_successfully():
    response =get(config["apiPath"]["books"]["getBook"])
    assert response.status_code == 200
    


    