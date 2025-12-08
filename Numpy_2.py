import numpy as np

print('*************** Array Indexing **************')
arr = np.array([1, 2, 3, 4])
print('Indexing of 1-D Array')
print(arr[-1]+arr[0])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Indexing of 2-D Array')
print(arr[0,2],arr[0,-1],arr[1,1],arr[1,-1])

arr = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])
print('Indexing of 3-D Array')
print(arr)
print(arr[(0,0,-1)],arr[(0,1,1)],arr[(1,0,0)],arr[(1,1,-1)])

print('*************** Array Slicing **************')
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[0:-1])


print('*************** Array Slicing **************')

print('Slicing of 1-D Array')
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print('Slicing of 1-D array ',arr[0:-1:2])
print('Slicing of 1-D array ',arr[::3])
print('Slicing of 1-D array ',arr[3:])
print('Slicing of 1-D array ',arr[::-1])

print('Slicing of 2-D Array')
'''
   Indexing : a[row_index, column_index]
   Slicing :  a[row_start:row_end , col_start:col_end]

'''
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[11,12,13,14,15]])
print(arr[0,2])
print(arr[:,::2])
print(arr[::2,:])
print(arr[1])
print(arr[:,2])
print(arr[:,1:3])
