import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium_framework import Selenium
import pytest
import re
@pytest.mark.usefixtures("setup")

class TestUrunDetaylari:
    
    def test_urun_adet_kontrol(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        urun=self.driver.find_element(By.XPATH,"//div[@class='item-box']//h2/a[contains(text(),'14.1-inch Laptop')]").click()
        time.sleep(2)

        shopping_card_items=self.driver.find_element(By.XPATH,"//span[@class='cart-qty']").text
        shopping_card_items=re.findall(r'\d+', shopping_card_items)
        onceki_urun_adet=int(shopping_card_items[0])
        
        urun_adet=self.driver.find_element(By.XPATH,"//input[@id='addtocart_31_EnteredQuantity']").clear()
        urun_adet=self.driver.find_element(By.XPATH,"//input[@id='addtocart_31_EnteredQuantity']").send_keys("2")
        urun_adet=self.driver.find_element(By.XPATH,"//input[@id='addtocart_31_EnteredQuantity']").get_attribute("value")
        urun_adet=re.findall(r'\d+', urun_adet)
        
        urun_ekle=self.driver.find_element(By.XPATH,"//input[@id='add-to-cart-button-31']").click()
        time.sleep(2)
        shopping_card_items=self.driver.find_element(By.XPATH,"//span[@class='cart-qty']").text
        shopping_card_items=re.findall(r'\d+', shopping_card_items)
        sonraki_urun_adet=int(shopping_card_items[0])
        
        assert onceki_urun_adet+int(urun_adet[0]) == sonraki_urun_adet
                       
    




