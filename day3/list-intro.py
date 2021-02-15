# '''
#    List are data structures 
#    The most flexible of all 
#    Can store heterogeneous / homogeneous values at a time, each item seperated by comma
 
#     To create a List use the []

#     marks = []   --> Empty List 
#     marks = List()  
    
# '''
 
# marks = [12,24,34,56]
# # print(type(marks))
# print(len(marks))

# print(marks[1])   # 24
# print(marks[-2])  # 34


# print(marks[0:3])   

# '''
#    Lists are mutable in nature ( can change )
   
# '''

# marks[1]= 90 
# print(marks)
# marks[0:3]=[1,2,3]
# print(marks)

# ''' 
#     Some common Methods on Lists 

# '''

# age = [10,40,5,38]

# result = age + marks
# print(result) 

# age.append(90)
# age.append(190)

# print(age)


# # extend()

# age.extend([1,2,3,4])
# print(age)

# # inserting an element at a desired location 
# # insert()

# age.insert(3,'rahul')
# print(age)

# print(age.pop(4))
# print(age)



marks = [10,4,3,9,19]
marks.sort(reverse=False)
print(marks)

print('-'*20)

age  = [ 19,56,78,1,56,76]
# print(age.sort(reverse=False))
age.sort(reverse=True)
print(age)

print('-'*20)

numbers = [1,2,1,1,0,-1,8,1,2,1]
print(numbers.count(9))

age = age.reverse()
print(age)














  
 
 
 