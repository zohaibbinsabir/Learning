print("----- Result Calulation -----")
name = input("Enter Student Name: ")
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
print("Student Name: ", name)
print("Total marks: ", english + math + Chemistry + socialScience + biology)
print("Percentage: ", percentage)
print("Grade: ", grade(percentage))