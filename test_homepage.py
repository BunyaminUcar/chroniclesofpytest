from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.anasayfa import Anasayfa
from selenium_framework import Selenium
import pytest

"""@pytest.fixture
def driver():
    driver = webdriver.Chrome("C:\chromewebdriver\chromedriver.exe")
    driver.maximize_window()
    yield driver
    driver.quit()"""



@pytest.mark.usefixtures("setup")
class TestPage:
    
    def test_menu(self):
        self.driver.get("https://www.fullprogramlarindir.net/")
        anasayfa=Anasayfa(self.driver)
        menu = anasayfa.menu_itemlerini_getir()
        assert menu == ["ANASAYFA","FULL PROGRAM INDIR","GÜNCEL İŞLETIM SISTEMLER","CEP MOBIL","FULL OYUN İNDIR","ÇEŞIT","YARDIM & İSTEK !"]
    
    def test_urun_ismine_basinca_icerigi_gosteriliyor(self):
        self.driver.get("https://www.fullprogramlarindir.net/")
        anasayfa=Anasayfa(self.driver)
        urun_adi,new_page_element = anasayfa.urun_ismine_basinca_icerigi_gosteriliyor()
        assert urun_adi == new_page_element
        
        
        
        