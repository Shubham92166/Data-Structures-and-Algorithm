class TrieNode:
    def __init__(self):
        self.children = [None] * 2
    
class Solution:
    def solve(self, nums):
        root = TrieNode()
        
        for num in nums:
            node = root
            for pos in range(31, -1, -1):
                bit = (num >> pos) & 1
                
                if node.children[bit] == None:
                    node.children[bit] = TrieNode()
                    
                node = node.children[bit]
        
        maxXor = 0
        
        for num in nums:
            node = root
            val = 0
            for pos in range(31, -1, -1):
                bit = (num >> pos) & 1
                if bit == 1:
                    child = 0
                else:
                    child = 1
                    
                if node.children[child]:
                    val |=  1 << pos
                    node = node.children[child]
                else:
                    node = node.children[bit]
                
            maxXor = max(maxXor, val)
        return maxXor

#Complexity:
#Time: O(n logk)
#Space: O(n  logk)
#where k is the largest number and n is the size of the array

#Test Cases:
#[1, 2, 3, 4, 5], [5, 17, 100, 11]

sol = Solution()
print(sol.solve([1, 2, 3, 4, 5]))
print(sol.solve([5, 17, 100, 11]))
