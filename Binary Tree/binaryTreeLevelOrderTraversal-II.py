import queue

def levelOrderBottom(root):
    if not root:
        return None
    q = queue.Queue()
    res = []
    res.append([root.val])
    temp = []
    q.put(root)
    q.put(None)
    while(not q.empty()):
        node = q.get()
        if node == None:
            if temp:
                res.append(temp)
            if not q.empty():
                q.put(None)
                temp = []
            continue
        if node.left:
            q.put(node.left)
            temp.append(node.left.val)
        if node.right:
            q.put(node.right)
            temp.append(node.right.val)
    return res[::-1]

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the no. of nodes

#Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/