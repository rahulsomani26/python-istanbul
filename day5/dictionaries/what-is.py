# '''
#   Dictionary is a data structure 
#   It is a sequence of key:value pair
#   Syntax  1 {}  --> Empty dict
#           2. dict()
#   Properties of a dictionary 

#   The key should not change 

    
# '''

# empty_dict = {}
# print(type(empty_dict))
# print(len(empty_dict))


# one_element = {'name':'rahul somani'}
# print(one_element)
# print(len(one_element))
# multiple_element = {'name':'rahul somani','age':40,'address':'Patna, India',30:'Ali'}

# # accessing elements in a dict 
# # accessing elements in a dict 
# # # accessing elements in a dict 
# # print(multiple_element['name'])
# # print(multiple_element['age'])
# # print(multiple_element['address'])
# # print(multiple_element[30])
# print(multiple_element)

# print(multiple_element.get('age'))  # accept a key and return the corresponding value

# # Finding keys in a dict

# print(multiple_element.keys())

# # Adding / Updating  --- using subscript notation[] / update()
# multiple_element['name'] = 'Ali Mohemmad'

# multiple_element.update({'address':'Mumbai'})
# print(multiple_element)


# # getting values in a dict 
# # using values()

# print(multiple_element.values())

# # Getting Items ---- items() method

# print(multiple_element.items())

# if "age" in multiple_element:
#     print('The key is present')
# else:
#     print('The key is not present')


'''
Deleting items 

1. pop()   ---> takes a key as an argument i.e input 
2. popitem()   --> removes the last inserted item
'''

# phoneNumbers = {'rahul':'8210638822', 'Ujjwal':'9867445626','shweta':'8969150666'}

# poppedValue = phoneNumbers.pop('shweta')
# print(poppedValue)
# print(phoneNumbers)

# lastValue = phoneNumbers.popitem()
# print(lastValue)
# print(phoneNumbers)

# phoneNumbers = {'rahul':'8210638822', 'Ujjwal':'9867445626','shweta':'8969150666'}

# del phoneNumbers['rahul']
# del phoneNumbers
# print(phoneNumbers)

phoneNumbers = {'rahul':'8210638822', 'Ujjwal':'9867445626','shweta':'8969150666'}

# phoneNumbers.clear()
# print(phoneNumbers)

# Looping through the dictionary

for i in phoneNumbers:  # we will get the keys 
    print(i)

for i in phoneNumbers:    # we get the value of the key
    print(phoneNumbers[i])

for k,v in phoneNumbers.items():
    print(f'The key is {k} and the corresponding value is {v} ')

















