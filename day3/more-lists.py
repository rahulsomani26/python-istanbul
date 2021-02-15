# alphabet=['a','c','b','u','x']
# alphabet.sort()
# print(alphabet)

# names = ['Rahul','Somani','Ali','Mohammad','AAli']
# names.sort()
# print(names)



# '''
#   Sequence Data Type     
#   List 
#   range
#   Tuple 
# ''' 
# x = 1,2,3
# print(x)


my_list = [1,2]
# my_list.append(3)
my_list[len(my_list):]= [3]   
print(my_list)
# my_list[2:]=[3,4,5]  
my_list.extend([3,4,5])
print(my_list)


# Removing an item from the list , use the remove() method

my_list.remove(3)
print(my_list)

# my_list[2:3]=[]
# print(my_list)

my_list.pop(2)
print(my_list)

'''
 Deleting a single/ multiple items/ entire list 
 use the del keyword
 
'''
print('----'*20)
temp = ['somani','Patna','India']
print(len(temp))

del temp[1]
print(len(temp))
print(temp)

# del temp 
# print(temp)
print('---'*20)
new_list = ['Ali','Mohammad','Qatar','Saudi Arabia']
temp_list=new_list.copy()
print(temp_list)       

# Find out ways to copy a list 

# can list be nested  ? 

# nested_list = [1,2,3,[10,20,30,['s','a']],'End']
# print(len(nested_list))   # 5/7 
# print(nested_list)  

# print(nested_list[3][2])


tst = [10,[1,2,'somani'],'Ali',99]
print(tst)
print(len(tst))
print(tst[1][2])
# print(type(tst[1]))



