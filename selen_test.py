from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

edge_options = Options()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.implicitly_wait(10)

# 1. Maximizăm fereastra imediat ce pornește browserul
driver.maximize_window()

driver.get("https://www.emag.ro/?msockid=31c98c6bef17601606879b4fee736185")

# 2. Folosim ID-ul exact al barei de căutare în loc de NAME
search_box = driver.find_element("xpath", "//form[@id='searchboxTrigger']//input")
#search_box = driver.find_element("css selector", "input.cdx-text-input__input")   nu prea se foloseste
search_box.send_keys("iphone 15")
search_box.send_keys(Keys.RETURN)