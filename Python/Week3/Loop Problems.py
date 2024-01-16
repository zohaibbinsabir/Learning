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