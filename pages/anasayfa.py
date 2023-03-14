import pytest
from selenium.webdriver.common.by import By



class Anasayfa():

    def __init__(self, driver):
        self.driver = driver
        
    def anasayfadan_urun_sec(self,xpath):
        self.driver.find_element(By.XPATH,xpath).click()
        
    def menu_itemlerini_getir(self):
        self.driver.implicitly_wait(10)
        elements = self.driver.find_elements(By.CSS_SELECTOR,"ul#menu-menu > li > a")  
        menu=[]
        for i in elements:
            menu.append(i.text)
        return menu
    def urun_ismine_basinca_icerigi_gosteriliyor(self):
        self.driver.implicitly_wait(10)
        link = self.driver.find_element(By.XPATH,"//*[@id='icerik']/div[3]/div[1]/div/h1/a")
        urun_adi = link.text.strip()
        link.click()
        self.driver.implicitly_wait(10)
        new_page_element=self.driver.find_element(By.XPATH,"//*[@id='icerik-yazi']/div[2]/h1/a").text.strip()
        return urun_adi,new_page_element