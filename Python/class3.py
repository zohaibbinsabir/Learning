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


"""
->  Arrays in python are called lists.
->  Lists are used to store multiple items in a single variable.
->  Lists are created using square brackets.
->  Lists are ordered, changeable and allow duplicate values.
->  List items are indexed, the first item has index [0], the second item has index [1] etc.
->  List items are ordered, changeable, and allow duplicate values.

->  List Length
    To determine how many items a list has, use the len() function:
        thislist = ["apple", "banana", "cherry"]
        print(len(thislist))

->  List Items - Data Types
    List items can be of any data type:
        String, int and boolean data types:
            list1 = ["apple", "banana", "cherry"]
            list2 = [1, 5, 7, 9, 3]
            list3 = [True, False, False]

    A list can contain different data types:
    for example, the following list contains an integer, a float, a complex number, and a string.
    list = ["apple", "banana", "cherry", 1, 5, 7, 9, 3, 3+5j]

->  type()
    From Python's perspective, lists are defined as objects with the data type 'list':
        <class 'list'>
    
->  what is list()?
    The list() constructor returns a list in Python.
        thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
        print(thislist)

->  Access Items
    List items are indexed and you can access them by referring to the index number:
        thislist = ["apple", "banana", "cherry"]
        print(thislist[1])

->  Negative Indexing
    Negative indexing means start from the end.
    -1 refers to the last item, -2 refers to the second last item etc.
        thislist = ["apple", "banana", "cherry"]
        print(thislist[-1])

->  Range of Indexes
    You can specify a range of indexes by specifying where to start and where to end the range.
    When specifying a range, the return value will be a new list with the specified items.
        thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
        print(thislist[2:5])

->  Range of Negative Indexes
    Specify negative indexes if you want to start the search from the end of the list:
        thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
        print(thislist[-4:-1])

->  Change Item Value
    To change the value of a specific item, refer to the index number:
        thislist = ["apple", "banana", "cherry"]
        thislist[1] = "blackcurrant"
        print(thislist)

->  Loop Through a List
    You can loop through the list items by using a for loop:
        thislist = ["apple", "banana", "cherry"]
        for x in thislist:
            print(x)

->  Check if Item Exists
    To determine if a specified item is present in a list use the in keyword:
        thislist = ["apple", "banana", "cherry"]
        if "apple" in thislist:
            print("Yes, 'apple' is in the fruits list")

->  List Length
    To determine how many items a list has, use the len() function:
        thislist = ["apple", "banana", "cherry"]
        print(len(thislist))

->  Add Items
    To add an item to the end of the list, use the append() method:
        thislist = ["apple", "banana", "cherry"]
        thislist.append("orange")
        print(thislist)

->  To add an item at the specified index, use the insert() method:
        thislist = ["apple", "banana", "cherry"]
        thislist.insert(1, "orange")
        print(thislist)

->  Remove Item
    There are several methods to remove items from a list:
        The remove() method removes the specified item:
            thislist = ["apple", "banana", "cherry"]
            thislist.remove("banana")
            print(thislist)

        The pop() method removes the specified index, (or the last item if index is not specified):
            thislist = ["apple", "banana", "cherry"]
            thislist.pop()
            print(thislist)

        The del keyword removes the specified index:
            thislist = ["apple", "banana", "cherry"]
            del thislist[0]
            print(thislist)

        The del keyword can also delete the list completely:
            thislist = ["apple", "banana", "cherry"]
            del thislist

        The clear() method empties the list:
            thislist = ["apple", "banana", "cherry"]
            thislist.clear()
            print(thislist)

->  Copy a List
    You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1
    changes made in list1 will automatically also be made in list2.

    There are ways to make a copy, one way is to use the built-in List method copy().
        thislist = ["apple", "banana", "cherry"]
        mylist = thislist.copy()
        print(mylist)

    Another way to make a copy is to use the built-in method list().
        thislist = ["apple", "banana", "cherry"]
        mylist = list(thislist)
        print(mylist)

->  Join Two Lists
    There are several ways to join, or concatenate, two or more lists in Python.
    One of the easiest ways are by using the + operator.
        list1 = ["a", "b" , "c"]
        list2 = [1, 2, 3]
        list3 = list1 + list2
        print(list3)

    Another way to join two lists are by appending all the items from list2 into list1, one by one:
        list1 = ["a", "b" , "c"]
        list2 = [1, 2, 3]
        for x in list2:
            list1.append(x)
        print(list1)

    Or you can use the extend() method, which purpose is to add elements from one list to another list:
        list1 = ["a", "b" , "c"]
        list2 = [1, 2, 3]
        list1.extend(list2)
        print(list1)

->  The list() Constructor
    It is also possible to use the list() constructor to make a new list.
        thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
        print(thislist)

->  List Methods
    Python has a set of built-in methods that you can use on lists.
    Method	Description
        append()	Adds an element at the end of the list
        clear()	Removes all the elements from the list
        copy()	Returns a copy of the list
        count()	Returns the number of elements with the specified value
        extend()	Add the elements of a list (or any iterable), to the end of the current list
        index()	Returns the index of the first element with the specified value
        insert()	Adds an element at the specified position
        pop()	Removes the element at the specified position
        remove()	Removes the item with the specified value
        reverse()	Reverses the order of the list
        sort()	Sorts the list

->  List Comprehension
    List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
    Example:
        Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
        Without list comprehension you will have to write a for statement with a conditional test inside:
            fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
            newlist = []

            for x in fruits:
                if "a" in x:
                    newlist.append(x)

            print(newlist)

    With list comprehension you can do all that with only one line of code:
        fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

        newlist = [x for x in fruits if "a" in x]

        print(newlist)

    The Syntax
        newlist = [expression for item in iterable if condition == True]

    The return value is a new list, leaving the old list unchanged.
    Condition:
        The condition is like a filter that only accepts the items that valuate to True.
        Example:
            Only accept items that are not "apple":
                newlist = [x for x in fruits if x != "apple"]

            The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

    The condition if num % 2 == 0  will only accept even numbers.
        newlist = [x for x in range(10) if x % 2 == 0]

        print(newlist)

    Expression:
        The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
            Set the values in the new list to upper case:
                newlist = [x.upper() for x in fruits]

                print(newlist)

            Set all values in the new list to 'hello':
                newlist = ['hello' for x in fruits]

                print(newlist)

            Return "orange" instead of "banana":
                newlist = [x if x != "banana" else "orange" for x in fruits]

                print(newlist)

    Iterable:
        The iterable can be any iterable object, like a list, tuple, set etc.
        Example:
            You can use the range() function to create an iterable:
                newlist = [x for x in range(10)]

                print(newlist)

            Same example, but with a condition:
                newlist = [x for x in range(10) if x < 5]

                print(newlist)

            Accept only numbers lower than 5:
                newlist = [x for x in range(10) if x < 5]

                print(newlist)

            Set the values in the new list to upper case:
                newlist = [x.upper() for x in fruits]

                print(newlist)

            Set all values in the new list to 'hello':
                newlist = ['hello' for x in fruits]

                print(newlist)

            Return "orange" instead of "banana":
                newlist = [x if x != "banana" else "orange" for x in fruits]

                print(newlist)

->  Sort List Alphanumerically
    List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
        cars = ['Ford', 'BMW', 'Volvo']

        cars.sort()

        print(cars)

->  Sort Descending
    To sort descending, use the keyword argument reverse = True:
        cars = ['Ford', 'BMW', 'Volvo']

        cars.sort(reverse = True)

        print(cars)

->  Customize Sort Function
    You can also customize your own function by using the keyword argument key = function.
    The function will return a number that will be used to sort the list (the lowest number first):
        def myFunc(e):
            return len(e)

        cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

        cars.sort(key=myFunc)

        print(cars)

->  Case Insensitive Sort
    By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
        thislist = ["banana", "Orange", "Kiwi", "cherry"]

        thislist.sort()

        print(thislist)

    Luckily we can use built-in functions as key functions when sorting a list.
    So if we want a case-insensitive sort function, use str.lower as a key function:
        thislist = ["banana", "Orange", "Kiwi", "cherry"]

        thislist.sort(key = str.lower)

        print(thislist)

->  Reverse Order
    What if you want to reverse the order of a list, regardless of the alphabet?
    The reverse() method reverses the current sorting order of the elements.
        thislist = ["banana", "Orange", "Kiwi", "cherry"]

        thislist.reverse()

        print(thislist)

"""


"""
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