import allure
from api_utils.api_client import APIClient
from api_utils.allure_helpers import attach_headers


client = APIClient()


@allure.title("Verify GET Users API")
def test_get_users():

    with allure.step("Show request headers"):

        attach_headers(client.HEADERS)

    with allure.step("Send GET users request"):

        response = client.get_users()

    with allure.step("Validate status code"):

        assert response.status_code == 200

    with allure.step("Validate response data"):

        data = response.json()

        assert len(data) > 0


@allure.title("Verify Create User API")
def test_create_user():

    with allure.step("Show request headers"):

        attach_headers(client.HEADERS)

    payload = {
        "name": "Alisha",
        "job": "QA Engineer"
    }

    with allure.step("Send POST request"):

        response = client.create_user(payload)

    with allure.step("Validate response"):

        assert response.status_code == 201

        response_data = response.json()

        assert response_data["name"] == "Alisha"

        assert response_data["job"] == "QA Engineer"


@allure.title("Verify Update User API")
def test_update_user():

    with allure.step("Show request headers"):

        attach_headers(client.HEADERS)

    payload = {
        "name": "Alisha Updated",
        "job": "Senior QA Engineer"
    }

    with allure.step("Send PUT request"):

        response = client.update_user(1, payload)

    with allure.step("Validate response"):

        assert response.status_code == 200

        response_data = response.json()

        assert response_data["name"] == "Alisha Updated"

        assert response_data["job"] == "Senior QA Engineer"


@allure.title("Verify Delete User API")
def test_delete_user():

    with allure.step("Show request headers"):

        attach_headers(client.HEADERS)

    with allure.step("Send DELETE request"):

        response = client.delete_user(1)

    with allure.step("Validate response"):

        assert response.status_code == 200