class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

import queue
class BinaryTee:
    def createBinaryTree(self, nums):        
        start = 0
    
        length = len(nums)

        if length <= 1 :
            return None
        
        root = TreeNode(nums[start])
        start += 1

        q = queue.Queue()
        q.put(root)

        while not q.empty():
            currentNode = q.get()

            leftChild = nums[start]
            start += 1

            if leftChild != -1:
                leftNode = TreeNode(leftChild)
                currentNode.left =leftNode
                q.put(leftNode)

            rightChild = nums[start]
            start += 1

            if rightChild != -1:
                rightNode = TreeNode(rightChild)
                currentNode.right =rightNode
                q.put(rightNode)

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



