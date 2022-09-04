class TreeNode:
     def __init__(self, val = 0, left = None, right = None):
         self.val = val
         self.left = left
         self.right = right
         
def sortedListToBST(head):
    allNodes = []
    cur = head
    while cur:
        allNodes.append(cur.val)
        cur = cur.next
        
    return sortedArrayToBST(allNodes)

def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[-10,-3,0,5,9], []

#Link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

