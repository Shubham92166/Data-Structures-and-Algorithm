import queue
from createBinaryTree import *

class Codec:
    def serialize(self, root):
       
        if not root:
            return ""
        
        q = queue.Queue()
        q.put(root)
        ans = ""
        ans += str(root.val)
        ans += "#"
        while not q.empty():
            node = q.get()
          
            if not node:
                continue
            
            if node.left:
                q.put(node.left)
                ans += str(node.left.val)
                ans += "#"
            else:
                ans += str(-10000000000)
                ans += "#"
        
            if node.right:
                q.put(node.right)
                ans += str(node.right.val)
                ans += "#"
            else:
                ans += str(-10000000000)
                ans += "#"
       
        return ans

    def deserialize(self, data):
    
        if data == "":
            return 
        data = [val for val in data[:-1].split("#")]
        q = queue.Queue()
        
        i = 1
        self.root = TreeNode(int(data[0]))
        q.put(self.root)
        
        while not q.empty():
            node = q.get()
            if data[i] != "-10000000000":
                node.left = TreeNode(int(data[i]))
                q.put(node.left)
            
            i += 1
            
            if data[i] != "-10000000000":
                node.right = TreeNode(int(data[i]))
                q.put(node.right)
           
            
            i += 1
            
        return self.root

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1,2,3,null,null,4,5], []

#Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/