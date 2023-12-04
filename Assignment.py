import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# ========================================================================================================
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()


# ========================================================================================================
@pytest.mark.parametrize("email, password", [
    ("esmaeil.abdalraziq@gmail.com", "**********")
])
# ========================================================================================================
def test_amazon_login(driver, email, password):
    driver.get("https://www.amazon.eg/")
    driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
    driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@id='continue']").click()
    driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
    time.sleep(2)
    if (driver.find_element(By.XPATH, "//input[@id='input-box-otp']")):  ##If OTP Found
        # 11 | click |
        driver.find_element(By.XPATH, "//input[@id='input-box-otp']").click()
        # 12 | type |
        driver.find_element(By.XPATH, "//input[@id='input-box-otp']").send_keys("171100")
        # 13 | sendKeys |
        driver.find_element(By.XPATH, "//input[@id='input-box-otp']").send_keys(Keys.ENTER)
        time.sleep(1)
    else:
        assert "LogIn Successfully" in driver.page_source
        print("Done Tested.!")


# ========================================================================================================
def test_amazonSelectLanguage(driver):
    driver.get("https://www.amazon.eg")
    amazonSelectLang = driver.find_element(By.XPATH, "//a[@id='icp-nav-flyout']")
    amazonSelectLang.click()
    engLang = driver.find_element(By.XPATH,
                                  "//body/div[@id='a-page']/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/label[1]/i[1]")
    engLang.click()
    saveButton = driver.find_element(By.XPATH, "//body/div[@id='a-page']/div[1]/div[1]/span[2]/span[1]/input[1]")
    saveButton.click()
    HomePage = driver.find_element(By.XPATH, "//a[@id='nav-logo-sprites']")
    HomePage.click()
    print("Done, English Language Selected")
    time.sleep(2.0)


# =======================================================================================================
def test_amazonSearchProduct(driver):
    driver.get("https://www.amazon.eg")

    # test_amazon_login(driver, "esmaeil.abdalraziq@gmail.com", "**********")  # Login User First

    # driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
    # driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("esmaeil.abdalraziq@gmail.com")
    # driver.find_element(By.XPATH, "//input[@id='continue']").click()
    # driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("**********")
    # driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()

    amazon_search_box = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    amazon_search_box.send_keys("Lenovo Laptop")
    driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
    # amazon_search_box.send_keys(Keys.ENTER)
    # Select Item First
    select_item = driver.find_element(By.XPATH, "//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div["
                                                "1]/span[1]/div[1]/div[6]/div[1]/div[1]/span[1]/div[1]/div[1]/div["
                                                "2]/div[1]/h2[1]/a[1]")
    select_item.click()
    time.sleep(1.0)
    # Add Item to Cart
    # add_item_to_cart = driver.find_element(By.XPATH, "//button[@id='a-autoid-1-announce']")
    add_item_to_cart = driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']")
    add_item_to_cart.click()
    time.sleep(5.0)
    if (driver.find_element(By.XPATH, "//span[@id='attachSiNoCoverage-announce']")): ##If announce Found
        driver.find_element(By.XPATH, "//span[@id='attachSiNoCoverage-announce']").click()#ignore with No Thanks

    open_cart = driver.find_element(By.XPATH, "//a[@id='nav-cart']")
    open_cart.click()
    time.sleep(3.0)
    # check if element with keyword lenovo found
    cart_items = driver.find_elements(By.XPATH, "//div[@id='sc-active-cart']")
    if(len(cart_items) > 0):
        time.sleep(2.0)
        print("Item Found")
        time.sleep(2.0)
    else:
        time.sleep(2.0)
        print("No Items Added")

