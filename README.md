
## Install and run
- Python 3.x
- `pip` for package management
- Create env for Win
  - python -m venv env
  - env\Scripts\activate 

- Run 
  - By specific test: `pytest tests/test_book.py`
  - By folder tests: `pytest tests/`
  - By tags: `pytest -m SMOKE`
  - Run options:
    - pytest --ff option: all tests will be run but the first previous failures will be executed first
    - pytest --showlocals     # show local variables in tracebacks
    - pytest -l               # show local variables (shortcut)
    - pytest --no-showlocals  # hide local variables (if addopts enables them)
    - pytest --capture=fd  # default, capture at the file descriptor level
    - pytest --capture=sys # capture at the sys level
    - pytest --capture=no  # don't capture
    - pytest -s            # don't capture (shortcut)
    - pytest --capture=tee-sys # capture to logs but also output to sys level streams
    - pytest --tb=auto    # (default) 'long' tracebacks for the first and last
    - pytest --tb=long    # exhaustive, informative traceback formatting
    - pytest --tb=short   # shorter traceback format
    - pytest --tb=line    # only one line per failure
    - pytest --tb=native  # Python standard library formatting
    - pytest --tb=no      # no traceback at all

- Reports:
  - Config allure report:
    `[pytest]`
    `addopts = --alluredir=./allure-results`
    `allure_features = allure`
  - Read report:
    `allure serve /path/to/results`

## Project structure

    pytest_api_automation/
    │
    ├── configs/                 # Configuration files for different environments (dev, test, prod)
    │   ├── __init__.py
    │   ├── config_dev.py
    │   ├── config_prod.py
    │   └── config_test.py
    │
    ├── tests/                   # All your pytest test modules
    │   ├── __init__.py
    │   ├── test_users_api.py
    │   ├── test_products_api.py
    │   └── test_orders_api.py
    │
    ├── models/                  # Data models or schemas for validation
    │   ├── __init__.py
    │   ├── user.py
    │   ├── product.py
    │   └── order.py
    │
    ├── utils/                   # Utility functions and classes
    │   ├── __init__.py
    │   ├── api_client.py        # Custom API client to manage the REST API calls
    │   ├── data_loader.py       # Helper to load data for tests
    │   └── validators.py        # For validating API responses against schemas
    │── fixtures/                # Functions executed by Pytest before a test starts, and their results are passed to the body of the test
    │
    │── data/                    # Testdata
    │
    │── reports/                 # Test report
    │
    ├── requirements.txt         # Python dependencies for the project
    │
    └── pytest.ini               # Pytest configuration settings