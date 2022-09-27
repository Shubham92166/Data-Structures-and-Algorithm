import sys
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")

def insertIntoBST(root, val):
    if not root:
        node = TreeNode(val)
        return node
    if root.val > val:
        root.left = insertIntoBST(root.left, val)
        return root
    if root.val <= val:
        root.right = insertIntoBST(root.right, val)
        return root

#Complexity:
#Time: O(H)
#Space: O(H)
#where H is the height of the tree. In worst case O(H) can be O(n) and n is the no. of nodes

#Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/

        