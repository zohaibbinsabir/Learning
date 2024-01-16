"""
Function:
    We use functions to perform a specific task
    We use functions to avoid writing same code again and again
    
    There are 2 types of functions in python
    1.  Built-in Functions
    2.  User-defined Functions

    1.  Built-in Functions
        ->  These functions are already defined in python
        ->  We can use these functions directly
        ->  for example:    print()
                            input()
                            int()
                            float()
                            str()
                            len()
                            type()
                            etc.

    2.  User-defined Functions
        ->  These functions are defined by user
        ->  We can use these functions after defining them
        ->  for example:    def function_name():
                                print("Hello World")
                            function_name()

    Syntax of function:
        def function_name():
            print("Hello World")
        function_name()

    Syntax of function with parameters:
        def function_name(parameter1, parameter2):
            print("Hello World" + parameter1 + parameter2)
        function_name(argument1, argument2)

    Syntax of function with return statement:
        def function_name(parameter1, parameter2):
            return parameter1 + parameter2
        function_name(argument1, argument2)

"""










""""
To make decisions, we use the if statement in Python.
The if statement is written by using the if keyword.
Syntax:
    if condition:
        statement
    else:
        statement

    if condition:
        statement
    elif condition:
        statement
    else:
        statement

Nested if statements:
When we use if condition inside another if condition, it is called nested if statement.
    if condition:
        if condition:
            statement
        else:
            statement
    else:
        statement

    if condition:
        statement
    else:
        if condition:
            statement
        else:
            statement
"""