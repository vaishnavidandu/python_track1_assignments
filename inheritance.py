# 1. Single Inheritance
class Vehicle:
    def fuel(self):
        print("All vehicles need fuel")

class Car(Vehicle):   # Single Inheritance
    def wheels(self):
        print("Car has 4 wheels")


# 2. Multiple Inheritance
class Electric:
    def battery(self):
        print("Runs on battery")

class Petrol:
    def petrol_engine(self):
        print("Runs on petrol")

class HybridCar(Electric, Petrol):  # Multiple Inheritance
    def type(self):
        print("Hybrid car can use both petrol and battery")


# 3. Multilevel Inheritance
class VehicleBase:
    def move(self):
        print("Vehicles can move")

class Bus(VehicleBase):
    def passengers(self):
        print("Bus carries many passengers")

class SchoolBus(Bus):   # Multilevel Inheritance
    def color(self):
        print("School Bus is yellow")


# 4. Hierarchical Inheritance
class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")

class Truck(Vehicle):
    def wheels(self):
        print("Truck has 6 wheels")


# 5. Hybrid Inheritance 
class A:
    def feature1(self):
        print("Basic Vehicle Features")

class B(A):
    def feature2(self):
        print("Four Wheeler Features")

class C(A):
    def feature3(self):
        print("Heavy Vehicle Features")

class D(B, C):   # Hybrid Inheritance
    def feature4(self):
        print("Advanced Truck Features")

print("Single Inheritance")
c = Car()
c.fuel()
c.wheels()

print("Multiple Inheritance")
h = HybridCar()
h.battery()
h.petrol_engine()
h.type()

print("Multilevel Inheritance")
sb = SchoolBus()
sb.move()
sb.passengers()
sb.color()

print("Hierarchical Inheritance")
b = Bike()
b.fuel()
b.wheels()

t = Truck()
t.fuel()
t.wheels()

print("Hybrid Inheritance")
d = D()
d.feature1()
d.feature2()
d.feature3()
d.feature4()
# Output
# Single Inheritance
# All vehicles need fuel
# Car has 4 wheels
# Multiple Inheritance 
# Runs on battery
# Runs on petrol
# Hybrid car can use both petrol and battery
# Multilevel Inheritance
# Vehicles can move
# Bus carries many passengers
# School Bus is yellow
# Hierarchical Inheritance
# All vehicles need fuel
# Bike has 2 wheels
# All vehicles need fuel
# Truck has 6 wheels
# Hybrid Inheritance
# Basic Vehicle Features
# Four Wheeler Features
# Heavy Vehicle Features
# Advanced Truck Features