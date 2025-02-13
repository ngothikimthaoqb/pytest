## Install and Run Instructions
### Prerequisites
  - Python 3.x: Ensure Python 3.x is installed.
  - pip: A Python package manager.
### Environment Setup
  - For Windows, create a virtual environment:
    ```shell
    python -m venv env
    env\Scripts\activate
    ```
  - Install required libraries:
    ```shell 
    pip install -r requirements.txt 
    ```

### Running Tests
  - Specific Test File:
    ```
    shell pytest tests/test_book.py 
    ```
  - Test Folder:
    ```shell 
    pytest tests/ 
    ```
  - By tags:
    ```shell 
    pytest -m SMOKE 
    ```
  - Run in Parallel:
    ```shell 
    pytest -n 2 -m SMOKE 
    ```    
  - Run options:
    - --ff: Run previously failed tests first.
    - -l, --showlocals: Show local variables in tracebacks.
    - --capture=fd: Capture outputs at file descriptor level.
    - --tb=short: Use a shorter traceback format.

## Reports
  - Modify the pytest configuration file:
    ```shell 
    [pytest]
    addopts = --alluredir=./allure-results 
    ```   
  - To view the report locally:
    ```shell 
    allure serve /path/to/results 
    ```    

## Project structure

    pytest_api_automation/
    ├── .github/workflow         # Configuration CI/CD, run in parallel and publish report to github page    
    │   ├── python-test.yml      
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

## CI/CD 
 - Use github action at https://github.com/ngothikimthaoqb/pytest/actions
 - Run:
    - Automatically: 
      - New commit merge to master
      - At 2 AM on the first day of every month, UTC time
    - Manually: User can input tag and number of CPUs to run parallel
 - Reporting: Allure reports are published on https://ngothikimthaoqb.github.io/pytest/

This README provides an exhaustive guide on setting up, running, and managing your Python testing environment using pytest. This setup ensures a robust testing framework that can be automatically or manually triggered within a CI/CD pipeline, enhancing code quality and project maintenance.
