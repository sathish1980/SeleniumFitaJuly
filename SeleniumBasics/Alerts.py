import time

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
class Alertsconcepts:

    def alertImplementation(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.leafground.com/alert.xhtml')
        browser.maximize_window()
        browser.find_element(by=By.ID,value="j_idt88:j_idt91").click()
        browser.switch_to.alert.accept()
        output= browser.find_element(by=By.ID,value="simple_result").text
        print(output)
        browser.find_element(by=By.ID, value="j_idt88:j_idt93").click()
        browser.switch_to.alert.dismiss()
        output1 = browser.find_element(by=By.ID, value="result").text
        print(output1)
        browser.find_element(by=By.ID, value="j_idt88:j_idt104").click()
        browser.switch_to.alert.send_keys("FITA")
        browser.switch_to.alert.accept()
        output3 = browser.find_element(by=By.ID, value="confirm_result").text
        print(output3)

obj = Alertsconcepts()
obj.alertImplementation()