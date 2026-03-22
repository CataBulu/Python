import pytesseract
from PIL import Image

# 1. Încărcăm imaginea (înlocuiește 'certificat.png' cu numele fișierului tău)
imagine = Image.open('imagine_89c43e.png')

# 2. Îi spunem lui Python să caute text în ea
# Putem adăuga limba română ('ron') sau germană ('deu') dacă le avem instalate
text_extras = pytesseract.image_to_string(imagine, lang='deu+ron')

print("--- Textul detectat în imagine ---")
print(text_extras)

# 3. Căutăm ceva specific, de exemplu numele tău
if "Bulugea" in text_extras:
    print("\n✅ Confirmat: Acesta este certificatul lui Cătălin!")