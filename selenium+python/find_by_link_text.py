from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

class DemoFindElementByid:
    def locate_by_id_demo(self):
        driver.get("https://www.emag.ro/")
        driver.find_element(By.XPATH, "//input[@id='searchboxTrigger']").send_keys('test@')
        driver.find_element(By.XPATH, "//i[@class='em em-search']")
        

findbyid = DemoFindElementByid()
findbyid.locate_by_id_demo()
bara_cautare = driver.find_element(By.XPATH, "//i[@class='em em-search']")
bara_cautare.send_keys("casti wireless")

# Pasul 2: Găsești BUTONUL de căutare (lupa) cu noul tău XPath
buton_cautare = driver.find_element(By.XPATH, "//i[@class='em em-search']")

# Pasul 3: Dai click efectiv pe el
buton_cautare.click()
time.sleep(10)