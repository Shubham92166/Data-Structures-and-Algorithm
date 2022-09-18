class TrieNode:
    def __init__(self):
        self.hashmap = {}
        self.count = 1
        
class Solution:
    def sumPrefixScores(self, words):
        self.root = TrieNode()
        self.ans = []
        
        for word in words:
            self.insert(word)
        
        for word in words:
            self.search(word)
        
        return self.ans
    
    def insert(self, word):
        cur = self.root
        for char in word:
            
            if char in cur.hashmap:
                cur = cur.hashmap[char]
                cur.count += 1 
                
            else:
                cur.hashmap[char] = TrieNode()
                cur = cur.hashmap[char]
         
    def search(self, word):
        cur = self.root
        sum = 0
        
        for char in word:
            if char in cur.hashmap:          
                cur = cur.hashmap[char]
                sum += cur.count
            else:
                break
        self.ans.append(sum)
        
#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the no. of characters in all words

#Test Cases:
#["abc","ab","bc","b"], ["abcd"]

sol = Solution()
print(sol.sumPrefixScores(["abc","ab","bc","b"]))
print(sol.sumPrefixScores(["abcd"]))

#Link: https://leetcode.com/problems/sum-of-prefix-scores-of-strings/