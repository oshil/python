import random
import string
import json
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

USER_DATA_PATH = os.path.join(os.path.dirname(__file__), "user_data.json")


def generate_email():
    random_digits = ''.join(random.choices(string.digits, k=4))
    return f"testUser{random_digits}@test.com"


def save_user_data(email, password):
    data = {"email": email, "password": password}
    with open(USER_DATA_PATH, "w") as f:
        json.dump(data, f)


def load_user_data():
    with open(USER_DATA_PATH, "r") as f:
        return json.load(f)


def login(driver):
    credentials = load_user_data()
    email = credentials["email"]
    password = credentials["password"]
    driver.get("https://practice.automationtesting.in/my-account/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "woocommerce-MyAccount-content")))
    welcome = driver.find_element(By.CLASS_NAME, "woocommerce-MyAccount-content").text
    assert "Hello" in welcome
