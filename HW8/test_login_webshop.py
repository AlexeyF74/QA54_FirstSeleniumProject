from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_page_opens():
    driver = webdriver.Chrome()

    try:
        driver.get("https://demowebshop.tricentis.com/books")

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        assert "demowebshop.tricentis.com" in driver.current_url

    finally:
        driver.quit()