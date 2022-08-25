class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = []

    def push(self, x):
        self.stack.append(x)
        self.storeMin(x)
        
    def pop(self):
        if self.stack:
            ele = self.stack.pop()
            if self.minValue and self.minValue[-1] == ele:
                self.minValue.pop()
            return ele
        else:
            return -1
        
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1
      
    def storeMin(self, x):
        if not self.minValue:
            self.minValue.append(x)
        else:
            if x <= self.minValue[-1]:
                self.minValue.append(x)
        
    def getMin(self):
        if self.minValue:
            return self.minValue[-1]
        else:
            return -1

#Complexity:
#Time: O(q)
#Space: O(q)
#where q is the no. of queries

#Test Cases:
#["MinStack","push","push","push","getMin","pop","top","getMin"], [[],[-2],[0],[-3],[],[],[],[]]

#Link: https://leetcode.com/problems/min-stack/


