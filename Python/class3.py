"""
->  There are two types of loops in Python, for and while.

->  The "for" loop
    For loops iterate over a given sequence. Here is an example:
        fruits = ["apple", "banana", "cherry"]
        for x in fruits:
            print(x)

->  The "while" loop
    With the while loop we can execute a set of statements as long as a condition is true.
        i = 1
        while i < 6:
            print(i)
            i += 1

->  The break Statement
    With the break statement we can stop the loop even if the while condition is true:
        i = 1
        while i < 6:
            print(i)
            if i == 3:
                break
            i += 1

->  The continue Statement
    With the continue statement we can stop the current iteration, and continue with the next:
        i = 0
        while i < 6:
            i += 1
            if i == 3:
                continue
            print(i)

->  The else Statement
    With the else statement we can run a block of code once when the condition no longer is true:
        i = 1
        while i < 6:
            print(i)
            i += 1
        else:
            print("i is no longer less than 6")
"""



# Class 3 Exercise
print("----- Result Calulation -----")
english = int(input("Enter marks in English: "))
math = int(input("Enter marks in Math: "))  
Chemistry = int(input("Enter marks in Chemistry: "))
socialScience = int(input("Enter marks in Social Science: "))   
biology = int(input("Enter marks in Biology: "))

# Percentage Calculation
percentage = (english + math + Chemistry + socialScience + biology)/5

# Grading system
def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

print("----- Result -----")
print("Student Name: ", input("Enter student name: "))
print("Total marks: ", english + math + Chemistry + socialScience + biology)
print("Percentage: ", percentage)
print("Grade: ", grade(percentage))



print()
print("-----Login System-----")
username = input("Enter username: ")
if username == "Admin":
    password = input("Enter password: ")
    if password == "TheMaster":
        print("Welcome!")
    elif password == "":
        print("Canceled")
    else:
        print("Wrong password")
elif username == "":
    print("Canceled")
else:
    print("I don't know you.")


print()
print("----- Running Total of 5 numbers -----")
total = 0
for i in range(1,5,1):
    total += int(input("Enter number: "))
print("Total: ", total)

print()
print("----- Sum of numbers until user enters -1 -----")
sum = 0
while True:
    num = int(input("Enter number: "))
    if num == -1:
        break
    sum += num
print("Sum: ", sum)

print()
print("----- print name with hello until user enters END -----")
while True:
    name = input("Enter name: ")
    if name == "END":
        print("END")
        break
    print("Hello ", name + "!")