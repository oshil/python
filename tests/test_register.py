import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import generate_email, save_user_data


def test_register_user(driver):
    allure.dynamic.suite("Login")
    allure.dynamic.title("Register")

    driver.get("https://practice.automationtesting.in/my-account/")
    email = generate_email()
    password = "12345Oo!!!!!!"

    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys(password)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "register")))
    breakpoint()
    driver.find_element(By.NAME, "register").click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "woocommerce-MyAccount-content")))
    welcome = driver.find_element(By.CLASS_NAME, "woocommerce-MyAccount-content").text
    assert "Hello" in welcome

    save_user_data(email, password)
