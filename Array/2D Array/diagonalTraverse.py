def findDiagonalOrder(mat):
    rowSize = len(mat)
    colSize = len(mat[0])
    res = []
    for i in range(rowSize + colSize -1):
        if i < colSize: 
            x = 0
            y = i
        else:
            x = i - colSize + 1
            y = colSize - 1
        temp = []
        while(x < rowSize and y >= 0):
            temp.append(mat[x][y])
            x += 1
            y -= 1
        if i%2:
            res.extend(temp)
        else:
            res.extend(temp[::-1])
    return res

#Test Cases:
#mat1 = [[1,2,3],[4,5,6],[7,8,9]]
#mat2 = [[1,2],[3,4]]
#mat3 = [[3,2]]

#Complexity:
#Time: O(m*n)
#Space: O(m)

print(findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(findDiagonalOrder([[1,2],[3,4]]))
print(findDiagonalOrder([[3,2]]))

#Link: https://leetcode.com/problems/diagonal-traverse/