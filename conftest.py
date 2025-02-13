import pytest
import json
import os
import logging

from utils.api_client import APIClient
from fixtures.user import user_data

@pytest.fixture()
def api():
    return APIClient()

@pytest.fixture(scope="session")
def database_connection(logger):
    logger.info("Setting up database connection")
    db_connection = "DatabaseConnectionObject"  
    yield db_connection  
    logger.info("Tearing down database connection")

@pytest.fixture(scope="session")
def config(pytestconfig):
    return pytestconfig.env

@pytest.fixture(scope='session')
def logger():
    logger = logging.getLogger(__name__)
    return logger

def pytest_configure(config):
    # Initialize logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='test.log',  
                        filemode='w')
    logger = logging.getLogger(__name__)

    # Load environment
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(dir_path, "configs", "production.json")

    try:
        with open(config_path, "r") as f:
            configuration = json.load(f)
            # Setting a custom configuration object attribute
            config.env = configuration
            logger.info("Configuration loaded successfully")
    except Exception as e:
        logger.error("Failed to load configuration:", exc_info=True)

    logger.info("Logging is configured, and configuration is loaded.")

# Pytest hooks
def pytest_sessionstart():
    logger = logging.getLogger(__name__)
    logger.info("Test session is starting")

def pytest_sessionfinish(exitstatus):
    logger = logging.getLogger(__name__)
    logger.info("Test session is finishing with exit status:", exitstatus)

def pytest_runtest_setup(item):
    logger = logging.getLogger(__name__)
    logger.info(f"Setting up for test: {item.name}")

def pytest_runtest_teardown(item):
    logger = logging.getLogger(__name__)
    logger.info(f"Tearing down after test: {item.name}")


