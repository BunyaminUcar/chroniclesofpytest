from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
url="https://testpages.herokuapp.com/styled/challenges/growing-clickable.html"

def get_driver(url):
    driver = webdriver.Chrome("C:\chromewebdriver\chromedriver.exe")
    driver.get(url)
    return driver

driver=get_driver(url)

# öğeyi ID ile seçin
example_element = driver.find_element(By.ID, "growbutton")

# öğenin class attribute'unu yazdırın
class_name = example_element.get_attribute("class")
print(class_name)

while True:
    if class_name != "styled-click-button showgrow":
        print("clickable")
        example_element.click()
        break
    else:
        class_name = example_element.get_attribute("class")

metin=driver.find_element(By.ID,"growbuttonstatus").text
print(metin)


# WebDriver'ı kapatın
driver.quit()



