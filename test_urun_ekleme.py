import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.anasayfa import Anasayfa
from pages.urun_detay_sayfasi import UrunDetaySayfasi
from selenium_framework import Selenium
import pytest
import re
@pytest.mark.usefixtures("setup")

class TestUrunDetaylari:
    
    def test_urun_adet_kontrol(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        anasayfa=Anasayfa(self.driver)
        urun_detay_sayfasi=UrunDetaySayfasi(self.driver)
        self.driver.implicitly_wait(10)
        anasayfa.anasayfadan_urun_sec("/html/body/div[4]/div[1]/div[4]/div[3]/div/div/div[3]/div[6]/div/div[2]/h2/a")
        time.sleep(2)

        onceki_urun_adeti=urun_detay_sayfasi.urun_adeti()
        
        urun_adet_gostergesi=urun_detay_sayfasi.urun_adeti_gostergesi()
        
        urun_detay_sayfasi.urun_ekle_butonuna_basma()
        
        time.sleep(2)
        sonraki_urun_adet=urun_detay_sayfasi.urun_adeti()
        
        assert onceki_urun_adeti+int(urun_adet_gostergesi[0]) == sonraki_urun_adet
                       
    




