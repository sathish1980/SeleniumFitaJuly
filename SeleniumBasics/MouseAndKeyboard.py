import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class MouseActions:

    """
    Functions in ActionsChains
    MovetoElement
    click
    doubleclick
    contextclick
    sendKeys
    DragandDrop
    dragandDropBy
    clickAndHold
    release
    perform

    keyboardactions
    keyup
    keydown
    """
    def mouseActions(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.ebay.com/')
        browser.maximize_window()
        # Mouseaction we need to use ActionChains class
        mouse = ActionChains(browser)
        mouse.move_to_element(browser.find_element(by=By.XPATH,value="//*[@class='vl-flyout-nav__js-tab']//*[text()='Electronics']")).perform()
        mouse.move_to_element(browser.find_element(by=By.XPATH,value="//*[text()='Computers and tablets']")).click().perform()
        time.sleep(3)

    def mouseActions2(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.facebook.com/')
        browser.maximize_window()
        # Mouseaction we need to use ActionChains class
        mouse = ActionChains(browser)
        mouse.move_to_element(browser.find_element(by=By.ID,value="email")).send_keys("sathish").double_click().context_click().perform()
        time.sleep(3)

    def mouseActions3(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.leafground.com/drag.xhtml')
        browser.maximize_window()
        # Mouseaction we need to use ActionChains class
        mouse = ActionChains(browser)
        mouse.move_to_element(browser.find_element(by=By.ID,value="form:drag_content")).drag_and_drop(browser.find_element(by=By.ID,value="form:drag_content"),browser.find_element(by=By.ID,value="form:drop_content")).perform()

    def mouseActions4(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.leafground.com/drag.xhtml')
        browser.maximize_window()
        # Mouseaction we need to use ActionChains class
        mouse = ActionChains(browser)
        mouse.move_to_element(browser.find_element(by=By.ID, value="form:conpnl_content")).drag_and_drop_by_offset(browser.find_element(by=By.ID, value="form:conpnl_content"),500,0).perform()
        time.sleep(2)
        mouse.move_to_element(browser.find_element(by=By.ID, value="form:conpnl_content")).drag_and_drop_by_offset(browser.find_element(by=By.ID, value="form:conpnl_content"),-200,0).perform()
        time.sleep(3)

    def keyboardusingpyautogui(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        browser.get('https://www.facebook.com/')
        browser.maximize_window()
        # Mouseaction we need to use ActionChains class
        mouse = ActionChains(browser)

        mouse.move_to_element(browser.find_element(by=By.ID, value="email")).send_keys("sathish").key_down(Keys.TAB).key_up(Keys.TAB).perform()
        mouse.move_to_element(browser.find_element(by=By.ID, value="pass")).send_keys(
            "sathish").double_click().context_click().perform()
        time.sleep(3)
        pyautogui.press(['down','down','down'])
        """pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')"""
        pyautogui.press('enter')
        #pyautogui.press('control')
        pyautogui.hotkey('ctrl','v')
        time.sleep(3)



obj = MouseActions()
obj.keyboardusingpyautogui()