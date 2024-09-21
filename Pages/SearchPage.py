from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class searchpage():

    def __init__(self,browser):
        self.browser = browser
    def clickOnFrom(self, browser1):
        WebDriverWait(browser1, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@for='fromCity']")))
        browser1.find_element(by=By.XPATH, value="//*[@for='fromCity']").click()

    def listimplementation(self, browser1, expectedCountry):

        allCountries = browser1.find_elements(by=By.XPATH, value="//*[@id='react-autowhatever-1']//li")
        for eachcountry in range(1, len(allCountries) + 1):
            WebDriverWait(browser1, 60).until(
                EC.element_to_be_clickable((By.XPATH, "(//*[@id='react-autowhatever-1']//li)[last()]")))
            actualCountry = browser1.find_element(by=By.XPATH, value="//*[@id='react-autowhatever-1']//li[" + str(
                eachcountry) + "]//div[starts-with(@class,'font14')]").text
            if expectedCountry == actualCountry:
                browser1.find_element(by=By.XPATH,
                                      value="//*[@id='react-autowhatever-1']//li[" + str(eachcountry) + "]").click()
                break
        time.sleep(3)

    def DateSlection(self,browser1,expectedDate):
        allWeeks = browser1.find_elements(by=By.XPATH,value="(//*[@class='DayPicker-Body'])[last()]//*[@class='DayPicker-Week']")
        for eachWeek in range(1,len(allWeeks)+1):
            WebDriverWait(browser1, 60).until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='DayPicker-Body'])[last()]//*[@class='DayPicker-Week'][last()]")))
            allDaysinWeek = browser1.find_elements(by=By.XPATH,value="(//*[@class='DayPicker-Body'])[last()]//*[@class='DayPicker-Week'][1]//*[@class='DayPicker-Day']")
            for eachDay in range(1, len(allDaysinWeek) + 1):

                actualdateclass = browser1.find_element(by=By.XPATH,
                                                  value="(//*[@class='DayPicker-Body'])[last()]//*[@class='DayPicker-Week'][" + str(
                                                      eachWeek) + "]//*[@class='DayPicker-Day'][" + str(
                                                      eachDay) + "]").get_attribute("aria-disabled")

                if(actualdateclass=="false"):
                    actualdate = browser1.find_element(by=By.XPATH,value="(//*[@class='DayPicker-Body'])[last()]//*[@class='DayPicker-Week']["+str(eachWeek)+"]//*[@class='DayPicker-Day']["+str(eachDay)+"]//p[1]").text
                    if expectedDate==actualdate:
                        browser1.find_element(by=By.XPATH, value="(//*[@class='DayPicker-Body'])[last()]//*[@class='DayPicker-Week']["+str(eachWeek)+"]//*[@class='DayPicker-Day']["+str(eachDay)+"]//p[1]").click()
                        return
        time.sleep(3)

    def clickOnto(self, browser1):
        WebDriverWait(browser1, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@for='toCity']")))
        browser1.find_element(by=By.XPATH, value="//*[@for='toCity']").click()

    def ValidatesamecityError(self, browser1):
        WebDriverWait(browser1, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@data-cy='sameCityError']")))
        return browser1.find_element(by=By.XPATH, value="//*[@data-cy='sameCityError']").text

    def clickOnSearchButton(self,browser1):
        WebDriverWait(browser1, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='submit']")))
        browser1.find_element(by=By.XPATH, value="//*[@data-cy='submit']").click()