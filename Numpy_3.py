import numpy as np

print('*************Shape And Reshape****************')
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([1,2,3,4,5],ndmin=5)
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.strides)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr1 = arr.reshape(4,3)
newarr2 = arr.reshape(3,2,2)
print('Reshape to 2-D array : \n',newarr1)
print('Reshape to 3-D array : \n',newarr2)

# Check whether it returns copy or view ?
print(arr.reshape(2,2,3).base)      # this returns just a view not a copy

# we can pass one "Unknown" dimension(-1) automatically numpy decides [only for 1 dimension]
a=arr.reshape(3,2,-1)
print(a.shape)

print('------------------------------------')
# Flatten : is coverting multi dimensional array to single dimension
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.reshape(-1))

'''
    flatten() : It always returns the copy (new array)  , slighlty slower
    ravel() : It returns the view   , fast
'''
a=arr.flatten()
print(a.base)
b=arr.ravel()
print(b.base)

# In this ravel return copy coz, If array is ->Non-contiguous (from slicing) -> Created through some operations
arr = np.arange(10)[::2]  # sliced, non-contiguous
r = arr.ravel()
print(r.base)

print('******************* nditer and ndenumerate**************************')

arr = np.array([1, 2, 3])
for i in arr:
    print(i,end=' ')
print()
arr = np.array([[1, 2, 3], [4, 5, 6]])
for i in arr:
    for j in i:
        print(j,end=' ')
print()      
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for i in arr:
    for j in i:
        for k in j:
            print(k,end=' ')
print()
# Hence instead of this we can use nditer
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for i in np.nditer(arr):
    print(i,end = ' ')
print()

'''
We can use os_dtypes argument to change the datatype of an element.
flags=['buffered'] allows NumPy to use temporary memory to safely convert each integer into a string 
    during iteration because the original array cannot be modified in-place to store string values.
'''

arr = np.array([1, 2, 3])
for i in np.nditer(arr,flags=['buffered'],op_dtypes='S'):
    print(i,i.dtype,end = ' ')
print()

# iterating with different step size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i in np.nditer(arr[:,::2]):
    print(i,end=' ')
print()
    
# use of np.ndenumerate
arr = np.array([1, 2, 3])  # for 1-D array
for i,j in np.ndenumerate(arr):
    print(i,j,end=' ')
print()

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i,j in np.ndenumerate(arr): # for 2-D array
    print(i,j,end=' ')
print()


print('***********************Joins in Numpy********************************')
'''
    1. np.concatenate() : It does not create a new axis. It join array along with existing axis
'''
a1 = np.array([1,1,1,1])
a2 = np.array([5,5,5,5])
res = np.concatenate((a1,a2),axis=0)
print('The result is a concatenate of axis 0 : ',res)       # can't use axis=1 coz this is an 1-D array 

a1 = np.array([[1,2],[3,4]])
a2 = np.array([[7,8],[9,10]])
a3 = np.concatenate((a1,a2),axis=1)
print(a3)

'''
    1. np.stack() : same as concatenate function which joins the array but it create new axis
'''
print('-------------------stack--------------------')
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

a3 = np.stack((a,b),axis=2)
print(a3)
print(a3.shape)

'''
    1. np.vstack() : vertically(row wise) stack the arrays
'''
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])
res1 = np.vstack((a,b))
print(res1)

'''
    1. np.hstack() : horizontally(column wise) stack the arrays
'''
res2 = np.hstack((a,b))
print(res2)

'''
    1. np.dstack() : depth-wise stack the arrays
'''
res3 = np.dstack((a,b))
print(res3)

x = np.array([1,2,3])
y = np.array([4,5,6])
print(np.column_stack((x,y)))   # same as hstack

print(np.row_stack((x,y)))      # same as vstack

# Note : stack and dstack creates an new axis

print('*******************Splitting Numpy array*********************')
print('------------Splitting 1-D array-----------------------')
a = np.array([1,2,3,4,5,6])
res1 = np.split(a,2)
res2 = np.array_split(a,4)
print(res1)
print(res2)

print('------------Splitting 2-D array-----------------------')
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
res3 = np.split(a,2,axis=0)
print(res3)

res4 = np.split(a,3,axis=1)
print(res4)

print('--------------------')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
res5 = np.hsplit(arr,3)
print(res5)

res6 = np.vsplit(arr,6)
print(res6)

print('--------------------')
arr = np.arange(1,17).reshape(4,2,2)
print(arr)
res6 = np.dsplit(arr,2)
print(res6)