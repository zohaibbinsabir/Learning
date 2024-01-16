"""
How to declare arrays:
    numbers = [1, 2, 3, 4, 5]

Negative Indexing:
    numbers = [1, 2, 3, 4, 5]
    print(numbers[-1]) # 5
    print(numbers[-2]) # 4

Slicing:
    numbers = [1, 2, 3, 4, 5]
    print(numbers[1:3]) # [2, 3]
    print(numbers[:3]) # [1, 2, 3]
    print(numbers[1:]) # [2, 3, 4, 5]
    print(numbers[:]) # [1, 2, 3, 4, 5]

Merge Arrays:
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]
    numbers = numbers1 + numbers2 # [1, 2, 3, 4, 5, 6]
    numbers3 = numbers1 + [7, 8, 9] # [1, 2, 3, 7, 8, 9]

    number2.extend([7, 8, 9]) # [4, 5, 6, 7, 8, 9]

Difference between append and extend:
    numbers = [1, 2, 3]
    numbers.append([4, 5, 6]) # [1, 2, 3, [4, 5, 6]]
    numbers.extend([4, 5, 6]) # [1, 2, 3, 4, 5, 6]

Difference betweeen mutable and immutable Arrays:
    mutable = changeable
    immutable = unchangeable
    strings are immutable arrays

Delete from array:
    numbers = [1, 2, 3, 4, 5]
    del numbers[0] # [2, 3, 4, 5]
    del numbers[1:3] # [1, 4, 5]
    del numbers # deletes the whole array

Convert string to array:
    string = "Hello"
    array = list(string) # ['H', 'e', 'l', 'l', 'o']
    "Master World".split() # ['Master', 'World']
    "Master,World".split(",") # ['Master', 'World']

Lists Aliasing vs Cloning:
    Aliasing:
        numbers1 = [1, 2, 3]
        numbers2 = numbers1
        numbers2[0] = 10
        print(numbers1) # [10, 2, 3]
        print(numbers2) # [10, 2, 3]
    Cloning:
        numbers1 = [1, 2, 3]
        numbers2 = numbers1[:] # or numbers2 = numbers1.copy()
        numbers2[0] = 10
        print(numbers1) # [1, 2, 3]
        print(numbers2) # [10, 2, 3]

List comprehension:
    numbers = [1, 2, 3, 4, 5]
    numbers = [x * 2 for x in numbers] # [2, 4, 6, 8, 10]
    numbers = [x * 2 for x in numbers if x % 2 == 0] # [4, 8]

combine list elements with comprehension:
    combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

python dictionaries:
    for example:
        student = {
            "name": "Ahmed",
            "age": 18,
            "gpa": 3.5
        }
    to access:
        print(student["name"]) # Ahmed
    to add:
        student["year"] = 2019
    to delete:
        del student["year"]
    to check if key exists:
        if "name" in student:
            print("name exists")
    to get length:
        print(len(student)) # 3
    to get keys:
        print(student.keys()) # dict_keys(['name', 'age', 'gpa'])
    to get values:
        print(student.values()) # dict_values(['Ahmed', 18, 3.5])
    to get items:
        print(student.items()) # dict_items([('name', 'Ahmed'), ('age', 18), ('gpa', 3.5)])
    to loop through keys:
        for key in student:
            print(key)
    to loop through values:
        for value in student.values():
            print(value)    
    to check if exists:
        if "name" in student:
            print("name exists")
"""