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
class FrameConcept:

    def frameImplementation(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.leafground.com/frame.xhtml')
        browser.maximize_window()
        #time.sleep(3)
        allFrames = browser.find_elements(by=By.TAG_NAME,value="iframe")
        for eachfrme in range(0,len(allFrames)):
            browser.switch_to.frame(eachfrme)
            elementexist = browser.find_elements(by=By.XPATH, value="//*[@id='Click' and contains(@style,'ff7295') ]")
            if(len(elementexist)>0):

                browser.find_element(by=By.XPATH,value="//*[@id='Click' and contains(@style,'ff7295') ]").click()
                browser.switch_to.default_content()
                break
            browser.switch_to.default_content()
        time.sleep(3)

obj=FrameConcept()
obj.frameImplementation()