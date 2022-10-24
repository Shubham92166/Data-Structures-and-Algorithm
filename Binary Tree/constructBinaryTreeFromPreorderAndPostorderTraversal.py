from createBinaryTree import *

def constructFromPrePost(preorder, postorder):
    return helper(preorder, 0, len(preorder)-1, postorder, 0, len(postorder)-1)
    
def helper(self, pre, psi, pei, post, ppsi, ppei):
    if psi > pei:
        return
    
    root = TreeNode(pre[psi])
    if psi == pei:
        return root
    
    index = post.index(pre[psi + 1]) 
    tnn = index - ppsi + 1
    
    root.left = self.helper(pre, psi+1, psi+tnn, post, ppsi, index)
    root.right = self.helper(pre, psi + tnn+1, pei, post, index+1, ppei-1)
    
    return root

#Complexity:
#Time: O(n^2)
#Space: O(h)
#where O(h) in worst case can be O(n). h is the height of tree and n is the no. of nodes

#Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/