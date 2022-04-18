def diagonalSort(mat):
    res = []
    m = len(mat)
    n = len(mat[0])
    r = m
    for i in range(m):
        res.append([0]*n)
    for i in range(m+n-1):
        r -= 1
        if i < m:
            x = r
            y = 0
        else:
            x = 0
            y = i - m + 1
        temp =[]
        while(x < m and y < n):
            temp.append(mat[x][y])
            x+= 1
            y += 1
        if i < m:
            x = r
            y = 0
        else:
            x = 0
            y = i - m + 1
        k = 0
        temp = sorted(temp)
        while(x < m and y < n):
            res[x][y] = temp[k]
            x += 1
            y += 1
            k += 1
    return res

#Test Cases:
# [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]

#Complexity:
#Time: O(m*n)
#Space: O(m*n)

print(diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
print(diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))