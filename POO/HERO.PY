class Erou:
    def __init__(self, nume, viata, energie):
        self.nume = nume
        self.viata = viata
        self.energie = energie

    def stare_erou(self):
        
        print(f"Eroul {self.nume} are {self.viata} HP și {self.energie} Energie.")

    def ataca(self):
        
        if self.energie >= 10:
            self.energie -= 10
            print(f"{self.nume} a atacat! Energie rămasă: {self.energie}")
        else:
            print(f"{self.nume} este prea obosit ca să mai atace!")

    def bea_potiune(self):
        
        if self.viata + 20 <= 100:
            self.viata += 20
        else:
            self.viata = 100
        print(f"{self.nume} a băut o poțiune. HP actual: {self.viata}")

    def foloseste_semn(self):
        if self.energie >= 30:
            print("Geralt a folosit Igni!")
            print(f"{self.nume} are {self.energie} energie")
            self.energie -= 30
        else:
            print("Energie insuficientă pentru semne!")
    def mediatie(self):
        if self.energie+50 <100 :
            self.energie += 50
            print(f"{self.nume} are {self.energie} energie") 
        else: 
            self.energie = 100
            print(f"{self.nume} are {self.energie} energie")
hero = Erou("Geralt", 90, 15)

hero.stare_erou()   
hero.ataca()        
hero.ataca()        
hero.bea_potiune()  
hero.stare_erou()
hero.foloseste_semn()
hero.mediatie()  
hero.foloseste_semn()