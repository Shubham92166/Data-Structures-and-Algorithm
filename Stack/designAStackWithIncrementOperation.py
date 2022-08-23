class CustomStack:

    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize
        self.length = 0

    def push(self, x):
        if self.length < self.maxSize:
            self.stack.append(x)
            self.length += 1

    def pop(self):
        
        if self.stack:
            ele = self.stack.pop()
            self.length -= 1
            return ele
        return -1

    def increment(self, k, val):
        i = 0
        while i < len(self.stack) and i < k:
            self.stack[i] += val
            i += 1

#Complexity:
#Time: O(No. of operations)
#Space: O(maxSize)

#Test Cases:
#["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"], [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]

#Link: https://leetcode.com/problems/design-a-stack-with-increment-operation/