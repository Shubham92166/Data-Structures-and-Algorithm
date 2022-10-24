import queue

def levelOrder(root):
    q = queue.Queue()

    if not root:
        return

    ans = []
    temp = []

    ans.append([root.val])
    q.put(root)
    q.put(None)
    
    while not q.empty():
        node = q.get()
        if not node:
            if temp:
                ans.append(temp)
            if not q.empty():
                q.put(None)
            temp = []
            continue
        
        if node.children:
            for child in node.children:
                q.put(child)
                temp.append(child.val)
    
    return ans

#Complexity:
#Time: O(n)
#Space: O(n)


#Test Cases:
#[1,null,3,2,4,null,5,6], [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

#Link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/