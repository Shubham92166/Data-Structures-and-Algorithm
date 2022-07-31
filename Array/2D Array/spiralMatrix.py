def spiralOrder(matrix):
    rStart = 0        
    nRows = len(matrix)
    mCols = len(matrix[0])
    rEnd = nRows-1
    cStart = 0
    cEnd = mCols-1
    count = 0
    res = []
    while(rStart <= rEnd and cStart <= cEnd):
        for j in range(cStart, cEnd+1):
            res.append(matrix[rStart][j])
            count += 1
        rStart += 1
        for i in range(rStart, rEnd+1):
            res.append(matrix[i][cEnd])
            count += 1
        cEnd -= 1
        if rStart <= rEnd:
            for i in range(cEnd, cStart-1, -1):
                res.append(matrix[rEnd][i])
                count += 1
            rEnd -= 1
        if cStart <= cEnd:
            for i in range(rEnd, rStart-1, -1):
                res.append(matrix[i][cStart])
                count += 1
            cStart += 1
    return res

#Complexity:
#Time: O(n*m)
#Space: O(1)

#Test Cases:
#[[1,2,3],[4,5,6],[7,8,9]], [[1,2,3,4],[5,6,7,8],[9,10,11,12]], [[2,5,8],[4,0,-1]]

print(spiralOrder([[2,5,8],[4,0,-1]]))
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

#Link: https://leetcode.com/problems/spiral-matrix/