from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium_framework import Selenium
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome("C:\chromewebdriver\chromedriver.exe")
    driver.maximize_window()
    yield driver
    driver.quit()

def get_menu_text(driver):
    driver.get("https://www.fullprogramlarindir.net/")
    driver.implicitly_wait(10)
    elements = driver.find_elements(By.CSS_SELECTOR,"ul#menu-menu > li > a")  
    menu=[]
    for i in elements:
        menu.append(i.text)
    return menu

def test_menu_bar_kontrol(driver):
    expected_menu = ["ANASAYFA","FULL PROGRAM INDIR","GÜNCEL İŞLETIM SISTEMLER","CEP MOBIL","FULL OYUN İNDIR","ÇEŞIT","YARDIM & İSTEK !"]
    assert get_menu_text(driver) == expected_menu