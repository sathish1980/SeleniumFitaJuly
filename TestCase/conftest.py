import time

import pytest
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

@pytest.fixture()
def browserlaunch():
    return webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    yield
    time.sleep(5)
    browser.quit()


@pytest.fixture
def password():
    return "admin"

@pytest.fixture
def username():
    return "kumar.sathish189@gmail.com"

@pytest.fixture()
def ValidSearch():
    return ["PNQ", "MAA", "24"]

@pytest.fixture(params=[("MAA", "BLR", "24"), ("PNQ", "MAA", "27")])
def SearchWithMultiDate(request):
    return request.param