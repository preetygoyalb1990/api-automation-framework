import allure
from logger_config import logger   # <-- ADDED
from pages.login_page import LoginPage


@allure.feature("Login")
@allure.story("Valid credentials")
@allure.title("Valid login test")
@allure.description("Verify user can login with correct username and password")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(page):

    login_page = LoginPage(page)

    with allure.step("Open login page"):
        logger.info("Opening login page")   # <-- ADDED
        login_page.open_login_page()

    with allure.step("Enter valid username"):
        logger.info("Entering valid username")   # <-- ADDED
        login_page.enter_username("tomsmith")

    with allure.step("Enter valid password"):
        logger.info("Entering valid password")   # <-- ADDED
        login_page.enter_password("SuperSecretPassword!")

    with allure.step("Click login button"):
        logger.info("Clicking login button")   # <-- ADDED
        login_page.click_login()

    with allure.step("Verify Secure Area page is displayed"):
       logger.info("Verifying secure area heading")

    try:
        assert "Secure Area" in login_page.get_heading()
        logger.info("Login successful")

    except AssertionError:
        logger.error("Secure Area heading not found")
        raise


@allure.feature("Login")
@allure.story("Invalid password")
@allure.title("Invalid password test")
@allure.description("Verify error message appears when user enters wrong password")
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_password(page):

    login_page = LoginPage(page)

    with allure.step("Open login page"):
        logger.info("Opening login page")   # <-- ADDED
        login_page.open_login_page()

    with allure.step("Enter valid username"):
        logger.info("Entering valid username")   # <-- ADDED
        login_page.enter_username("tomsmith")

    with allure.step("Enter wrong password"):
        logger.info("Entering wrong password")   # <-- ADDED
        login_page.enter_password("wrongpassword")

    with allure.step("Click login button"):
        logger.info("Clicking login button")   # <-- ADDED
        login_page.click_login()

    with allure.step("Verify invalid password error message"):
        logger.info("Verifying invalid password error message")   # <-- ADDED
        assert "Your password is invalid!" in login_page.get_error_message()