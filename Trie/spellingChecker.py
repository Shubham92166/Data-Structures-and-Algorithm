class TrieNode:
    def __init__(self):
        self.hashmap = {}
        self.isEnd = False

class Solution:
    def __init__(self):
        self.ans = []
        self.root = TrieNode()
   
    def solve(self, A, B):
        self.insert(A)
        self.search(B)
        return self.ans
    
    def insert(self, A):
        for word in A:
            self.insertHelper(word)
    
    def search(self, B):
        for word in B:
            self.searchHelper(word)
    
    def insertHelper(self, word):
        cur = self.root
        for char in word:
            if char in cur.hashmap:
                cur = cur.hashmap[char]
            else:
                cur.hashmap[char] = TrieNode()
                cur = cur.hashmap[char]
        cur.isEnd = True
    
    def searchHelper(self, word):
        cur = self.root
        for char in word:
            if char in cur.hashmap:
                cur = cur.hashmap[char]
            else:
                break
        if cur.isEnd:
            self.ans.append(1)
        else:
            self.ans.append(0)

#Link: https://www.geeksforgeeks.org/spell-checker-using-trie/
    

    


