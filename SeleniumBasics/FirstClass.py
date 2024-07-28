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



class firstclass():

    def launch(self):
        # Initialize Chrome driver instance
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        #browser = webdriver.Edge(service=ChromiumService(executable_path=EdgeChromiumDriverManager().install()))
        #browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        # Navigate to the url
        browser.get('https://www.facebook.com/')
        browser.maximize_window()
        #browser.maximize_window()
        #browser.back()
        #time.sleep(3)
        #browser.forward()
        #time.sleep(3)
        #browser.refresh()


        browser.find_element(by=By.ID,value="email").send_keys("sathish")
        browser.find_element(by=By.NAME, value="pass").send_keys("kumar")
        #browser.find_element(by=By.CLASS_NAME, value="inputtext _55r1 _6luy _9npi").send_keys("kumar")
        time.sleep(3)
        browser.find_element(by=By.CSS_SELECTOR,value="input#email").clear()
        #browser.find_element(by=By.CSS_SELECTOR, value="input.inputtext _55r1 _6luy").clear()
        browser.find_element(by=By.CSS_SELECTOR, value="input[name=email]").clear()
        #browser.find_element(by=By.CSS_SELECTOR, value="input.inputtext _55r1 _6luy[name=email]").clear()
        """
        startswith - ^  -input[name^=ema]"
        endsWith - $    -input[name$=il]"
        contains - *    -input[name*=ema]"
        """
        time.sleep(2)
        browser.find_element(by=By.XPATH,value="//input[@placeholder='Email address or phone number']").send_keys("test")
        #browser.find_element(by=By.LINK_TEXT,value="Forgotten password?").click()
        time.sleep(2)
        browser.find_element(by=By.XPATH,value="//*[contains(@class,'_55r1') and @id='pass']").clear()
        browser.find_element(by=By.XPATH,value="//button[@id='u_0_9_RT' or starts-with(@id,'U_0_9')]").send_keys("FITA")
        browser.find_element(by=By.PARTIAL_LINK_TEXT, value=" passw").click()
        # Close the driver
        browser.quit()

    def createAccoutn(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        # browser = webdriver.Edge(service=ChromiumService(executable_path=EdgeChromiumDriverManager().install()))
        # browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        # Navigate to the url
        browser.get('https://www.facebook.com/')
        browser.maximize_window()
        browser.find_element(by=By.XPATH,value="//*[text()='Create new account']").click()
        #browser.implicitly_wait(60)
        #time.sleep(60)

        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.NAME, "firstname")))
        browser.find_element(by=By.NAME,value="firstname").send_keys("sathish")
        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.NAME, "lastname")))
        browser.find_element(by=By.NAME,value="lastname").send_keys("FITA")
        time.sleep(2)


obj = firstclass()
obj.createAccoutn()