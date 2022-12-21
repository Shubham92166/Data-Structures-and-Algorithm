def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    
    elif rowIndex == 1:
        return [1,1]
    
    pascal = [1,1]

    i = 1

    while i < rowIndex:
        temp = [1]
        i += 1
    
        for j in range(len(pascal)-1):
            temp.append(pascal[j+1] + pascal[j])
        
        temp.append(1)
        
        pascal = temp 
    
    return pascal

#Complexity:
#Time: O(n^2)
#Space: O(n)

#Test Cases:
#3, 0, 1, 33

print(getRow(3))
print(getRow(0))
print(getRow(1))
print(getRow(33))

#Link: https://leetcode.com/problems/pascals-triangle-ii/description/