
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def login2(driver, username, password):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    # Chờ đến khi trường username xuất hiện
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    
    # Nhập tên đăng nhập
    username_field = driver.find_element("xpath", "//input[@name='username']")
    username_field.send_keys(username)

    # Nhập mật khẩu
    password_field = driver.find_element("xpath", "//input[@name='password']")
    password_field.send_keys(password)

    # Nhấn nút đăng nhập
    login_button = driver.find_element("xpath", "//button[@type='submit']")
    login_button.click()
    # Chờ đến khi tiêu đề sau đăng nhập xuất hiện
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"))
    )
    time.sleep(4)
    print("Login successful")

# Khởi tạo driver trước khi gọi hàm login2
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
login2(driver, "Admin", "admin123")
driver.quit()