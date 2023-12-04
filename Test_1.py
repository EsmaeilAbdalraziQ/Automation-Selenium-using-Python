from selenium import webdriver
from selenium.webdriver.chrome.service import service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()

driver.get("https://google.com")
# title = driver.title
driver.implicitly_wait(0.10)

driver.close()
driver.quit()

print("Done")