import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# Hàm khởi tạo driver
def init_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # maximize_window
    driver.maximize_window()

    # timeout settings
    driver.implicitly_wait(10)           # tìm element tối đa 10s
    driver.set_page_load_timeout(20)     # tải trang tối đa 20s
    driver.set_script_timeout(10)        # JS script tối đa 10s

    return driver


@pytest.mark.selenium
def test_all_functions():
    driver = init_driver()

    try:
        # get(url)
        driver.get("https://www.youtube.com/")
        time.sleep(2)

        # refresh
        driver.refresh()
        time.sleep(2)

        # back / forward (cần có history)
        driver.get("https://example.com")
        driver.back()     # quay lại YouTube
        time.sleep(2)
        driver.forward()  # tiến tới example.com
        time.sleep(2)

        # switch_to.active_element
        active = driver.switch_to.active_element
        print("Active element:", active.tag_name)

        # switch_to.frame / default_content (demo, cần iframe thật)
        # driver.switch_to.frame("frame_id")
        # driver.switch_to.default_content()

        # switch_to.alert (demo, cần alert thật)
        # driver.execute_script("alert('Hello Selenium!')")
        # alert = driver.switch_to.alert
        # print("Alert text:", alert.text)
        # alert.accept()

        # switch_to.window (mở tab mới để demo)
        driver.execute_script("window.open('https://www.wikipedia.org', '_blank');")
        time.sleep(2)
        windows = driver.window_handles
        print("Windows list:", windows)

        driver.switch_to.window(windows[1])   # sang Wikipedia
        print("Current URL:", driver.current_url)
        time.sleep(2)

        driver.switch_to.window(windows[0])   # quay lại tab đầu
        print("Back to first tab:", driver.current_url)

        # close() - đóng tab hiện tại
        driver.close()

    finally:
        # quit() - đóng toàn bộ browser
        driver.quit()