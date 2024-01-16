"""
Problem: Login System
Details:
    Write a program that asks the user for a username and password. If the username is "admin" and the password is "TheMaster", then display "Welcome!". If the username is blank, display "Canceled", and if the username is anything else, display "I don't know you."
Extras:
    * If the password is wrong, make it say "Wrong password"
    * If the password is blank, make it say "Canceled"
"""

print("-----Login System-----")
username = input("Enter username: ")
if username == "Admin":
    password = input("Enter password: ")
    if password == "TheMaster":
        print("Welcome!")
    elif password == "" or not password:
        print("Canceled")
    else:
        print("Wrong password")
elif username == "":
    print("Canceled")
else:
    print("I don't know you.")