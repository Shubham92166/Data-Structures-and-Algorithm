class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

import queue
from tempfile import TemporaryDirectory
class BinaryTee:
    def createBinaryTree(self, nums):
        q = queue.Queue()
        i = 0
        if not nums or (len(nums) == 1 and nums[0] == -1):
            return None
        root = TreeNode(nums[i])
        q.put(root)
        i += 1
        while not q.empty() and i < len(nums):
            node = q.get()
            if  i < len(nums) and (nums[i] != None or nums[i] != -1):
                leftChild = TreeNode(nums[i])
                node.left = leftChild
                q.put(leftChild)
                i += 1

            if i < len(nums) and (nums[i] != None or nums[i] != -1) :
                rightChild = TreeNode(nums[i])
                node.right = rightChild
                q.put(rightChild)
                i += 1
        
        return root
    
    def printTree(self, root):
        ans = []
        q = queue.Queue()
        if not root:
            return None
        q.put(root)
        q.put(None)
        temp = []
        ans.append([root.val])

        while not q.empty():
            node = q.get()
            if not node:
                #print(len(temp))
                if temp:
                    ans.append(temp)
                if not q.empty():
                    q.put(None)
                temp = []
                continue
            
            if node.left != None:
                q.put(node.left)
                temp.append(node.left.val)
            if node.right != None:
                q.put(node.right)
                temp.append(node.right.val)
        return ans



