def postorderTraversal(root):
        ans = []
        postOrder(root, ans)
        return ans

def postOrder(root, ans):
    if not root:
        return None
    
    postOrder(root.left, ans)
    postOrder(root.right, ans)
    ans.append(root.val)

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the no. of nodes

#Test Cases:
#[1,null,2,3], [], [1]

#Link: https://leetcode.com/problems/binary-tree-postorder-traversal/