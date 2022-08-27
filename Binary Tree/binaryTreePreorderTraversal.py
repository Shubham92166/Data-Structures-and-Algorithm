def preorderTraversal(root):
        ans = []
        preOrder(root, ans)
        return ans
def preOrder(root, ans):
    if not root:
        return 0
    ans.append(root.val)
    preOrder(root.left, ans)
    preOrder(root.right, ans)

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the no. of nodes

#Test Cases:
#[1,null,2,3], [], [1]

#Link: https://leetcode.com/problems/binary-tree-preorder-traversal/