
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_login_page_opens():
    driver = webdriver.Chrome()


    try:
        driver.get("https://demowebshop.tricentis.com/books")

        wait = WebDriverWait(driver, 10)

        email_field = wait.until(
            selenium.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[type='email']")
            )
        )

        password_field = wait.until(
            selenium.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[type='password']")
            )
        )

        assert email_field.is_displayed()
        assert password_field.is_displayed()

    finally:
        driver.quit()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_login_page_opens():
    driver = webdriver.Chrome()

    try:
        driver.get("https://telranedu.web.app/login")

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        assert "telranedu.web.app" in driver.current_url

    finally:
        driver.quit()