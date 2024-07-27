import time

from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class firstclass():

    def launch(self):
        # Initialize Chrome driver instance
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        #browser = webdriver.Edge(service=ChromiumService(executable_path=EdgeChromiumDriverManager().install()))
        #browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        # Navigate to the url
        browser.get('https://www.facebook.com/')
        browser.maximize_window()
        #browser.maximize_window()
        browser.back()
        time.sleep(3)
        browser.forward()
        time.sleep(3)
        browser.refresh()


        browser.find_element(by=By.ID,value="email").send_keys("sathish")
        browser.find_element(by=By.NAME, value="pass").send_keys("kumar")
        #browser.find_element(by=By.CLASS_NAME, value="inputtext _55r1 _6luy _9npi").send_keys("kumar")
        time.sleep(3)
        # Close the driver
        browser.quit()

obj = firstclass()
obj.launch()