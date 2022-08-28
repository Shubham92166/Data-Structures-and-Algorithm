def checkTree(root):
    if root.val == root.left.val + root.right.val:
        return True
    else:
        return False

#Complexity:
#Time: O(1)
#Space: O(1)

#Test Cases:
#[10,4,6], [5,3,1]

#Link: https://leetcode.com/problems/root-equals-sum-of-children/