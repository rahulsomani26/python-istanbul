"""
Regular Expressions / re / regex 
used to search for specific things 
step1. import re 
"""
import re

'''
     create a msg string ( multi-line strings )  
     make a pattern ( to be searched )
     Than search using methods provided by the re module 

    Some methods / functions 

    To create a pattern ---> re.compile() , we can also create a pattern manually

'''
msg = 'Hi my name is Rahul and my Phone number is 8210638822'
# if '8210638822' in msg:
#     print('Found')
# else:
#     print('not found ')


# Manually creating a pattern
# pattern = '8210638822'
# result = re.search(pattern, msg)
# print(result)
# print(result.group())


# Creating a pattern using the compile()

# pattern = re.compile('8210638822')
# print(pattern)
# result = re.search(pattern, msg)
# print(result.group())


'''
    What is so special about Regular Expressions
    In re, we can customize our search 

'''


msg = """
        Hi my name is Rahul.
        My Phone number is 82rahul
        My mail id is  abc123@gmail.com
        and my friends number is 

    """


# pattern = re.compile(r'\d\d\d\d\d\d\d\d\d\d')  # \d -- digit
# pattern = re.compile(r'\d.')  # . will match a single character
# result = re.search(pattern, msg)
# print(result)
# print(result.group())


# searching for Alphabets

# pattern = re.compile(r'\w.')  # \w Alphabet
# result = re.search(pattern, 'rahul somani a trainer')
# print(result)
# print(result.group())


# search for email id


# pattern = re.compile(r'\w..@\w\w\w\w\w.\w\w\w')
# pattern = re.compile(r'\w+@\w+.\w+')
# result = re.search(pattern, msg)
# print(result.group())


# Find for  abc123@gmail.com

# pattern = re.compile(r'\w+\d+@\w+.\w+')
# result = re.search(pattern, msg)
# print(result)
# print(result.group())


'''
   Using character class
'''


# pattern = re.compile(r'[0-9]')  # equivalent to \d , search for a single digit
# result = re.search(pattern, 'Hi My number is 812')
# print(result.group())


# equivalent to \d , search for a single digit
pattern = re.compile(r'[a-zA-Z0-9]+')
result = re.search(pattern, 'Hi8989 My number is 812')
print(result.group())
