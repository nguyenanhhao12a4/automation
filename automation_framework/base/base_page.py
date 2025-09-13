from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
     
    def get_element(self, xpath):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(xpath)
        )
        return element
    
    def click(self, element):
        self.driver.click(element)
    
    def wait(self, driver, xpath):
        self.driver = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    
    def send_keys(self, key):
        self.driver.send_keys(key)
        
