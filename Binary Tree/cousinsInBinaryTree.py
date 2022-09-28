#Method-1: Using DFS (2 passes):

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def isCousins(root, x: int, y: int):
    dummy = TreeNode(-1)
    levelOfX, parentOfX = searchNode(root, x, dummy, 0)
    levelOfY, parentOfY = searchNode(root, y, dummy, 0)
    if levelOfX == levelOfY and parentOfX != parentOfY:
        return True
    else:
        return False
    
def searchNode(root, value, parent, level):
    if not root:
        return ()
    if root.val == value:
        return (level, parent.val)
    left = searchNode(root.left, value, root, level+1)
    right = searchNode(root.right, value, root, level+1)
    return left or right

#Complexity:
#Time: O(n)
#Space: O(h)
#where h in worst case can be n. h is the height and n is the no. of nodes

#Method-2: Using DFS (1 pass):

def isCousins(root, x, y):
    dummy = TreeNode(-1)
    ans = searchNode(root, x, dummy, y, dummy, 0)
    if len(ans) != 4:
        return False
    levelOfX, parentOfX, levelOfY, parentOfY = ans
    if levelOfX == levelOfY and parentOfX != parentOfY:
        return True
    else:
        return False
    
def searchNode(root, value1, parent1, value2, parent2, level):
    if not root:
        return ()
    if root.val == value1:
        return [level, parent1.val]
    
    if root.val == value2:
        return [level, parent2.val]
    
    left = searchNode(root.left, value1, root, value2, root, level+1)
    right = searchNode(root.right, value1, root, value2, root, level+1)
    ans = []
    if left:
        ans.extend(left)
    if right:
        ans.extend(right)
    
    return ans

#Complexity:
#Time: O(n)
#Space: O(h)
#where h in worst case can be n. h is the height and n is the no. of nodes

#Test Cases:
#[1,2,3,4], 4, 3
#[1,2,3,null,4,null,5], 5, 4
#[1,2,3,null,4], 2, 3
#[1,null,2,3,null,null,4,null,5], 1, 3
#[1,2,3,null,null,4,5], 4, 5

#Link: https://leetcode.com/problems/cousins-in-binary-tree/