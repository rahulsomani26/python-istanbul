'''
Function
set of instructions
block of instructions
has a name

The keyword def introduces a function definition. It must be followed by the
function name and the parenthesized list of formal parameters.
The statements that form the body of the function start at the next line, and must be indented.


The first statement of the function body can optionally be a string literal;
this string literal is the function’s documentation string, or docstring.
'''


def myFirstFunction():
    msg = """
       This is a doc string and it will
       just tell us what this function does

    """
    print(" This is the first statement")
    print(msg)
    # (' And this one is the last')

# Rishiprintt are you able to see the screen.


# myFirstFunction()
# print(myFirstFunction())


# def myFunction(num, count):
#     print(" Function with a single parameter")
#     print(' You passed {} and {}'.format(num, count))


# myFunction(201, 20)
# myFunction(300, 20)


# def fun():
#     print(' Inside function')


# fun()

# print(' End of program ')
# print(fun())


# def stringify(myString):
#     if myString.isupper():
#         print(' Upper case')
#     else:
#         print(' Lower case ')


# stringify('RAHUL')

'''
More on defining functions
Functions can be defined with a variable number of arguments
There are 3 forms that can be combined
'''

# 1. Default Argument values

'''
Create a function that can accept two arguments name and age and print its value
'''


def newFun(name, age=50):
    print(name, age)


newFun('rahul', 36)   # rahul ,36
newFun('rahul')   # rahul ,36
newFun('rahul', 60)   # rahul ,36


'''
Write a function calculation()
 such that it can accept two variables and calculate the addition and subtraction of it.
  And also it must return both addition and subtraction in a single return call

'''


def calculation(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    print(add, sub)
    print(' End of the function ')

    return add, sub


# result = calculation(20, 20)
# print(result)


def defaultArgument(count, num=10):
    print(count, num)


# defaultArgument(100)   # 100 , 10
# defaultArgument(20, 30)  # 20 30


# Variable number of arguments


def variableArguments(*args):
    for i in args:
        print(i)


# variableArguments('rahul', 'ali')
# # print('-'*10)
# variableArguments(10)
# print('--'*10)
# variableArguments(1, 2, 3, 4, 5, 6)


'''
Write a function calculation() such that it can accept two variables and calculate the
 addition and subtraction of it. 
And also it must return both addition and subtraction in a single return call
'''

'''
Create a function showEmployee() in such a way that it should accept employee name,
 and it’s salary and display both,
 and if the salary is missing in function call it should show it as 9000
'''


'''
Create a function showEmployee() in such a way that it should accept employee name, 
and it’s salary and display both,
and if the salary is missing in function call it should show it as 9000
'''


'''
  write a function that accepts varible number of args 
  and return the sum of all the args ( assuming that every arg is an int)
'''


def sums(*args):
    s = 0
    for item in args:
        s = s + item
    print(s)


sums(1, 1, 2)
