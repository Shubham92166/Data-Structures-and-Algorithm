import queue

def levelOrder(root):
    if not root:
        return None
    ans = []
    temp = []
    ans.append([root.val])
    q = queue.Queue()
    q.put(root)
    q.put(None)
    while(not q.empty()):
        node = q.get()
        if node == None:
            if temp:
                ans.append(temp)
                
            if not q.empty():
                q.put(None)
                temp = []
            continue
        
        if node.left:
            temp.append(node.left.val)
            q.put(node.left)
        if node.right:
            temp.append(node.right.val)
            q.put(node.right)
    return ans

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the no. of nodes

#Link: https://leetcode.com/problems/binary-tree-level-order-traversal/