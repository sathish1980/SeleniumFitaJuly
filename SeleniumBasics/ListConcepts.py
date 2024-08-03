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
class lsitConcepts:

    def listimplementation(self,expectedCountry):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.leafground.com/select.xhtml')
        browser.maximize_window()
        browser.find_element(by=By.XPATH,value="//*[@id='j_idt87:country']//div[starts-with(@class,'ui-selectonemenu-trigge')]").click()
        allCountries = browser.find_elements(by=By.XPATH,value="//*[@id='j_idt87:country_items']//li")
        for eachcountry in allCountries:
            WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "(//*[@id='j_idt87:country_items']//li)[last()]")))
            #browser.find_element(by=By.NAME, value="firstname").send_keys("sathish")
            actualCountry =eachcountry.text
            if expectedCountry==actualCountry:
                eachcountry.click()
                break
        time.sleep(3)


obj = lsitConcepts()
obj.listimplementation("Germany")
