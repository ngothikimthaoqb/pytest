import pytest

from utils import config
from utils.random import generate_random_character, generate_secure_password

@pytest.fixture(scope="function")    
def user_data(api):
    username = f"usertest{generate_random_character(6)}"
    password = generate_secure_password()
    body = {
        "userName": username,
        "password": password
    }

    resp = api.post(config["apiPath"]["users"]["createUser"], body)
    assert resp.status_code == 201
    userResp = {
        "userName": username,
        "password": password,
        "userID": resp.json()['userID']
        }

    token_resp = api.post(config["apiPath"]["users"]["token"], body)
    assert token_resp.status_code == 200
    assert token_resp.json()['status'] == "Success"

    authorized_resp = api.post(config["apiPath"]["users"]["authorized"], body)
    assert authorized_resp.status_code == 200
    assert authorized_resp.json() == True
    
    yield userResp
