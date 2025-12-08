'''
Numpy : is a Numerical array library in python
 It is used for mathematical and scientific computations.
 It was created in 2005 by Travis Oliphant.
    numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0, like=None)

'''   

'''
Why numpy array is faster then list
    >Numpy are Stored in continous memory location also called locality of reference.
    >It has fixed data type(int, float)
'''

'''
when creation of any n-array ( a = np.array([1, 2, 3]) ), internally it creates:
    -> A contiuous block of memory
    -> ndarray = {
        data pointer → memory,      -> Keep references to underlying buffer
        shape → (3,),               
        dtype → int32,
        strides → (4,),             -> It tells numpy how many bytes to jump to get next element(int -> 4)
        size → 3
    }
'''
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print(a)
print('Dtype : ',a.dtype)
print('Size : ',a.size)
print('Strides : ',a.strides)            #(To go to next rows, to go to next columns)
print('Type : ',type(a))

print('-------------------------------------------------------')
# O-D Arrays: The array that does not have any dimnension. Which consist of single value.
a1 = np.array(12)
print('Dimension of 0-D array : ',a1.ndim)
print('Shape of 0-D array : ',a1.shape) 
print('Size of 0-D array : ',a1.size) 

#1-D Arrays: The array that has 0 dimensional array has its elements.
a2 = np.array([1,2,3,4])
print(a2)
print('Shape of 1-D array : ',a2.shape) 

#2-D Arrays: The array that has 1 dimensional array has its elements.
a3 = np.array([[1,2,3,4],[5,6,7,8]])
print('2-D Array \n',a3)
print('Size of 2-D array : ',a3.size) 

# Array Creation : There are multiple ways to create an array in numpy
# 1. using List and Tuple
a=np.array([1,2,3,4])   # Using list
b=np.array((2,3,4))  # Using tuple
print('Creation of array using list : ',a)
print('Creation of array using tuple : ',b) 

#2. Using zeros,ones and fixed numbers
a1 = np.zeros((3))
a2 = np.ones((1,3))
a3 = np.full((2,2),9)
print('Zero Array creation : ',a1)
print('One Array creation : ',a2)
print('Fixed Array creation : \n',a3)

#3. Using of range,linspace and matrix
a1 = np.eye(3,3)
print('The array of identity matrix :\n',a1)
a2 = np.arange(1,11,2)
print(a2)
a3 = np.linspace(1,10,10)
print('The array of linspace matrix :\n',a3)

#4. Adding some more commands
a1 = np.empty((2,2))        # This creates an uninitialized array which contains garbage values.
print('This array created using empty : \n',a1)
a2= np.diag([1,2,3]) 
a3= np.diag([[1,2,3],[4,5,6]])
print('This array created using diagonal : \n',a2)
print('This array created using diagonal : \n',a3)

a = np.fromfile('.\\commands.txt', sep=' ')
print(a)