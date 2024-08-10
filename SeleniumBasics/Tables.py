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
class tablesConcept:

    def tablesimplementation(self, expectedCountry):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.leafground.com/table.xhtml')
        browser.maximize_window()
        Allpage = browser.find_elements(by=By.XPATH,value="//*[@class='ui-paginator-pages']//a")
        for eachpage in range(1, len(Allpage) + 1):
            browser.find_element(by=By.XPATH, value="//*[@class='ui-paginator-pages']//a["+str(eachpage)+"]").click()
            time.sleep(2)
            allRows = browser.find_elements(by=By.XPATH,value="//*[@id='form:j_idt89_data']//tr")
            for eachrow in range(1,len(allRows)+1):
                actualCountry = browser.find_element(by=By.XPATH, value="//*[@id='form:j_idt89_data']//tr["+str(eachrow)+"]//td[2]//span[starts-with(@style,'vertical-align:')]").text
                if(expectedCountry==actualCountry):
                    name = browser.find_element(by=By.XPATH,
                                         value="//*[@id='form:j_idt89_data']//tr[" + str(eachrow) + "]").text
                    print(name)


        time.sleep(5)


obj = tablesConcept()
obj.tablesimplementation("India")