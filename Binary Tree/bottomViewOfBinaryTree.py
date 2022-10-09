import queue
class Solution:
    def bottomView(self, root):
        self.dic = {}
        q = queue.Queue()
        q.put((root, 0))
        while not q.empty():
            node = q.get()
            level = node[1]
            Root = node[0]
            self.dic[level] = Root.data
           
            if Root.left:
                q.put((Root.left, level-1))
            if Root.right:
                q.put((Root.right, level+1))
        
        all_keys = self.dic.keys()
        minKey = min(all_keys)
        maxKey = max(all_keys)
        
        ans = []
        
        for key in range(minKey, maxKey+1):
            ans.append(self.dic[key])
        return ans

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the no. of nodes

#Test Cases:
#[20, 8, 22, 5, 3, 4, 25, 10, 14]

#Link: https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1?page=1&category[]=Tree&sortBy=submissions
    