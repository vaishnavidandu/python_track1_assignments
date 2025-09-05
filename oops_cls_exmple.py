class Student:
    # Class Variable 
    school_name = "Vijaysai High School"

    #  Constructor
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Instance Method 
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

    #  Class Method 
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # Static Method 
    @staticmethod
    def info():
        print("Today topic is OOPS concept")


#  Creating Objects 
s1 = Student("Vaishnavi", 21)
s2 = Student("Pavani", 22)

# Accessing instance methods
print("Student 1 ")
s1.show_details()
print("School:", s1.school_name)

print("Student 2 ")
s2.show_details()
print("School:", s2.school_name)

# Calling static method
print("Static Method Output")
Student.info()

# Changing class variable using class method
print("After Changing School Name")
Student.change_school("Matrusri High School")

print("Student 1 School:", s1.school_name)
print("Student 2 School:", s2.school_name)

#output
# Student 1 
# Name: Vaishnavi
# Age: 21
# School: Vijaysai High School
# Student 2
# Name: Pavani
# Age: 22
# School: Vijaysai High School
# Static Method Output
# Today topic is OOPS concept
# After Changing School Name
# Student 1 School: Matrusri High School
# Student 2 School: Matrusri High School