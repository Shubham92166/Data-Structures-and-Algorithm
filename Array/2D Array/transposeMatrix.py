def transpose(matrix):
    rowSize = len(matrix)
    colSize = len(matrix[0])
    res = []
    for i in range(colSize):
        res.append([0]*rowSize)
    for i in range(rowSize):
        for j in range(colSize):
            res[j][i] = matrix[i][j]
    return res

#Complexity:
#Time: O(mn)
#Space: O(mn)

#Test Cases:
#[[1,2,3],[4,5,6],[7,8,9]], [[1,2,3],[4,5,6]]

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(transpose([[1,2,3],[4,5,6]]))

#Link: https://leetcode.com/problems/transpose-matrix/ 