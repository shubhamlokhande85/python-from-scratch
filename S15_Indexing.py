'''1.indexing'''
'''in python indexing means accessing individual elements of sequence 
using their position(index)'''
# in python indexing start from 0 
# indexing always travelling or iterating left to right
# there is two of indexing positive indexing and negative indexing 

list = [1,2,3,4,5,6,7,8,9]
#index  0 1 2 3 4 5 6 7 8 

print(list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]  

'''1.1. positive indexing '''
print(list[1]) # 2 

'''1.2.negative indexing - negative indexing start from -1 '''
print(list[-1]) # -2 

'''1.3.slicing list using indexing '''
slice = list[0:5]
print(slice) # its slice list but not include last index cause last considerated as range index 
# [1, 2, 3, 4, 5] 

print(list[:]) # its also called [0:-1] its print entire list 
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list[-3:]) # it is also called [-3:-1]
#[7, 8, 9]

'''1.4.updating elements using indexing '''
list[2] = "IRONMAN"
print(list)
# [1, 2, 'IRONMAN', 4, 5, 6, 7, 8, 9]

'''1.5.deleting elements using indexing'''
# when have delete we use del keyword 
'''a.deleteing specific element'''
del list[0]
print(list)
# [2, 'IRONMAN', 4, 5, 6, 7, 8, 9]

'''b.deleting entire list'''
list2 =["s",False,True,(8+9j),900]
print(list2)
#["s",False,True,(8+9j),900]
del list2 # its delete entire list
'''print(list2)''' # raise nameError
#NameError: name 'list2' is not defined. Did you mean: 'list'?
