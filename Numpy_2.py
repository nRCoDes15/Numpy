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