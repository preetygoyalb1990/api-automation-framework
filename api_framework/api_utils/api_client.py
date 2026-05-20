import requests
from logger_config import logger


class APIClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    def get_users(self):

        logger.info("Sending GET request to users API")

        response = requests.get(
            f"{self.BASE_URL}/users",
            headers=self.HEADERS
        )

        logger.info(f"Response status code: {response.status_code}")

        return response

    def create_user(self, data):

        logger.info("Sending POST request to create user")

        response = requests.post(
            f"{self.BASE_URL}/users",
            json=data,
            headers=self.HEADERS
        )

        logger.info(f"Response status code: {response.status_code}")

        return response

    def update_user(self, user_id, data):

        logger.info(f"Sending PUT request to update user {user_id}")

        response = requests.put(
            f"{self.BASE_URL}/users/{user_id}",
            json=data,
            headers=self.HEADERS
        )

        logger.info(f"Response status code: {response.status_code}")

        return response

    def delete_user(self, user_id):

        logger.info(f"Sending DELETE request for user {user_id}")

        response = requests.delete(
            f"{self.BASE_URL}/users/{user_id}",
            headers=self.HEADERS
        )

        logger.info(f"Response status code: {response.status_code}")

        return response