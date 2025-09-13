import time
import pytest
from base.base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.usefixtures("setup")
class TestOrange(BaseTest):
    
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        
        #xac nhan dang nhap thanh cong va hien thi dashboard
        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.is_dashboard_displayed(), "Dashboard is not displayed after login"
        print("Dashboard is displayed !!!")
        print("Login successful !!!")
    
    # def test_add_vacancy(self):
    #     driver = self.driver
        
    #     # Nhấn vào menu "Recruitment"
    #     recruitment_menu = driver.find_element(By.XPATH, "//span[text()='Recruitment']")
    #     recruitment_menu.click()

    #     # Chờ đến khi trang Recruitment tải xong
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"))
    #     )

    #     # Nhấn vào nút "vacancies"
    #     vacancies_button = driver.find_element(By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item' and text()='Vacancies']")
    #     vacancies_button.click()

    #     # Chờ đến khi trang vacancies tải xong
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//h5[@class='oxd-text oxd-text--h5 oxd-table-filter-title']"))
    #     )
    #     time.sleep(4)
    #     print("Add vacancy successful")
        
    #     # Nhấn vào nút "Add"
    #     add_button = driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    #     add_button.click()

    #     # Chờ đến khi trang thêm vị trí tuyển dụng tải xong
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']"))
    #     )
    #     time.sleep(4)
    #     print("Add vacancy successful")
        