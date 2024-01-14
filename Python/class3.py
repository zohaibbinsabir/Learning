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
