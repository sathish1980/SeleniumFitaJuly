import time

from selenium.webdriver.common.by import By

from SeleniumFitaJuly.Pages.SearchPage import searchpage
from SeleniumFitaJuly.BrowserLaunch.Browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_MakeMytrip(Browser):

    global browser
    def test_validflightsearch(self):
        self.browser = Browser.Launch_Browser(self)
        self.browser.get("https://www.makemytrip.com/")
        time.sleep(4)
        sp = searchpage(self.browser)
        self.browser.find_element(by=By.XPATH,value="//*[@data-cy='closeModal']").click()
        sp.clickOnFrom(self.browser)
        time.sleep(1)
        Test_MakeMytrip.listimplementation(self,self.browser,"PNQ")
        Test_MakeMytrip.clickOnto(self, self.browser)
        time.sleep(1)
        Test_MakeMytrip.listimplementation(self, self.browser, "MAA")
        time.sleep(3)
        Test_MakeMytrip.DateSlection(self,self.browser,str(5))
        time.sleep(3)
        Test_MakeMytrip.clickOnSearchButton(self, self.browser)
        time.sleep(10)
        actualError = Test_MakeMytrip.ValidateError(self,self.browser)
        extectedError = "NETWORK PROBLEM"
        assert actualError == extectedError

        Browser.Close_Browser(self)

    def test_samecityflightsearcherror(self):
        self.browser = Browser.Launch_Browser(self)
        self.browser.get("https://www.makemytrip.com/")
        time.sleep(4)
        sp = searchpage(self.browser)
        self.browser.find_element(by=By.XPATH,value="//*[@data-cy='closeModal']").click()
        sp.clickOnFrom(self.browser)
        time.sleep(1)
        Test_MakeMytrip.listimplementation(self,self.browser,"PNQ")
        Test_MakeMytrip.clickOnto(self, self.browser)
        time.sleep(1)
        Test_MakeMytrip.listimplementation(self, self.browser, "PNQ")
        time.sleep(3)
        exepcetedsamecityerror = "From & To airports cannot be the same"
        actualdssmrcityerror =Test_MakeMytrip.ValidatesamecityError(self,self.browser)
        assert exepcetedsamecityerror == actualdssmrcityerror
        Browser.Close_Browser(self)

    def ValidatesamecityError(self, browser1):
        WebDriverWait(browser1, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@data-cy='sameCityError']")))
        return browser1.find_element(by=By.XPATH, value="//*[@data-cy='sameCityError']").text

    def ValidateError(self,browser1):
        WebDriverWait(browser1, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='error-title']")))
        return browser1.find_element(by=By.XPATH, value="//*[@class='error-title']").text
    def clickOnSearchButton(self,browser1):
        WebDriverWait(browser1, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='submit']")))
        browser1.find_element(by=By.XPATH, value="//*[@data-cy='submit']").click()

    def clickOnFrom(self,browser1):
        WebDriverWait(browser1, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@for='fromCity']")))
        browser1.find_element(by=By.XPATH, value="//*[@for='fromCity']").click()

    def clickOnto(self,browser1):
        WebDriverWait(browser1, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@for='toCity']")))
        browser1.find_element(by=By.XPATH, value="//*[@for='toCity']").click()
    def listimplementation(self,browser1,expectedCountry):

        allCountries = browser1.find_elements(by=By.XPATH,value="//*[@id='react-autowhatever-1']//li")
        for eachcountry in range(1,len(allCountries)+1):
            WebDriverWait(browser1, 60).until(EC.element_to_be_clickable((By.XPATH, "(//*[@id='react-autowhatever-1']//li)[last()]")))
            actualCountry = browser1.find_element(by=By.XPATH,value="//*[@id='react-autowhatever-1']//li["+str(eachcountry)+"]//div[starts-with(@class,'font14')]").text
            if expectedCountry==actualCountry:
                browser1.find_element(by=By.XPATH, value="//*[@id='react-autowhatever-1']//li[" + str(eachcountry) + "]").click()
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