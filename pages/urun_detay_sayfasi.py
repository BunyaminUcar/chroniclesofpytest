import re
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class UrunDetaySayfasi():
    def __init__(self, driver):
        self.driver = driver

    def urun_adeti(self):
        shopping_card_items=self.driver.find_element(By.XPATH,"//span[@class='cart-qty']").text
        shopping_card_items=re.findall(r'\d+', shopping_card_items)
        urun_adet=int(shopping_card_items[0])
        return urun_adet
    
    def urun_adeti_gostergesi(self):
        urun_adet=self.driver.find_element(By.XPATH,"//input[contains(@id, 'EnteredQuantity')]").clear()
        urun_adet=self.driver.find_element(By.XPATH,"//input[contains(@id, 'EnteredQuantity')]").send_keys("2")
        urun_adet=self.driver.find_element(By.XPATH,"//input[contains(@id, 'EnteredQuantity')]").get_attribute("value")
        urun_adet=re.findall(r'\d+', urun_adet)
        return urun_adet
    
    def urun_ekle_butonuna_basma(self):
        self.driver.find_element(By.XPATH,"//input[contains(@id, 'add-to-cart')]").click()