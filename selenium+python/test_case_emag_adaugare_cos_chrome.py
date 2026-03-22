from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# 1. CONFIGURARE (Adăugăm setări să evităm crash-ul de memorie)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("window-size=1920,1080")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)

try:
    # 2. START
    driver.get("https://www.emag.ro/")
    driver.maximize_window()
    
    # Curățare pop-ups
    driver.execute_script("""
        var c = document.querySelector('.js-reject-all'); if(c) c.click();
        var p = document.querySelector('.gh-tooltip, .popover'); if(p) p.remove();
    """)
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # 3. CĂUTARE + ADĂUGARE (Rămân la fel, funcționau bine)
    search = wait.until(EC.element_to_be_clickable((By.ID, "searchboxTrigger")))
    search.send_keys("iphone 15")
    search.send_keys(Keys.ENTER)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card-v2-wrapper")))
    for i in range(3):
        btns = driver.find_elements(By.CSS_SELECTOR, ".card-v2-atc [type='submit'], .card-v2-wrapper .btn-primary")
        if i < len(btns):
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btns[i])
            time.sleep(1)
            driver.execute_script("arguments[0].click();", btns[i])
            print(f"Produs {i+1} adăugat.")
            time.sleep(2)
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # 4. NAVIGARE LA COȘ
    print("Mergem la coș...")
    driver.get("https://www.emag.ro/cart/products?ref=cart")
    
    # 5. CLICK "CONTINUA" - METODA SUPREMĂ (Navigare forțată)
    # Dacă butonul de click dă crash, înseamnă că eMAG blochează evenimentul de click.
    # Atunci, "imităm" ce ar face butonul: trimitem browserul direct la adresa de checkout.
    
    time.sleep(3) # Lăsăm coșul să se încarce complet
    
    print("Executăm pasul de Checkout...")
    
    # Încercăm întâi click-ul prin JS pur (fără Selenium)
    # Dacă JS-ul nu merge, facem redirect direct la URL-ul de checkout
    driver.execute_script("""
        var btn = document.querySelector('a[href="/cart/checkout"]');
        if (btn) {
            btn.click();
        } else {
            window.location.href = "https://www.emag.ro/cart/checkout";
        }
    """)
    
    print("✓ Ar trebui să fii pe pagina de Login acum.")

except Exception as e:
    print(f"Eroare: {e}")