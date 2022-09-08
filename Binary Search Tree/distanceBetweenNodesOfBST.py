class Solution:
    def __init__(self):
        self.count1 = 0
        self.count2 = 0
        self.lca = -1

    def solve(self, A, B, C):
        
        self.findLCA(A, B, C)
        self.findDistance(self.lca, B, True)
        self.findDistance(self.lca, C, False)
        return self.count1 + self.count2

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) in worst can be O(n) and n is the number of nodes

#Link: https://www.geeksforgeeks.org/shortest-distance-between-two-nodes-in-bst/