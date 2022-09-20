class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        self.stack1.append(x)
        

    def pop(self):
        if not self.stack2 and self.stack1:
            self.moveElements()
        return self.stack2.pop()
            
        

    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        else:
            return self.stack1[0]

    def empty(self):
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False
    
    def moveElements(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

#Complexity:
#Time: O(q)
#Space: O(q)

#Test Cases:
#["MyQueue", "push", "push", "peek", "pop", "empty"]
#[[], [1], [2], [], [], []]

#Link: https://leetcode.com/problems/implement-queue-using-stacks/