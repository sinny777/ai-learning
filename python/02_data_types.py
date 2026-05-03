# 02_data_types.py
# ----------------------------------------------------
# Exploring basic data types in Python.
# ----------------------------------------------------

# 1. Numbers (Integers and Floats)
x = 10          # Integer
y = 3.14        # Float
print(f"x: {x}, Type: {type(x)}")
print(f"y: {y}, Type: {type(y)}")

# Basic Math
addition = x + 5
multiplication = x * 2
print(f"x + 5 = {addition}")
print(f"x * 2 = {multiplication}")

print("\n--- Lists ---")
# 2. Lists (Ordered, mutable collections of items)
fruits = ["apple", "banana", "cherry"]
print(f"Fruits list: {fruits}")
print(f"First fruit: {fruits[0]}")  # Indexing starts at 0

# Adding an item to a list
fruits.append("orange")
print(f"After adding orange: {fruits}")

print("\n--- Dictionaries ---")
# 3. Dictionaries (Key-Value pairs)
person = {
    "name": "Bob",
    "age": 30,
    "city": "New York"
}
print(f"Person Dictionary: {person}")
print(f"Person's name: {person['name']}")

# Adding a new key-value pair
person["occupation"] = "Engineer"
print(f"Updated Person: {person}")
