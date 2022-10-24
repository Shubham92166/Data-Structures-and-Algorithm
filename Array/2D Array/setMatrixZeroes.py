def setZeroes(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == 0):
                setRow(matrix, len(matrix), j)
                setCol(matrix, i, len(matrix[0]))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == None):
                matrix[i][j] = 0
    
    return matrix
                
def setRow(matrix, row, col):
    for i in range(0, row):
        if matrix[i][col]:
            matrix[i][col] = None
def setCol(matrix, row, col):
    for i in range(0, col):
        if matrix[row][i]:
            matrix[row][i] = None

#Complexity:
#Time: O(n^2)
#Space: O(1)

#Test Cases:
#[[1,1,1],[1,0,1],[1,1,1]], [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

#Link: https://leetcode.com/problems/set-matrix-zeroes/
        