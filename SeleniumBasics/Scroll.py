
import time


from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class scroll():
    browser = "null";
    def scrollimplementation(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.browser.get("https://leafground.com/drag.xhtml")
        self.browser.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        obj.screenshot("scrolldown")
        self.browser.execute_script("window.scrollTo(0, -100)")
        time.sleep(1)
        obj.screenshot("scrollup")
        self.browser.execute_script("window.scrollTo(-100,0)")
        time.sleep(1)
        self.browser.execute_script("window.scrollTo(100,0)")
        time.sleep(1)
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        obj.screenshot("completlyscrolldown")
        self.browser.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
        time.sleep(1)
        actualelement = self.browser.find_element(by=By.XPATH,value="//*[text()='Draggable Rows']")
        self.browser.execute_script("arguments[0].scrollIntoView();",actualelement)
        obj.screenshot("specifictotheelement")
        time.sleep(1)


    def screenshot(self, filename):
        self.browser.save_screenshot(
                "C:\\Users\\kumar\\PycharmProjects\\SeleniumFitaJuly\\Screenshot\\" + filename + ".png")


obj = scroll()
obj.scrollimplementation()


