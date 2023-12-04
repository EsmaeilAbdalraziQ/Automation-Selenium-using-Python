import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get("https://www.amazon.eg")
time.sleep(2.0)
amazonSelectLang = driver.find_element(By.XPATH,"//a[@id='icp-nav-flyout']").click()
time.sleep(2.0)
engLang = driver.find_element(By.XPATH, "//body/div[@id='a-page']/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/label[1]/i[1]").click()
time.sleep(2.0)
saveButton = driver.find_element(By.XPATH, "//body/div[@id='a-page']/div[1]/div[1]/span[2]/span[1]/input[1]").click()
time.sleep(2.0)
HomePage = driver.find_element(By.XPATH, "//a[@id='nav-logo-sprites']")
print("Done, English Language Selected")
time.sleep(2.0)

driver.close()
driver.quit()

print("Done")


# Test Case 3
# amazonSearchBox =  driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
# amazonSearchBox.send_keys("Lenovo Laptop")
# amazonSearchBox.send_keys(Keys.ENTER)
# # driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
# Add Item to Cart
# print("Item Found")
