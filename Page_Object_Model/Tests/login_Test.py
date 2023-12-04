import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Page_Object_Model.Pages.login_page import LoginPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# =====================================================================================================
# @pytest.mark.parametrize("email, password", [
#     ("esmaeil.abdalraziq@gmail.com", "**********")
# ])
# =====================================================================================================
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    yield driver
    driver.close()
    driver.quit()


def test_Login(driver):
    # chrome_driver = webdriver.Chrome()
    # driver = chrome_driver
    login_page = LoginPage()
    login_page.open_page_url("https://www.amazon.eg/")
    time.sleep(1)
    login_page.open_login_page()
    time.sleep(1)
    login_page.enter_email("esmaeil.abdalraziq@gmail.com")
    login_page.continueButton()
    time.sleep(1)
    login_page.password_Input("**********")
    login_page.click_submit_login()
    time.sleep(1)

    # driver.get("https://www.amazon.eg/")
    # driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
    # driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys(email)
    # driver.find_element(By.XPATH, "//input[@id='continue']").click()
    # driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys(password)
    # driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
    # time.sleep(2)
    # If_OTP_Found
    if (driver.find_element(By.XPATH, "//input[@id='input-box-otp']")):
        # 11 | click |
        driver.find_element(By.XPATH, "//input[@id='input-box-otp']").click()
        # 12 | type |
        driver.find_element(By.XPATH, "//input[@id='input-box-otp']").send_keys("171100")
        # 13 | sendKeys |
        driver.find_element(By.XPATH, "//input[@id='input-box-otp']").send_keys(Keys.ENTER)
        time.sleep(2)
    else:
        assert "LogIn Successfully" in driver.page_source
        print("Done Tested.!")
# ========================================================================================================
