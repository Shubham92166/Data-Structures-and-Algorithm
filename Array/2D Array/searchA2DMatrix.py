def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    l = 0
    r = n*m - 1
    while(l <= r):
        mid = (l+r)//2
        row = mid//n
        col = mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

#Complexity: O(log (n*m))
#Space: O(1)

#Test cases:
#[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3
#[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))

#Link: https://leetcode.com/problems/search-a-2d-matrix/