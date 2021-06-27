list=[1,5,9,9,4,4,1,2,2,3,12,12,74,74,85,3,20]
newList=[]
def uniqueElements(list):
    for element in list:
        if(element in newList):
            return False
        else:
            newList.append(element)           
    return True
print(uniqueElements(list))
