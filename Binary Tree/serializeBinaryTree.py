import queue

def solve(A):
        q = queue.Queue()
        q.put(A)
        ans = []
        while not q.empty():
            node = q.get()
        
            if node == -1:
                ans.append(node)
                continue
            else:
                ans.append(node.val)
            
            if node.left:
                q.put(node.left)
            else:
                q.put(-1)
            
            if node.right:
                q.put(node.right)
            else:
                q.put(-1)
        return ans

#Complexity:
#Time: O(n)
#Space: O(n)

