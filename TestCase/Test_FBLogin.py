import time

import pytest
from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
@pytest.mark.usefixtures("browserlaunch")
class Test_FBLogin:

    browser="null"
    def test_ValidLogin(self,password,username):
        self.browser.get('https://www.facebook.com/')
        self.browser.maximize_window()
        self.browser.find_element(by=By.ID,value="email").send_keys(username)
        self.browser.find_element(by=By.ID, value="pass").send_keys(password)
        self.browser.find_element(by=By.NAME, value="login").click()

    def test_ValidLogin_2(self,password,username):
        self.browser.get('https://www.facebook.com/')
        self.browser.maximize_window()
        self.browser.find_element(by=By.ID,value="email").send_keys(username)
        self.browser.find_element(by=By.ID, value="pass").send_keys(password)
        self.browser.find_element(by=By.NAME, value="login").click()


    @pytest.fixture()
    def browserlaunch(self):
        self.browser= webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        yield
        time.sleep(5)
        self.browser.quit()
