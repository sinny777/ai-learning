# 03_control_flow.py
# ----------------------------------------------------
# Learning how to control the flow of a program 
# using conditions and loops.
# ----------------------------------------------------

print("--- If/Else Statements ---")
# 1. If/Elif/Else
temperature = 25

if temperature > 30:
    print("It's a hot day! Drink water.")
elif temperature > 20:
    print("It's a nice day.")
else:
    print("It's cold. Wear a jacket.")


print("\n--- For Loops ---")
# 2. For Loops (Iterating over a sequence)
# Iterating over a list
colors = ["red", "green", "blue"]
for color in colors:
    print(f"Color: {color}")

# Iterating over a range of numbers
# range(5) generates numbers from 0 to 4
for i in range(5):
    print(f"Number: {i}")


print("\n--- While Loops ---")
# 3. While Loops (Executes as long as a condition is true)
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1  # Decrement count by 1
print("Go!")
