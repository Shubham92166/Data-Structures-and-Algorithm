def pivotInteger(n):
    if n == 1:
        return 1
    
    pre = [0]*n
    pre[0] = 1
    
    for i in range(1, n):
        pre[i] = pre[i-1] + i+1
    
    
    for i in range(1, n):
        if pre[i] == pre[-1] - pre[i-1]:
            return i+1
    
    return -1

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#8, 1, 4

print(pivotInteger(8))
print(pivotInteger(1))
print(pivotInteger(4))

#Link: https://leetcode.com/problems/find-the-pivot-integer/