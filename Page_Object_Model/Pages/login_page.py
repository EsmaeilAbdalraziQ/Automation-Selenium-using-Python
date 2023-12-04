import pytest
import time
from selenium import webdriver

from selenium.webdriver.common.by import By


class LoginPage:

    def __int__(self, driver):
        # self.driver = webdriver.Chrome() # web element locators
        self.driver = driver
        self.LoginButtonScreen = (By.ID, "nav-link-accountList-nav-line-1")
        self.email_Input = (By.XPATH, "//input[@id='ap_email']")
        self.password_Input = (By.XPATH, "//input[@id='ap_password']")
        self.continueButton = (By.XPATH, "//input[@id='continue']")
        self.logInSubmitButton = (By.XPATH, "//input[@id='signInSubmit']")

    #   Func For action for what we are going to Do
    def open_page_url(self, url):
        # driver = self.driver
        self.driver.get(url)

    def open_login_page(self):
        self.driver.find_element(*self.LoginButtonScreen).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_Input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_Input).send_keys(password)

    def click_continue_button(self):
        self.driver.find_element(*self.continueButton).click()

    def click_submit_login(self):
        self.driver.find_element(*self.logInSubmitButton).click()
