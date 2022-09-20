class TrieNode:
    def __init__(self):
        self.hashmap = {}
        self.isEnd = False
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.ans = []
        
    def replaceWords(self, dictionary, sentence):
        self.insert(dictionary)
        sentence = sentence.split()
        self.search(sentence)
        return " ".join(self.ans)
        
    def insert(self, dictionary):
        for word in dictionary:
            self.insertHelper(word)
            
    def insertHelper(self, word):
        cur = self.root
        for char in word:
            if char not in cur.hashmap:
               cur.hashmap[char] = TrieNode()
            cur = cur.hashmap[char]
        cur.isEnd = True
    
    def search(self, sentence):
        for word in sentence:
            index = self.searchHelper(word)
            if index == -1:
                self.ans.append(word)
            else:
                self.ans.append(word[:index+1])

    def searchHelper(self, word):
        index = -1
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.hashmap:
                return index
            else:
                cur = cur.hashmap[word[i]]
                if cur.isEnd:
                    return i
        return index

#Complexity:
#Time: O(n*m + p*q)
#Space: O(n*m)
#where n is the length of longest word from dictionary and m is the length of dictionary
#p is the length of longest word from sentence and q is the length of sentence

#Test Cases:
#["cat","bat","rat"], "the cattle was rattled by the battery"
#["a","b","c"], "aadsfasf absbs bbab cadsfafs"

sol1 = Solution()

print(sol1.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))

sol2 = Solution()
print(sol2.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))