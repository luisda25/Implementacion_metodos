#PYTHONFILE3.PY

import math

# This is a sample Python code with 20 lines

# Variable declaration
name = "John"
age = 25

# Conditional statement
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Looping statement
for i in range(5):
    print(i)

# Function definition
def greet(name):
    print("Hello, " + name)

# Function call
greet(name)

# List declaration
fruits = ["apple", "banana", "orange"]

# List iteration
for fruit in fruits:
    print(fruit)

# Dictionary declaration
person = {"name": "John", "age": 25}

# Dictionary access
print(person["name"])

# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Class definition
class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Driving the", self.brand, "car")

# Class instantiation
my_car = Car("Toyota")

# Method call
my_car.drive()

# Import statement

# Math operation
result = math.sqrt(16)

# Print result
print("Square root of 16 is", result)