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