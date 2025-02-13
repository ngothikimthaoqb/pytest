import pytest

from utils import config
from utils.json_schema_validator import verify_json_schema, load_json_data
from utils.random import generate_random_character

@pytest.fixture(scope="class")
def invalid_user():
    username = f"usertest{generate_random_character(6)}"
    body = {
            "userName": username,
            "password": "11111"
        }
    return body 

@pytest.mark.usefixtures("api", "user_data")
@pytest.mark.SMOKE
@pytest.mark.REGRESSION
class TestUser:
    def test_creat_user_possitive(self, user_data):
        user_expected = load_json_data('../schemas/user/create_user.json')
        verify_json_schema(user_data, user_expected)

    def test_creat_user_invalid_pass_negative(self, api):
        username = f"usertest{generate_random_character(6)}"
        body = {
            "userName": username,
            "password": "11111"
        }

        resp = api.post(config["apiPath"]["users"]["createUser"], body)
        assert resp.status_code == 400
        error_message = "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer."
        assert resp.json()["message"] == error_message

    def test_get_token_positive(self, api, user_data):
        body = {
            "userName": user_data["userName"],
            "password": user_data["password"]
        }

        resp = api.post(config["apiPath"]["users"]["token"], body)
        assert resp.status_code == 200
        token_resp = resp.json()
        token_expected = load_json_data('../schemas/user/token.json')
        verify_json_schema(token_resp, token_expected)
        assert token_resp['status'] == "Success"

    def test_get_token_negative(self, api, invalid_user):
        resp = api.post(config["apiPath"]["users"]["token"], invalid_user)
        assert resp.status_code == 200
        token_resp = resp.json()
        assert token_resp['status'] == "Failed"
        
    def test_authorized_positive(self, api, user_data):
        body = {
            "userName": user_data["userName"],
            "password": user_data["password"]
        }

        resp = api.post(config["apiPath"]["users"]["authorized"], body)
        assert resp.status_code == 200
        assert resp.json() == True

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_skip(self, api, user_data):
        body = {
            "userName": user_data["userName"],
            "password": user_data["password"]
        }

        resp = api.post(config["apiPath"]["users"]["authorized"], body)
        assert resp.status_code == 200
        assert resp.json() == True