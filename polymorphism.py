#method overloading
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return str(self.amount)

m1 = Money(100)
m2 = Money(200)
print(m1 + m2)   # 300


#over riding
class Vehicle:
    def speed(self):
        return "Average speed"

class Car(Vehicle):
    def speed(self):
        return "Car speed: 120 km/h"

class Bike(Vehicle):
    def speed(self):
        return "Bike speed: 80 km/h"

vehicles = [Car(), Bike(), Vehicle()]
for v in vehicles:
    print(v.speed())

#Car speed: 120 km/h
# Bike speed: 80 km/h
# Average speed