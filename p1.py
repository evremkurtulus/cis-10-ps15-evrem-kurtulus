class Employee:

  def init(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay

  def bonus(self,bonuspay):
    b = float(bonuspay) * float(self.pay)
    return b

class Manager(Employee):
  def mbonus(self,mngrbonus):
    b = float(mngrbonus) * float(self.pay)
    return b

empl1 = Employee('Max', 'Payne',50000)
mana1 = Manager('Max', 'Payne',50000)
bonusrate = input("Enter bonus rate: ")
mgrbonus = 0.40
print(empl1.first)
print(empl1.last)
print(empl1.bonus(bonusrate))
print(mana1.mbonus(mgrbonus))