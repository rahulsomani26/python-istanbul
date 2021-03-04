"""
  Some methods in regular expressions
"""
import re
msg = '''
        Hello I live in california U.S 
        and my number is 8210638822
        and yours is 98343984
    '''

# pattern = re.compile(r'\D+')  # \D will search for anything except numbers
# preceding a character class with ^ will complement the character class
# pattern = re.compile(r'[^0-9]+')
# result = re.search(pattern, msg)
# print(result.group())

# search for space
# pattern = re.compile(r'\s')
# result = re.search(pattern, msg)
# print(result.group())


pattern = re.compile(r'\d+')
result = re.findall(pattern, msg)
# print(result)
for num in result:
    print(f' Your number is {num}')
