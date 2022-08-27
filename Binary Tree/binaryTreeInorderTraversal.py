def inorderTraversal(root):
        ans = []
        inorder(root, ans)
        return ans

def inorder(root, ans):
    if not root:
        return None
    inorder(root.left, ans)
    ans.append(root.val)
    inorder(root.right, ans)

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the number of nodes

#Test Cases:
#[1,null,2,3], [], [1]

#Link: https://leetcode.com/problems/binary-tree-inorder-traversal/