def generateMatrix(A):
    n = A
    res = []
    for i in range(n):
        res.append([0]*n)
    
    rStart=0
    rEnd=n-1
    cStart=0
    cEnd=n-1
    val = 1

    while(val-1 < n*n):
        
        for j in range(cStart, cEnd+1):
            res[rStart][j] = val
            val += 1 
        
        rStart+=1
        
        for row in range(rStart, rEnd+1):
            res[row][cEnd] = val
            val += 1 
            
        cEnd-=1

        for col in range(cEnd, cStart-1,-1):
            res[rEnd][col] = val
            val += 1
            
        rEnd-=1

        for i in range(rEnd, rStart-1, -1):
            res[i][cStart] = val
            val += 1
            
        cStart+=1

    return res

#Complexity:
#Time: O(n^2)
#Space: O(1)

#Test Cases:
#1, 2, 5

print(generateMatrix(1))
print(generateMatrix(2))
print(generateMatrix(5))

#Link: https://leetcode.com/problems/spiral-matrix-ii/