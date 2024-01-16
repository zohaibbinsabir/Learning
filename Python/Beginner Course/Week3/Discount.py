print("----- Discount -----")
price = int(input("Enter price: "))
day = input("Enter day: ")
month = input("Enter month: ")
def discount(price, day, month):
    if((day == "sunday" or day == "Sunday") and (month == "october" or month == "October" or month == "march" or month == "March" or month == "August" or month == "august")):
        return price * 10 / 100
    elif((day == "monday" or day == "Monday") and (month == "november" or month == "November" or month == "december" or month == "December")):
        return price * 5 / 100
    return 0
    
print("Price after discount: ", price - discount(price, day, month))