from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Importăm WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # Importăm Condițiile (EC)
import time

class DemoFindElementByid:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.emag.ro/")
        
        # DEFINIM SENZORUL: Așteaptă maxim 10 secunde pentru orice acțiune
        wait = WebDriverWait(driver, 10)

        # BLOCUL DE BANNERE (Cookies + Login)
        try:
            # wait.until(EC.element_to_be_clickable(...)) înlocuiește time.sleep() + find_element()
            buton_cookies = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]")))
            buton_cookies.click()
            print("Succes: Am dat click pe Accept Cookies!")
            
            # Așteptăm "X"-ul de la fereastra de login și dăm click
            buton_x_login = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Închide notificarea de login']//i[@class='em em-close']")))
            buton_x_login.click()
            print("Info: Succes: Am dat click pe butonul X de dupa cookies")
        except Exception:
            print("Info: Bannerele nu au apărut sau au fost deja închise.")

        # CĂUTAREA
        # Așteptăm ca bara de căutare să fie interacționabilă
        bara_cautare = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='searchboxTrigger']")))
        bara_cautare.send_keys('casti wireless')
        
        driver.find_element(By.XPATH, "//i[@class='em em-search']").click()
        print("Am reusit sa dam search la obiectele cerute")
        
        # BUCLA PENTRU PRODUSE
        for i in range(1, 4):
            # Așteptăm ca butonul "Adaugă în coș" numărul {i} să fie gata de click
            buton_adauga = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//button[@type='submit'][normalize-space()='Adauga in Cos'])[{i}]")))
            buton_adauga.click()
            
            # Așteptăm să apară fereastra de confirmare (am scurtat puțin XPath-ul ca să fie anti-crăpare)
            buton_x_confirmare = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[contains(@class, 'em-close')])[1]")))
            buton_x_confirmare.click()
            
            print(f"Am adăugat cu succes produsul numărul {i} în coș!")

# Rulăm scriptul
test = DemoFindElementByid()
test.locate_by_id_demo()

print("Felicitari! Scriptul a avut succes!")
# Păstrăm un singur sleep la final ca să poți admira tu browserul înainte să se închidă
time.sleep(10)