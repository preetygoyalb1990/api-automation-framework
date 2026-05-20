import json
import allure


def attach_headers(headers):

    allure.attach(
        json.dumps(headers, indent=4),
        name="Request Headers",
        attachment_type=allure.attachment_type.JSON
    )