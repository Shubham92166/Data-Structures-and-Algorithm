from createBinaryTree import *
import sys
sys.setrecursionlimit(10**6)

def solve(self, A):
        q = queue.Queue()
        k = 1
        root = TreeNode(A[0])
        q.put(root)
        while not q.empty():
            node = q.get()

            if A[k] != -1:
                node.left = TreeNode(A[k])
                q.put(node.left)
            else:
                node.left = None

            k += 1

            if A[k] != -1:
                node.right = TreeNode(A[k])
                q.put(node.right)
            else:
                node.right = None
                
            k += 1

        return root

#Complexity:
#Time: O(n)
#Space: O(n)
