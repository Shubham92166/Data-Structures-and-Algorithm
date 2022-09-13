class TrieNode:
    def __init__(self):
        self.hashmap = {}
        self.isEnd = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str):
        self.insertHelper(self.root, word)

    def search(self, word: str) -> bool:
        return self.searchHelper(self.root, word)
        

    def startsWith(self, prefix: str):
        return self.startsWithHelper(self.root, prefix)
    
    def insertHelper(self, cur, word):
        node = None
        for char in word:
            if char not in cur.hashmap:
                node = TrieNode()
                cur.hashmap[char] = node
                cur = node
            else:
                cur = cur.hashmap[char]
                    
        cur.isEnd = True
        
    def searchHelper(self, cur, word):
        node = None
        for char in word:
            if char not in cur.hashmap:
                return False
            else:
                cur = cur.hashmap[char]
                node = cur
                
        if cur.isEnd:
            return True
        return False
    
    def startsWithHelper(self, cur, word):
        for char in word:
            if char not in cur.hashmap:
                return False
            else:
                cur = cur.hashmap[char]
        return True

#Test Cases:
#["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
#[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

#Link: https://leetcode.com/problems/implement-trie-prefix-tree/