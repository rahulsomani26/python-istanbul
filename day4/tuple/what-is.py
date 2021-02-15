'''
   Tuples are data structures that stores multiple values 
   at a time . All the values may be of the same or different type 
   They are basically used to store heterogeneous
   
   How it is created : Syntax ()---> Empty tuple 
                                ----> tuple()
                                
   

'''

# empty_tuple = ()
# print(type(empty_tuple))
# print(len(empty_tuple))

# Creating a tuple with only a single element 

# name = 'Ali',
# age = (24,)
# print(type(name),type(age),name,age)

# Tuples are immutable in nature ( it cannot be changed once created)

first_tuple = (10,'rahul','India','UAE','Mumbai')
print(first_tuple)
# first_tuple[1] = 'somani'   # Item assignment not allowed in tuple
print(first_tuple)

'''
  Accessing element within a tuple
  By Index position
  
'''
print(first_tuple[2])
print(first_tuple[-1])
print(first_tuple[-3])

'''
 Slicing tuples
'''

print(first_tuple[1:3])
print(first_tuple[:])  #
print(first_tuple[:5:2])  #


'''
   If you really want to update an item in a tuple 
   convert the tuple in a list , make neccessary changes and then again change the list 
   into a tuple
'''

y = (1,2,10,20)  # update the item at index pos 2 
x = list(y)
print(y,x) 
x[2]='somani'
y = tuple(x)
print(f'Final value of the tuple is {y}')

'''
  Cannot add items in a tuples as there is no append() method 
'''
a = (1,2)
b = list(a)
b.append(4)
a = tuple(b)
print(a)

# a[0:2]=()  # won't work
# print(a)

# del a 
# print(a)

'''
  Loop through a tuple
'''

c = (8,'r','s','7',56,True,False)

'''
 Syntax of a for loop 
 for varible_name in object:
     
'''

for item in c:
    print(item)
    















 





