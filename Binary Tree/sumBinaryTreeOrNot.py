def solve(A):
    res, Sum = helper(A)
    if res == True:
        return 1
    else:
        return 0

def helper(root):
    if not root:
        return True, 0 
    
    if not root.left and not root.right:
        return True, root.val
        
    ans, lsum = helper(root.left)
    ans, rsum = helper(root.right)
    
    if root.val == lsum + rsum:
        return True, root.val + lsum + rsum
    else: 
        return False, root.val + lsum + rsum

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the no. of nodes