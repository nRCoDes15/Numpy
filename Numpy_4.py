import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])
print(np.where(arr==5))
print(np.where(arr%2==0))
print(np.where(arr%2==0,'even','odd'))


print(arr[arr>2])
print(arr[arr%2==0])
print(arr[arr!=5])

arr = np.array([0,4,0,7,9])
print(np.nonzero(arr))
print(np.argmin(arr))
print(np.argmax(arr))

#searchsorted : where the elements to be inserted to keep array sorted
arr = np.array([10,20,30,40])
print(np.searchsorted(arr,15))
print(np.searchsorted(arr,15,side='right'))
