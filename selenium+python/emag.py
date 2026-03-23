from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

class DemoFindElementByid:
    def locate_by_id_demo(self):
        driver.maximize_window()
        driver.get("https://www.emag.ro/")
        time.sleep(5)
        try:
            # Folosim un XPath mai deștept: "găsește orice buton care CONȚINE cuvântul Accept" asta e singura de nu am facut-o eu
            buton_cookies = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
            buton_cookies.click()
            driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
            print("Succes: Am dat click pe Accept Cookies!")
            time.sleep(3)
            driver.find_element(By.XPATH, "//button[@aria-label='Închide notificarea de login']//i[@class='em em-close']").click()
            print("Info: Succes: Am dat click pe butonul x de dupa cookies ")
            time.sleep(3)            
        except Exception:
             print("Info: Bannerul de cookies nu a apărut sau textul e diferit.")
        driver.find_element(By.XPATH, "//input[@id='searchboxTrigger']").send_keys('caine')
        driver.find_element(By.XPATH, "//i[@class='em em-search']").click()
        print("Am dat search la obiectele cerute")
        
        for i in range(1, 4):
            
            time.sleep(3)
            driver.find_element(By.XPATH, f"(//button[@type='submit'][normalize-space()='Adauga in Cos'])[{i}]").click()
            time.sleep(3)
            driver.find_element(By.XPATH, "(//i[@class='em em-close d-none d-sm-block gtm_6046yfqs'])[1]").click()
            print(f"Am adăugat cu succes produsul numărul {i} în coș!")
    
    
        
test = DemoFindElementByid()
test.locate_by_id_demo()
driver.find_element(By.XPATH, "//span[contains(text(),'Coșul meu')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "(//a[@class='btn btn-emag btn-primary fs-16 btn-block btn-lg gtm_sn11312018'])[1]").click()

print("Felicitari! Scriptul a avut succes!")
time.sleep(10)