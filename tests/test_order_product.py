import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login


def test_order_product(driver):
    allure.dynamic.suite("Order Product")
    allure.dynamic.title("Login and verify product test")

    login_user(driver)

    product = verify_product(driver)

    submit_product(driver, product)

    verify_basket(driver)

@allure.step("Login User")
def login_user(driver):
    login(driver)


@allure.step("Verify Basket")
def verify_basket(driver):
    product_result = "//*[@class= 'cart_item']//*[text() = 'Android Quick Start Guide']"
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, product_result)))
    product_result_text = driver.find_element(By.XPATH, product_result).text
    assert "Android Quick Start Guide" in product_result_text

@allure.step("Submit Product")
def submit_product(driver, product):
    add_to_basket = product + "//*[ text() = 'Add to basket']"
    add_to_basket_text = driver.find_element(By.XPATH, add_to_basket).text
    assert "ADD TO BASKET" in add_to_basket_text
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          driver.find_element(By.XPATH, product + "//*[text() = 'Android Quick Start Guide']"))
    driver.find_element(By.XPATH, add_to_basket).click()
    view_basket = product + "//*[ text() = 'View Basket']"
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, view_basket)))
    driver.find_element(By.XPATH, view_basket).click()

@allure.step("Verify Product")
def verify_product(driver):
    driver.find_element(By.ID, "menu-item-40").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "woocommerce-breadcrumb")))
    shop = driver.find_element(By.CLASS_NAME, "woocommerce-breadcrumb").text
    assert "Home / Shop" in shop
    product = "//*[contains(@class, 'post-169 product type-product status-publish product_cat-android product_tag-android has-post-title no-post-date has-post-category has-post-tag has-post-comment has-post-author first instock sale downloadable taxable shipping-taxable purchasable product-type-simple')]"
    product_name = driver.find_element(By.XPATH, product + "//*[text() = 'Android Quick Start Guide']").text
    assert "Android Quick Start Guide" in product_name
    return product
