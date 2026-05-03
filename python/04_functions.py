# 04_functions.py
# ----------------------------------------------------
# Functions are reusable blocks of code.
# ----------------------------------------------------

# 1. Defining a basic function
def greet():
    print("Hello from a function!")

# Calling the function
greet()

# 2. Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")
greet_user("Bob")

# 3. Function with return values
def add_numbers(a, b):
    """This function adds two numbers and returns the result."""
    result = a + b
    return result

sum_result = add_numbers(5, 7)
print(f"The sum of 5 and 7 is: {sum_result}")

# 4. Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print(f"3 squared (default): {power(3)}")
print(f"3 cubed (override default): {power(3, 3)}")
