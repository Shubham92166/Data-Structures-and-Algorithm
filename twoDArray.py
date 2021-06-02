import numpy as np
#creating array
Array=np.array([[1,2,3,4],[5,9,8,6],[7,8,4,5]])
print(Array)
#adding one column at pos 0, axis=1 means column wise
newTwoDArray=np.insert(Array,1,[[7,4,6]],axis=1)
print(newTwoDArray)
#adding one row at pos 0, axis=0 means row wise
newTwoDArray=np.insert(Array,1,[[7,4,6,4]],axis=0)
print(newTwoDArray)
#if we are adding any row/column at any given position except last position then time complexity will be O(nm)
#adding one column at pos 0, axis=1 means column wise
#adding column at the end
newTwoDArray=np.append(Array,[[9],[2],[6]],axis=1)
print(newTwoDArray)
