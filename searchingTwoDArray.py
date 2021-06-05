array=[[1,2,3],[4,5,6],[7,8,9]]
def searchElement(array,element):
    for row in range(len(array)):
        for column in range(len(array[0])):
            if(array[row][column]==element):
                return "Element is found at", row,column
    return "Element is not found"
print(searchElement(array,10))
print(searchElement(array,3))