class TrieNode:
    def __init__(self):
        self.hashmap = {}
        self.count = 1

class Solution:
    
    def solve(self, A, B):
        self.root = TrieNode()
        self.ans = []
        for index in range(len(A)):
            if A[index] == 0:
                self.addContact(B[index])
            else:
                self.findContact(B[index])
        return self.ans

    def addContact(self, name):
        cur = self.root

        for char in name:
            if char in cur.hashmap:
                cur = cur.hashmap[char]
                cur.count += 1
            else:
                cur.hashmap[char] = TrieNode()
                cur = cur.hashmap[char]
    
    def findContact(self, name):
        cur = self.root
        total = 0
        for char in name:
            if char in cur.hashmap:
                cur = cur.hashmap[char]
                total = cur.count
            else:
                total = 0
                break
        self.ans.append(total)

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the no. of characters in all the words

#Test Cases:
#[0, 0, 1, 1], ["hack", "hacker", "hac", "hak"]
#[0, 1], ["abcde", "abc"]

sol = Solution()
print(sol.solve([0, 0, 1, 1], ["hack", "hacker", "hac", "hak"]))
print(sol.solve([0, 1], ["abcde", "abc"]))


