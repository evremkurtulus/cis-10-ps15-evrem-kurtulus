class Employee:

  def init(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay

  def bonus(self,bonuspay):
    b = float(bonuspay) * class Car:

  def init(self, make, model, stickerprice, discount):
    self.make = make
    self.model = model
    self.stickerprice = stickerprice
    self.discount = discount

  def SW(self, SportWheels):
    b = float(SportWheels) * float(self.stickerprice)
    return b

  def SE(self, Sportengine):
    b = float(SportEngine) * float(self.stickerprice)
    return b 

  def SI(self, SportInterior):
    b = float(SportInterior) * float(self.stickerprice)
    return b

class Sport(Car):
  def options(self,option):
    b = float(option) * float(self.stickerprice)
    return b

car1 = Car('Dodge', 'Charger',50000.00)
sport1 = Sport('Dodge' ,'Charger Hellcat',70000.00)
upgrades = input("Enter Options : ")
SportWheels = 1000.00
SportEngine = 3000.00
SportInterior = 2000.00
print(car1.make)
print(car1.model)
print(car1.stickerprice)
print(sport1.upgrades(options))