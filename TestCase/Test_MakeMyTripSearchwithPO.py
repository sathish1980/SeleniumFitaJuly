import time

from selenium.webdriver.common.by import By

from SeleniumFitaJuly.Pages.SearchPage import searchpage
from SeleniumFitaJuly.BrowserLaunch.Browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from SeleniumFitaJuly.Pages.SearchResultPage import searchResultPage


class Test_MakeMytrip(Browser):

    global browser
    def test_validflightsearchwithPO(self,ValidSearch):
        self.browser = Browser.Launch_Browser(self)
        self.browser.get("https://www.makemytrip.com/")
        time.sleep(4)
        sp = searchpage(self.browser)
        srp = searchResultPage(self.browser)
        self.browser.find_element(by=By.XPATH,value="//*[@data-cy='closeModal']").click()
        sp.clickOnFrom(self.browser)
        time.sleep(1)
        sp.listimplementation(self.browser, ValidSearch[0])
        sp.clickOnto(self.browser)
        time.sleep(1)
        sp.listimplementation(self.browser, ValidSearch[1])
        time.sleep(3)
        sp.DateSlection(self.browser, ValidSearch[2])
        time.sleep(3)
        sp.clickOnSearchButton(self.browser)
        time.sleep(10)
        actualError = srp.ValidateError(self.browser)
        extectedError = "NETWORK PROBLEM"
        assert actualError == extectedError
        Browser.Close_Browser(self)

    def test_validflightsearchwithPOwithmultipledata(self, SearchWithMultiDate):
        self.browser = Browser.Launch_Browser(self)
        self.browser.get("https://www.makemytrip.com/")
        time.sleep(4)
        sp = searchpage(self.browser)
        srp = searchResultPage(self.browser)
        self.browser.find_element(by=By.XPATH, value="//*[@data-cy='closeModal']").click()
        sp.clickOnFrom(self.browser)
        time.sleep(1)
        sp.listimplementation(self.browser, SearchWithMultiDate[0])
        sp.clickOnto(self.browser)
        time.sleep(1)
        sp.listimplementation(self.browser, SearchWithMultiDate[1])
        time.sleep(3)
        sp.DateSlection(self.browser, SearchWithMultiDate[2])
        time.sleep(3)
        sp.clickOnSearchButton(self.browser)
        time.sleep(10)
        actualError = srp.ValidateError(self.browser)
        extectedError = "NETWORK PROBLEM"
        assert actualError == extectedError
        Browser.Close_Browser(self)

    def test_validflightsamecityerrorinPO(self):
        self.browser = Browser.Launch_Browser(self)
        self.browser.get("https://www.makemytrip.com/")
        time.sleep(4)
        sp = searchpage(self.browser)
        srp = searchResultPage(self.browser)
        self.browser.find_element(by=By.XPATH,value="//*[@data-cy='closeModal']").click()
        sp.clickOnFrom(self.browser)
        time.sleep(1)
        sp.listimplementation(self.browser, "MAA")
        sp.clickOnto(self.browser)
        time.sleep(1)
        sp.listimplementation(self.browser, "MAA")
        time.sleep(3)
        #time.sleep(3)
        exepcetedsamecityerror = "From & To airports cannot be the same"
        actualdssmrcityerror = sp.ValidatesamecityError(self.browser)
        assert exepcetedsamecityerror == actualdssmrcityerror
        Browser.Close_Browser(self);
