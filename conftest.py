from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium_framework import Selenium
import pytest
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome("C:\chromewebdriver\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.fullprogramlarindir.net/")
    request.cls.driver = driver
    yield
    driver.quit()
