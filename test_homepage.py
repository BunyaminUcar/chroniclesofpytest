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




class TestPage:
    
    def test_menu(self, driver):
        driver.get("https://www.fullprogramlarindir.net/")
        driver.implicitly_wait(10)
        elements = driver.find_elements(By.CSS_SELECTOR,"ul#menu-menu > li > a")  
        menu=[]
        for i in elements:
            menu.append(i.text)
        assert menu == ["ANASAYFA","FULL PROGRAM INDIR","GÜNCEL İŞLETIM SISTEMLER","CEP MOBIL","FULL OYUN İNDIR","ÇEŞIT","YARDIM & İSTEK !"]
    
    def test_urun_ismine_basinca_icerigi_gosteriliyor(self, driver):
        driver.get("https://www.fullprogramlarindir.net/")
        driver.implicitly_wait(10)
        link = driver.find_element(By.XPATH,"//*[@id='icerik']/div[3]/div[1]/div/h1/a")
        urun_adi = link.text.strip()
        link.click()
        driver.implicitly_wait(10)
        new_page_element=driver.find_element(By.XPATH,"//*[@id='icerik-yazi']/div[2]/h1/a").text.strip()
        assert urun_adi == new_page_element
        
        
        
        