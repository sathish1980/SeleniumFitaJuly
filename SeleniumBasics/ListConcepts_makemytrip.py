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
class lsitConcepts_makemytrip:

    def listimplementation(self,expectedCountry):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.makemytrip.com/')
        browser.maximize_window()
        WebDriverWait(browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='commonModal__close']")))
        browser.find_element(by=By.XPATH, value="//*[@class='commonModal__close']").click()
        WebDriverWait(browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@for='fromCity']")))
        browser.find_element(by=By.XPATH,value="//*[@for='fromCity']").click()
        allCountries = browser.find_elements(by=By.XPATH,value="//*[@id='react-autowhatever-1']//li")
        for eachcountry in range(1,len(allCountries)+1):
            WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "(//*[@id='react-autowhatever-1']//li)[last()]")))
            actualCountry = browser.find_element(by=By.XPATH,value="//*[@id='react-autowhatever-1']//li["+str(eachcountry)+"]//div[starts-with(@class,'font14')]").text
            if expectedCountry==actualCountry:
                browser.find_element(by=By.XPATH, value="//*[@id='react-autowhatever-1']//li[" + str(eachcountry) + "]").click()
                break
        time.sleep(3)


obj = lsitConcepts_makemytrip()
obj.listimplementation("PNQ")
