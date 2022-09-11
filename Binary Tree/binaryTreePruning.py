def pruneTree(root):
    if not root:
        return 
    
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)
    
    if root.val == 0 and root.left == None and root.right == None:
        return None

    return root

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) can be O(n) is worst case. h is th height and n is the no. of nodes

#Test Cases:
#[1,None,0,0,1], [1,0,1,0,0,0,1], [1,1,0,1,1,0,1,0]

#Link: https://leetcode.com/problems/binary-tree-pruning/