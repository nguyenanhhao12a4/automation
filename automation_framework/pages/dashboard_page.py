from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_header = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    
    def is_dashboard_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.dashboard_header)
            )
            return True
        except:
            return False