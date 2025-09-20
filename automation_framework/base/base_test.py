import pytest
from selenium import webdriver
from time import sleep
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        #xac nhan trang login hien thi
        login_page = LoginPage(driver)
        assert login_page.is_login_page_displayed(), "Login page is not displayed"
        print("Login page is displayed")

        request.cls.driver = driver

        yield 
        driver.quit()
