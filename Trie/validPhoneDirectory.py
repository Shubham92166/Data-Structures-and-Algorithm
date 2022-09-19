class TrieNode:
    def __init__(self):
        self.hashmap = {}
        self.count = 1

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def solve(self, A):
        return self.insert(A)

    def insert(self, A):
        for number in A:
            ans = self.insertHelper(number)
            if ans == 0:
                return 0
        return 1
    
    def insertHelper(self, number):
        cur = self.root
        for char in number:
            if char in cur.hashmap:
                return 0
            else:
                cur.hashmap[char] = TrieNode()
                cur = cur.hashmap[char]
        return 1

#Test Cases:
#["1234", "2342", "567"], ["00121", "001"]

sol = Solution()

print(sol.solve(["1234", "2342", "567"]))
print(sol.solve(["00121", "001"]))
