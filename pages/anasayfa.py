import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Anasayfa():

    def __init__(self, driver):
        self.driver = driver
        
    def anasayfadan_urun_sec(self,xpath):
        self.driver.find_element(By.XPATH,xpath).click()
