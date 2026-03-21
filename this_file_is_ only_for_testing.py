class Car: 
  def startUp(self): 
    print("Press brake") 
     
  def turn_on_ac(self): 
    print("AC on") 
 
class Manual(Car): 
  def start_up(self): 
    print("Press clutch") 
 
car = Manual()
 
car.turn_on_ac() 
car.start_up()