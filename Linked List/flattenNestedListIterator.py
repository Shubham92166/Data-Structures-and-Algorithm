class NestedIterator:
    def __init__(self, nestedList):
        self.nestedList = nestedList
        self.count = 0
        self.output = []
        self.helper(self.nestedList)
        
    def helper(self, nestedList):
        for val in nestedList:
            if val.isInteger():
                self.output.append(val.getInteger())
            else:
                self.helper(val.getList())        
    
    def next(self):
        if self.count < len(self.output):
            ans = self.output[self.count]
            self.count += 1
            return ans
        
    
    def hasNext(self):
        if self.count < len(self.output):
            return True
        else:
            return False

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[[1,1],2,[1,1]], [1,[4,[6]]]

#Link: https://leetcode.com/problems/flatten-nested-list-iterator/