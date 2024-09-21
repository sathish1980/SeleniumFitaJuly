from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
class searchResultPage():

    def __init__(self,browser):
        self.browser = browser
    def ValidateError(self, browser1):
        WebDriverWait(browser1, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='error-title']")))
        return browser1.find_element(by=By.XPATH, value="//*[@class='error-title']").text