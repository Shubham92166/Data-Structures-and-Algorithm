def evaluateTree(root):
    return helper(root)

def helper(root):
    if not root.left and not root.right:
        if root.val == 0:
            return False
        else:
            return True
    
    if root.val == 2:
        return helper(root.left) or helper(root.right)
    else:
        return helper(root.left) and helper(root.right)

#Complexity:
#Time: O(n)
#Space: O(h) or O(log n)
#where h is height of binary tree. Since the given tree is full binary tree so h is log n.

#Link: https://leetcode.com/problems/evaluate-boolean-binary-tree/