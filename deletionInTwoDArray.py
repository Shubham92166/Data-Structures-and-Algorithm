import numpy as np
array=[[1,2,3],[4,5,6],[7,8,9]]
newArray=np.delete(array,0,axis=0)
print(newArray)
newArray=np.delete(array,0,axis=1)
print(newArray)