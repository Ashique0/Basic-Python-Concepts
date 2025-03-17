# Task 1: Basic Mathematical Operations

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing the basic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
# Handling division by zero error
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

# Displaying the results
print(f"\nResults of operations on {num1} and {num2}:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
