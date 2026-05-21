import allure
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page(request):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        yield page

        if request.node.rep_call.failed:

            screenshot = page.screenshot()

            allure.attach(
                screenshot,
                name="failure screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)
    