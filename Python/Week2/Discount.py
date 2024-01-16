print("----- Discount on total purchase amount -----")
total = float(input("Enter total amount: "))
day = input("Enter day: ")
def discount(total, day):
    if day == "Sunday" or day == "sunday":
        return total * 10 / 100
    elif day == "Monday" or day == "monday":
        return total * 8 / 100
    elif day == "Tuesday" or day == "tuesday":
        return total * 5 / 100
    return 0

print("Total amount after discount: ", total - discount(total, day))