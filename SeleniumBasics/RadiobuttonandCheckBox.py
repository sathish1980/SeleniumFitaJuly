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
class radioAndCheck():

    def radiobutton(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.facebook.com/')
        browser.maximize_window()
        browser.find_element(by=By.XPATH, value="//*[text()='Create new account']").click()
        # browser.implicitly_wait(60)
        # time.sleep(60)

        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.NAME, "firstname")))
        browser.find_element(by=By.NAME, value="firstname").send_keys("sathish")
        browser.find_element(by=By.XPATH, value="//*[@class='_8esa' and @value='1']").click()
        time.sleep(3)

    def check_BOX(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.leafground.com/checkbox.xhtml')
        browser.maximize_window()
        browser.find_element(by=By.XPATH,value="//*[@id='j_idt87:j_idt89']//div[starts-with(@class,'ui-chkbox-box')]").click()
        classname = browser.find_element(by=By.XPATH, value="//*[@id='j_idt87:j_idt89']//div[starts-with(@class,'ui-chkbox-box')]").get_attribute("class")
        if(classname.__contains__("ui-state-active")):
            print("test passed")
        else:
            print("test failed")
        time.sleep(3)

obj =radioAndCheck()
obj.radiobutton()
obj.check_BOX()