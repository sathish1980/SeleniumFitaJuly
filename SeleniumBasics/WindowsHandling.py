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
class windowsHandling:

    def wndowsimplementation(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.leafground.com/window.xhtml')
        browser.maximize_window()
        # get current wondow name
        parentWindow=browser.current_window_handle
        print(parentWindow)
        #click on open button
        browser.find_element(by=By.ID,value="j_idt88:new").click()
        #get all window name
        allwindowName = browser.window_handles
        print(allwindowName)
        for eachwindow in allwindowName:
            if parentWindow!=eachwindow:
                browser.switch_to.window(eachwindow)
                elementexist = browser.find_elements(by=By.ID,value="menuform:j_idt39")
                if len(elementexist)>0:
                    browser.find_element(by=By.ID, value="menuform:j_idt40").click()
                    browser.find_element(by=By.ID, value="menuform:m_input").click()
                    browser.find_element(by=By.ID, value="j_idt88:name").send_keys("FITA")

        time.sleep(5)



obj = windowsHandling()
obj.wndowsimplementation()