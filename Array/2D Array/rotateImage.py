def rotateMatrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in range(n):
        reverseRow(matrix[row], 0, n-1)
    return matrix
    
def reverseRow(A, start, end):
    while(start < end):
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

#Test Cases:
#matrix1 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# matrix2 = [[1,2,3],[4,5,6],[7,8,9]]

#Complexity:
#Time: O(N)
#Space: O(1)

print(rotateMatrix([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
print(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]])) 