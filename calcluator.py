# Editting code here
# Program goal: Build a simple program that can add, subtract, multiply, and divide 2 numbers.

# Functional Decomposition: 
# 1. Obtain a way to grab 2 numbers
# 2. Obtain a way to choose either add, subtract, multiply, or divide
# 3. Do the wanted calculation with the given 2 numbers
# 4. Output the calculation/result

print("Welcome to my python calculator app!")

# Create a way to grab 2 numbers
num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))

# Asking to choose add/subtract/multiply/divide
choice = input("Choose either : add, subtract, multiply, or divide: ")

# Completing the chosen option
if choice == "add":
    print (num1 + num2)
elif choice == "subtract": 
    print (num1 - num2)
elif choice == "multiply": 
    print (num1 * num2)
elif choice == "divide":
    print (num1 / num2)
    
# output with print ()
# Inject a variable using curly brackets: {}