import pytest

from utils.api_client import APIClient
from fixtures.user import user_data


@pytest.fixture()
def api():
    return APIClient()

@pytest.fixture(scope="session")
def database_connection():
    print("Setting up database connection")
    db_connection = "DatabaseConnectionObject"  
    yield db_connection  
    print("Tearing down database connection")