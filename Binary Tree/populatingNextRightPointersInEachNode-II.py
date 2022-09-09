import queue

class Solution:
    def connect(self, root):
        
        if not root:
            return 
        
        q = queue.Queue()
        
        q.put(root)
        q.put(None)
        
        while not q.empty():
            node = q.get()
            
            if node and not q.empty():
                node.next = q.queue[0]
            
            if not node:
                if not q.empty():
                    q.put(None)
                continue
            
            if node.left:
                q.put(node.left)
            
            if node.right:
                q.put(node.right)
            
        return root

#Complexity:
#Time: O(n)
#Space: O(W)
#where W is the maximum no. of nodes at the last level

#Test Cases:
#[1,2,3,4,5,null,7], []

#Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/