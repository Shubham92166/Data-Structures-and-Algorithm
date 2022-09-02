import math
def isValidBST(root):
        return helper(root, -math.inf, math.inf)
        
def helper(root, l, r):
    if not root:
        return True
    if root.val >= l and root.val <= r:
        left = helper(root.left, l, root.val-1) 
        right = helper(root.right, root.val+1, r)
        return left and right
    else:
        return False
    
#Complexity:
#Time: O(H) 
#Space: O(H)
#O(H) in worst case could be O(n)

#Test Cases:
#[2,1,3], [5,1,4,null,null,3,6]

#Link: https://leetcode.com/problems/validate-binary-search-tree/