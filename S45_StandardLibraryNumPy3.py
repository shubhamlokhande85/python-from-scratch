

'C.2.8 Insert() '
'''
-np.insert() is a NumPy function used to insert values into an array at a 
specified position.It returns a new array because NumPy arrays have a
fixed size; the original array is not modified

- syntax
np.insert(arr,obj_index,elements or values, axis=None)
where,
arr: Input array.
obj: Index (or indices) before which to insert the values.
values: Value(s) to insert.
axis:
None (default): The array is flattened before insertion.
0: Insert rows.
1: Insert columns (for 2D arrays).

'''
# eg 01 - inserting single value in array
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
# [1 2 3 4 5]
inst=np.insert(arr,2,45)
print(inst)
# [ 1  2 45  3  4  5]

# eg 02 - inserting multiple values in array
inst2=np.insert(arr,2,[55,65,75])
print(inst2)
#[ 1  2 55 65 75  3  4  5]

#eg 03 inserting a row into 2D array 
arr2=np.array([[1,2],
               [3,4]])
inst3=np.insert(arr2,1,[5,6],axis=0)
print(inst3)
# [[1 2]
#  [5 6]
#  [3 4]]

#eg 04 inserting column into 2D array 
inst4=np.insert(arr2,0,[7,8],axis=1)
print(inst4)
# [[7 1 2]
#  [8 3 4]]

'C.2.9 Delete()'
'''
-np.delete() is a NumPy function used to delete values into an array at a 
specified position
-syntax
np.delete(arr,object_index, axis=None)'''

#eg o1 deleting single element from array
arr3=np.array([1,2,3])
d=np.delete(arr3,1)
print(np.delete(arr3,1))
# [1 3]
print(d)
# [1 3]

#eg 02 deleting multiple elements from a array
print(np.delete(arr3,[1,2]))
#[1]

#eg 03 deleting a specific row from a array 
arr4=np.array([[1,2],
               [3,4]])
d2=np.delete(arr4,1,axis=0)
print(d2)
#[[1 2]]

#eg 04 deleting specific column from a array 
d3=np.delete(arr4,0,axis=1)
print(d3)
# [[2]
#  [4]]

'C.2.10 Append()'
'''
-Add values to the end of an array
-syntax
np.append(arr,value)'''
#eg 
arr5=np.array([1,2,3,4,5])
d4=np.append(arr5,[6,7,8])
print(d4)
# [1 2 3 4 5 6 7 8]

'C.2.11 Repeat()'
'''
-np.repeat() is a function in numpy that reapeats elements of array
-syntax
np.repeat(arr,repeats_num,axis=None)
where,
arr = input array
repeats = Number of repettions for each elements , it can be 
    1.A single integer (same repetition for all elements)
    2.a list/array specifying repetitions for each element
axis = optional - axis along which to repeat values , If None the array is flattened  first'''

#eg 01 single integer used at repeat position
arr6=np.array([1,2,3])
print(np.repeat(arr6,2)) # two repeatitions of elements
# [1 1 2 2 3 3]

#eg 02 list/array used at repeat position
print(np.repeat(arr6,[2,2,3])) 
'Repeat each element a different number of time'
#[1 1  2 2 3 3 3]

#eg 03 row repeatition - 2D
arr7=np.array([[1,2],
              [3,4]])
rpt=np.repeat(arr7,2,axis=0)
print(rpt)
# [[1 2]
#  [1 2]
#  [3 4]
#  [3 4]]

#eg 04 column repeatition 
rpt2=np.repeat(arr7,2,axis=1)
print(rpt2)
# [[1 1 2 2]
#  [3 3 4 4]]

'C.2.12 Tile()'
'''
-np.tile() is a functions that repeat entire array
-syntax
np.tile(arr,repeats)
where,
arr = input array 
repeats = 1 . in case of single array  repeatition use integer
          2 . in case of row and column repeatition use (row,column)'''

#eg 01 repeatition of single array
arr8=np.array([1,2,3,4,5])
rpta=np.tile(arr8,2)
print(rpta)
# [1 2 3 4 5 1 2 3 4 5]

# eg 02 repeation of row and column repeatition 
arr9=np.array([[1,2],
               [3,4]])
rpta2=np.tile(arr9,(2,3))
print(rpta2)
# [[1 2 1 2 1 2]
#  [3 4 3 4 3 4]
#  [1 2 1 2 1 2]
#  [3 4 3 4 3 4]]


'C.2.13 Sort()'
'''
-np.sort() is used to sort the elements of an array
-syntax 
np.sort(arr,axis=-1)
where,
axis=-1  - last axis by default
    = 1  - for each row sorting 
    = 0  - for each column sorting'''
# eg 01 sorting array
arr10 = np.array([9,3,4,1,2,5])
print(np.sort(arr10))
# [1 2 3 4 5 9]

#eg 02 sorting 2D array 
arr11=np.array([[4,3],
                [1,2]])
print(np.sort(arr11))
# [[3 4]
#  [1 2]]

'C.2.14 reverse()'
'''
-In numpy their no np.reverse() but we can achieve this slicing index and 
np.flip()

'C.2.14.1 slicing[]
-syntax of reverse array slicing
arr_name[start:stop:step]


'''
#eg 1D
arr12 = np.array([1,2,3,4,5,5,6,7])
rever_arr12=arr12[::-1]
print(rever_arr12)
#[7 6 5 5 4 3 2 1]


'C.2.14.2 flip()'
'''
-np.flip() reverses the order of elements along a specified axis
-syntax of np.flip()
np.arr(arr,axis=None)
'''
#eg 02 2D array reversing using np.flip() 
arr13=np.array([[1,2],
                [3,4]])
print(np.flip(arr13, axis=0)) # row 
# [[3 4]
#  [1 2]]
print(np.flip(arr13, axis=1)) # column
# [[2 1]
#  [4 3]]

'C.2.15 Boolean indexing '
'''
-Boolean indexng in numpy is way to select or modify elements of array
 based on condition. you create a boolean array (True/False), and numpy
 returns the elements where the condition is true
-we use conditions like greater than (>) , even(==), less than(<), not equal(!=)

-syntax
 array[condition]'''
 #eg 
arr14=np.array([1,2,3,4,5,6,7,8,9])
bi=arr14[arr14>5]
print(bi)
# [6 7 8 9]

'C.2.16 fancy indexing'
'''
-fancy indexing in numpy is a method of acessing array elements using lists
or arrays of integer indices . unlike silicing , fancy indexing lets you 
select elements in any order and even repeat elements
-syntax
array[[index1,index2,index3..indexN]]'''
# eg 01 
arr15=np.array([10,20,30,40,50,60,70,80])
find=arr15[[0,1,4,5]]
print(find)
# [10 20 50 60]

'C.2.17  add()'
'''
-np.add() is used to to perform addition between two 
arrays elements
-syntax
np.add(arr1,arr2)
'''
#eg 
arr16=np.array([1,2,3,4])
arr17=np.array([5,6,7,8])
add=np.add(arr16,arr17)
print(add)
# [ 6  8 10 12]

'C.2.18 multiply()'
'''
-np.multiply() is used to to perform multiply between two 
arrays elements
-syntax
np.multiply(arr1,arr2)'''
#eg 
arr18=np.array([[1,2,3],
                [4,5,6]])
arr19=np.array([[7,8,9],
                [10,11,12]])

ml=np.multiply(arr18,arr19)
print(ml)
# [[ 7 16 27]
#  [40 55 72]]

'D. Scalar operation '
'''
scalar operations in numpy are operations where a single value(scalar) is
applied to every element of numpy array '''
#eg   + (scalar)
arr20=np.array([1,2,3,4])
add_scalar=arr20 + 5
print(add_scalar)
#[6 7 8 9]

#eg * (scalar)
arr21=np.array([1,2,3,4])
mul_scalar=arr21 * 5
print(mul_scalar)
# [ 5 10 15 20]

