from createLinkedList import *

ll = Node()

def spiralMatrix(m, n, head):
    matrix = [[-1]*n for row in range(m)]
    
    rowStart = 0
    rowEnd = m-1
    
    colStart = 0
    colEnd = n-1
    
    cur = head
    
    while cur and rowStart <= rowEnd and colStart <= colEnd:
        if cur and (rowStart <= rowEnd):
            for col in range(colStart, colEnd+1):
                if cur:
                    matrix[rowStart][col] = cur.val
                    cur = cur.next
                else:
                    break
            rowStart += 1
        
        if cur and colStart <= colEnd:
            for row in range(rowStart, rowEnd+1):
                if cur:
                    matrix[row][colEnd] = cur.val
                    cur = cur.next
                else:
                    break
            colEnd -= 1
        
        if rowStart <= rowEnd:
            for col in range(colEnd, colStart-1, -1):
                if cur:
                    matrix[rowEnd][col] = cur.val
                    cur = cur.next
                else:
                    break
            rowEnd -= 1
        
        if colStart <= colEnd:
            for row in range(rowEnd, rowStart-1, -1):
                if cur:
                    matrix[row][colStart] = cur.val
                    cur = cur.next
                else:
                    break
            colStart += 1
        
        return matrix

#Complexity:
#Time: O(k)
#Space: O(m*n)
#Where k is the length of the linked list, m is the no. of rows and n is the no. of columns of the matrix

#Test Cases:
#3, 5, [3,0,2,6,8,1,7,9,4,2,5,5,0]
#1, 4, [0,1,2]

head = ll.createLL([3,0,2,6,8,1,7,9,4,2,5,5,0])
print(spiralMatrix(3, 5, head))

head = ll.createLL([0,1,2])
print(spiralMatrix(1, 4, head))

#Link: https://leetcode.com/problems/spiral-matrix-iv/