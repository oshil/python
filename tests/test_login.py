import allure
from utils.helpers import login


def test_login(driver):
    allure.dynamic.suite("Login User")
    allure.dynamic.title("Login")
    login(driver)


