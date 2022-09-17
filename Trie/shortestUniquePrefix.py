class TrieNode:
    def __init__(self):
        self.hashmap = {}
        self.count = 1

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.ans = []

    def prefix(self, A):
        self.insert(A)
        self.findPrefix(A)
        return self.ans

    def insert(self, A):
        for word in A:
            self.insertHelper(self.root, word)

    def insertHelper(self, node, word):
        for char in word:
            if char not in node.hashmap:
                node.hashmap[char] = TrieNode()
                node = node.hashmap[char]
            else:
                node = node.hashmap[char]
                node.count += 1

    def findPrefix(self, A):
        for word in A:
            self.findPrefixHelper(self.root, word)
    
    def findPrefixHelper(self, node, word):
        for index in range(len(word)):
            node = node.hashmap[word[index]]
            if node.count == 1:
                self.ans.append(word[:index+1])
                break

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the no. of characters in all words

#Test Cases:
#["zebra", "dog", "duck", "dove"], ["apple", "ball", "cat"]


#Link: https://practice.geeksforgeeks.org/problems/shortest-unique-prefix-for-every-word/1

    




