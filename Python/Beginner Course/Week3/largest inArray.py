arr = []
for i in range (0,5,1):
    arr.append(int(input("Enter Number " + str(i+1) + ": ")))
print("Largest number is: ", max(arr))