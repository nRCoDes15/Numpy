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


print('*******************Data Types ********************')
'''
    1. Integer
        a) integer (signed) : contains both positive and negative
            1. int8 : (1 byte) (Range : -128 to 127)
            2. int16 : (2 byte) (−32,768 to 32,767)
            3. int32 : (4 byte) (Range : -2Billion to 2 billion)
            4. int64 : (8 byte) (huge range)
        b) integer(unsigned) : contains positive
            1. uint8 : (1 byte) (Range 0 to 255) 
            2. uint16 : (2 byte) (Range 0 to 255) 
    
    2. Floating point numbers:
        1. float16 : (2 bytes)
        2. float32 : (4 bytes)
        3. float64 : (8 bytes)
    
    3. Boolean Type
        1.True
        2.False
    
    4. Complex number:
        1.complex64 : 32bit real+32bit imaginary
        2.complex128 : 64bit real+64bit imaginary
    
    5. String types: 
        1.Unicode string :
        2.Byte string :
    
    6. Object: It allows mixed type, but numpy becomes slow.
        
'''