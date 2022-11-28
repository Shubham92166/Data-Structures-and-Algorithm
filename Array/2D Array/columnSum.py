'''
Question:
You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.

Problem Constraints
1 <= A.size() <= 103
1 <= A[i].size() <= 103
1 <= A[i][j] <= 103
'''

def solve(A):
    res = []
    rowSize = len(A)
    colSize = len(A[0])
    for col in range(colSize):
        sum = 0
        for row in range(rowSize):
            sum += A[row][col]
        res.append(sum)
    return res

#Complexity:
#Time: O(n*m)
#Space: O(m)
#Where n is the no. of rows and m is the no. of columns

#Test Cases:
#[[1,2,3,4], [5,6,7,8], [9,2,3,4]]

print(solve([[1,2,3,4], [5,6,7,8], [9,2,3,4]]))
