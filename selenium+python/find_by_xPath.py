from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

class DemoFindElementByid:
    def locate_by_id_demo(self):
        driver.maximize_window()
        driver.get("https://www.emag.ro/")
        driver.find_element(By.XPATH, "//input[@id='searchboxTrigger']").send_keys('casti wireless')
        driver.find_element(By.XPATH, "//i[@class='em em-search']").click()
        driver.find_element(By.XPATH, "//div[@class='container']//div[1]//div[1]//div[1]//div[4]//div[2]//form[1]//button[1]").click()
        
        
        
        time.sleep(10)

findbyid = DemoFindElementByid()
findbyid.locate_by_id_demo()