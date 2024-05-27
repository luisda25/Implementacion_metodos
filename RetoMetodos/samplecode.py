import math
# False, True, None
a = False
b = True
c = None

# and, or, not
if a and not b or c:
    pass

# as, with
with open('example.txt', 'w') as f:
   f.write('Hello, world!')

# assert
assert b == True

# async, await
async def async_function():
    return 42

# break, continue
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)

# class, def
class MyClass:
    def __init__(self, value):
        self.value = value

    def method(self):
        return self.value

# del
x = [1, 2, 3]
del x[1]

# elif, else, if
if a:
    pass
elif b:
    pass
else:
    pass

# except, raise, try
try:
    raise ValueError("An example exception")
except ValueError as e:
    print(e)

# finally
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This always executes")

# for, in
for item in [1, 2, 3]:
    print(item)

# from, import
from math import pi

# global, nonlocal
global_var = 0

def outer():
    nonlocal_var = 1

    def inner():
        nonlocal nonlocal_var
        global global_var
        nonlocal_var += 1
        global_var += 1

    inner()
    print(nonlocal_var)

outer()
print(global_var)

#is
if a is b:
    pass

#lambda
square = lambda x: x * x

#pass
def empty_function():
    pass

#return
def func():
    return

#yield
def generator():
    yield 1

#while
counter = 0
while counter < 5:
    counter += 1

#Match-case statement
point = (3, 4)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"X={x}")
    case (0, y):
        print(f"Y={y}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        print("Not a point")

#Asynchronous function call
async def main():
    result = await async_function()
    print(result)

#Running the async main function
import asyncio
asyncio.run(main())