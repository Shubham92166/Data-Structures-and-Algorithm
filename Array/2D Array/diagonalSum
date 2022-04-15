def diagonalSum(mat):
    rowSize = len(mat)
    colSize = len(mat[0])
    rowSum = colSum = 0
    row = 0
    col = colSize - 1
    while(row < rowSize  and col >= 0):
        rowSum += mat[row][row]
        row += 1
        col -= 1
    row = 0
    col = colSize - 1
    while(row < rowSize and col >= 0):
        colSum += mat[row][col]
        row += 1
        col -= 1
    if rowSize == colSize and rowSize % 2 and colSize % 2:
        mid = (rowSize-1)//2 
        return rowSum + colSum - mat[mid][mid]
    else:
        return rowSum + colSum 

#Test Cases:
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[7,9,8,6,3],[3,9,4,5,2],[8,1,10,4,10],[9,5,10,9,6],[7,2,4,10,8]]
mat3 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
mat4 = [[5]]

#Time Complexity:
#Time: O(N)
#Space: O(1)

print(diagonalSum(mat1))
print(diagonalSum(mat2))
print(diagonalSum(mat3))
print(diagonalSum(mat4))