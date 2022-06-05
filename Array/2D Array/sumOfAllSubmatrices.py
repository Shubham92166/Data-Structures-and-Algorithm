def sumOfMatrices(A):
    n = len(A)
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += A[i][j] * (i+1)*(j+1) * (n-i) *(n-j)
    return sum


#Complexity:
#Time: O(n2)
#Space: O(1)

#Test Cases:
#[ [1, 1], [1, 1] ]

print(sumOfMatrices([ [1, 1],[1, 1] ]))