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
class dropdown:

    def dropdownImplementation(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.leafground.com/select.xhtml')
        browser.maximize_window()
        AutomationTools = Select(browser.find_element(by=By.XPATH,value="//*[@class='ui-selectonemenu']"))
        print(AutomationTools.is_multiple)
        """
        selectbyIndex
        selectbyvalue
        selectbyvisibletext
        
        mu;tiselect methods
        deselectbyIndex
        deselectbyvalue
        deselectbyvisibleText
        deselecall
        """
        AutomationTools.select_by_index(4)
        time.sleep(2)
        #AutomationTools.select_by_value()
        AutomationTools.select_by_visible_text("Playwright")
obj = dropdown()
obj.dropdownImplementation()