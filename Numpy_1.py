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


