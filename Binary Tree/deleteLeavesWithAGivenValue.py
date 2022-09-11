def removeLeafNodes(root, target):
    if not root:
        return
    
    root.left = removeLeafNodes(root.left, target)
    root.right = removeLeafNodes(root.right, target)
    
    if root.val == target and root.left == None and root.right == None:
        return None
    
    return root

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) can be O(n) in worst case. h is the height and n is the no. of nodes

#Test Cases:
#[1,2,3,2,None,2,4], 2
#[1,3,3,3,2], 3
#[1,2,None,2,None,2], 2

#Link: https://leetcode.com/problems/delete-leaves-with-a-given-value/