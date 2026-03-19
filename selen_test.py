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

driver.get("https://ro.wikipedia.org/wiki/Pagina_principal%C4%83")

# 2. Folosim ID-ul exact al barei de căutare în loc de NAME
search_box = driver.find_element("xpath", "//form[@id='searchform']//input")
#search_box = driver.find_element("css selector", "input.cdx-text-input__input")   nu prea se foloseste
search_box.send_keys("Buna Ziua")
search_box.send_keys(Keys.RETURN)