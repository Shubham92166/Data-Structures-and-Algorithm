def postorder(root):
    ans = []
    helper(root, ans)
    return ans

def helper(root, ans):
    if not root:
        return
    
    for child in root.children:
        helper(child, ans)
    
    ans.append(root.val)

#Complexity:
#Time: O(H)
#Space: O(H)
#where H in worst case can be O(n)

#Test Cases:
#[1,null,3,2,4,null,5,6], [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

#Link: https://leetcode.com/problems/n-ary-tree-postorder-traversal/


