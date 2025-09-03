class Arithmetic:
    def add(self):
        print("Addition:", self.a + self.b)

    def subtract(self):
        print("Subtraction:", self.a - self.b)

    def multiply(self):
        print("Multiplication:", self.a * self.b)

    def divide(self):
        print("Division:", self.a / self.b)


# Create object and assign values manually
obj1 = Arithmetic()
obj1.a = 10
obj1.b = 5

obj1.add()
obj1.subtract()
obj1.multiply()
obj1.divide()

# Add extra attributes
obj1.model_num = "M123"
obj1.made_in = "India"

obj2 = Arithmetic()
obj2.a = 20
obj2.b = 4
obj2.color = "Blue"
obj2.discount = "30%"

# Print attributes
print("Object 1")
print("Model Number:", obj1.model_num)
print("Made In:", obj1.made_in)

print("Object 2")
print("Color:", obj2.color)
print("Discount:", obj2.discount)

#self:it refer to present object
#dyanamic nature
class Example:
    def set_values(self, x, y):
        self.a = x
        self.b = y


# Create object
obj1 = Example()

# Set values
obj1.set_values(10, 20)

# Print directly
print("a =", obj1.a)
print("b =", obj1.b)
