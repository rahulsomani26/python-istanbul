'''
     Input a string with some messages
     we have split that string based on a pattern 

    Regular expressions 
'''

import re
msg = """Tell me something about yourself,
        your background, your family, your country 
        """

text_to_search = 'does What of means to you'


# pattern = re.compile(r'\s')
# result = re.split(pattern, text_to_search)
# print(result)
# number_of_occurence_of = result.count('of')
# print(number_of_occurence_of)

text_to_search_intermediate = 'does What of means to you of generally is of and '

# Problem 2 is
# step1 Make a pattern
# use the split()
# step3 use the count function on the list


# pattern = re.compile(r'of')
# print(pattern)
# result = re.split(pattern, text_to_search_intermediate)
# print(result)


'''

^  will match something at the beginning of a string/file


'''

# pattern = re.compile(r'^What')
# result = re.search(pattern, text_to_search)
# print(result)
# print(result.group())

# $ will match something at the end of the string


# pattern = re.compile(r'you$')
# result = re.search(pattern, text_to_search)
# print(result)
# print(result.group())


'''

    sub() ---> substitutes 
'''

search_and_substitute = 'Hello my Name is Rahul Somani'
substitute_result = re.sub(r'Name', '&', search_and_substitute)
print(substitute_result)


print('----' * 20)
test_string = 'What a beaautiful world'
pattern = re.compile(r'[bea].')
result = re.search(pattern, test_string)
print(result.group())
print(result.span())
