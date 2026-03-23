from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

class DemoFindElementByid:
    def locate_by_id_demo(self):
        driver.get("https://www.emag.ro/")
        driver.find_element(By.ID, 'searchboxTrigger').send_keys('test@')
        time.sleep(10)

findbyid = DemoFindElementByid()
findbyid.locate_by_id_demo()