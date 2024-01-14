# single line comment in python
''' multi line comment in python '''
""" multi line comment in python """
# Path: Python/class1.py

# printing on console
print ("----- Let's Calculate Speed -----")
print ("Enter Distance: ")

# taking distance as input from user
distance = input()

# input is always in string format so converting string to integer
distance = int(distance)

# Taking time as input from user
time = int(input("Enter time: "))

# calculating speed
speed = distance / time

# printing speed
print ("Speed is: ", speed)





# Checking the type of variable
print() # for new line
print ("Data type of Distance: ",type(distance))
print()

# Class 1 Exercise
print("----- Let's Calculate Mass by using F = ma -----")
f = int(input("Enter force: "))
a = int(input("Enter acceleration: "))
m = f/a
print("Mass is: ", m)

print()
print("----- Let's Calculate Mass by using w = mg -----")
w = int(input("Enter Weight: "))
g = w/9.8
print("Mass is: ", g)

print()
print("----- Let's Convert USD -> PKR -----")
usd = int(input("Enter USD: "))
pkr = usd * 300
print("PKR is: ", pkr)