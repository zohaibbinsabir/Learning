# we use functions for repetitive tasks
"""
->  There are two types of functions:
    1. Built-in functions: Built-in functions are already defined in python
        for example: print(), input(), int(), float(), str(), etc.
    2. User-defined functions: User-defined functions are defined by the user

->  Some functions return some value after implementation some didn't

->  Syntax of function:
    def function_name():
        statements
        return

->  def is a keyword
    function_name is the name of function
    () is used for parameters
    : is used for indentation
    return is used to return the value from function

->  Syntax of function call:
    function_name()
"""

print("----- Function to sum two hard coded numbers -----")
def sumNumbers(a, b):
    return a + b

print("Sum of 2 and 3 is: ", sumNumbers(2, 3))
print("Sum of 5 and 6 is: ", sumNumbers(5, 6))
print()

print("----- Function to sum two numbers taken from user -----")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum of ", num1, " and ", num2, " is: ", sumNumbers(num1, num2))

# we use if-else statements for decision making
"""
->  Syntax of if-else statement:
    if condition:
        statements
    elif condition:
        statements
    else:
        statements
"""

print()
print("----- Discount Calculator -----")
def discount(day, total):
    if day == "Sunday" or day == "sunday":
        return total * 0.1 # 10% discount
    elif day == "Monday" or day == "monday":
        return total * 0.08 # 8% discount
    elif day == "Tuesday" or day == "tuesday":
        return total * 0.05 # 5% discount
    else:
        return 0
    
day = input("Enter day: ")
total = int(input("Enter total: "))
print("You've to pay: ", total - discount(day, total))

# Class 2 Exercise
print()
print("----- Check Equal or greater than 50 -----")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if(num1 >= 50 or num2 >= 50 or num3 >= 50):
    print("One of value is too large.")


# program to invite friend to Sindh if he hasn't visited Sindh
print()
print("----- Invite Friend to Sindh -----")
province = input("What is your province: ")
if not (province == "Sindh" or province == "sindh"):
    print("You should come visit Sindh Sometimes.")

