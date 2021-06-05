import numpy as np
twoDArray=[[1,2,3],[4,5,6],[7,8,9]]
def accessElement(array,rowindex, colindex):
    try:
        print(array[rowindex][colindex])
    except:
        print("Incorrect row index or column index")

accessElement(twoDArray,2,3)
accessElement(twoDArray,2,2)