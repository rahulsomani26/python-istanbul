# msg = 'Ali Turkey'
# temp = msg 
# print(temp)
 
 

# print(id(msg))
# print(id(temp))



# # msg[0]='B'
# # print(msg)

'''
   We cannot change a string once created 
  Strings are immutable in nature ( we cannot change a string once created )
  
'''

'''
 Some string methods ()

'''


# msg = ' Hello world ! '
# print(msg.upper())  # It will change all char in upper case 
# print(msg.title())  # It will change all char in upper case 
# # print(msg.lower())  # It will change all char in upper case 
# print('RAHUL'.lower())

# print('rahul somani'.capitalize())  
# print('rAhUL SOmaNi'.swapcase())  



'''
  Sequence operation 
  
  len()
  max(), min() 
  s in b
  
  
'''

# msg = 'Hello I am there for you '  
# result = 'fr' in msg
# print(result)

# test_string = 'Aabc'    # ASCII values A 65 B 66 a 65+32 = 97 
# print(min(test_string))
# print(max(test_string))  


'''
 What are literals ( variables / constants )
 
'''
# m = 'x'
# print('li' + 'mi'+ m )


'''
 Some more string methods 
  strip()
 split()
 replace()
 rsplit()     # can u write a program that mimics rsplit and lsplit
 lsplit()

 .....
'''


# strip_test = '.....Ali Mohammad.....?'
# print(strip_test.strip('?.'))  # order is not important 

# your_name = 'Ali+Mohammad'
# splitted_val = your_name.split()
# print(splitted_val)
# print(your_name.split('+'))


'''
  find() 
'''

# my_name = 'My name is rahul somani and I stay in India'
# result = my_name.find('stay',14)
# if result == -1:
#     print(' not found')
# else:
#     print('found')



# test_string = 'Apple is my fav fruit'
# print(test_string.replace('Apple','Orange'))


print('#'.join('rahul'))

'''
    couple of more methods 
'''

msg_1 = '123'
msg_2 = 'Rahul123'
msg_3 = 'somani.classes@outlook.com'

print(msg_2.isalnum())
print(msg_3.isalnum())
print(msg_1.isalnum())

print('-'*20)

print(msg_1.isalpha())  # False
print(msg_2.isalpha())  # True
print(msg_3.isalpha())  # False

print('--'*20)

print(msg_2.startswith('a'))
print(msg_2.startswith('Ra'))
print(msg_2.startswith('Rah'))
print(msg_2.startswith('u'))

print('-'*20)
print(msg_3.endswith('om'))












 






