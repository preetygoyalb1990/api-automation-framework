import requests

from logger_config import logger


def test_get_users():

    logger.info("Sending GET request")

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    logger.info(f"Status code: {response.status_code}")

    assert response.status_code == 200

    data = response.json()

    logger.info("Validating response data")

    assert len(data) > 0

    assert data[0]["id"] == 1

    assert data[0]["name"] == "wrong name"

    assert "@" in data[0]["email"]


def test_create_user():

    data = {
        "name": "Alisha",
        "job": "QA Engineer"
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=data
    )

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["name"] == "Alisha"
    assert response_data["job"] == "QA Engineer"  

def test_update_user():

    updated_data = {
        "name": "Alisha Updated",
        "job": "Senior QA Engineer"
    }

    response = requests.put(
        "https://jsonplaceholder.typicode.com/users/1",
        json=updated_data
    )

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["name"] == "Alisha Updated"
    assert response_data["job"] == "Senior QA Engineer"

def test_delete_user():

    response = requests.delete(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    assert response.status_code == 200