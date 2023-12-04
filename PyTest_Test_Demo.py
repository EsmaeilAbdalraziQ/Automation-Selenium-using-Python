import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(7)
    yield driver
    driver.close()
    driver.quit()
# ====================================================

def test_googleSearch(driver):
    driver.get("https://www.google.com/")
    googleSearchBox = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
    googleSearchBox.send_keys("Latest Lenovo Laptop")
    googleSearchBox.send_keys(Keys.ENTER)
    # driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
    time.sleep(5)
    print("Done Tested.!")