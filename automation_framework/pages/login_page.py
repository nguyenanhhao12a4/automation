from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.username = (By.XPATH, "//input[@name='username']")
        self.password = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def is_login_page_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.login_button)
            )
            return True
        except:
            return False   
        
    def login(self, username_value, password_value):
        self.get_element(self.username).send_keys(username_value)
        self.get_element(self.password).send_keys(password_value)
        self.get_element(self.login_button).click()