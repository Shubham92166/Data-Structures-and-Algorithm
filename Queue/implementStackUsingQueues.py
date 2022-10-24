from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x):
        self.q.append(x)


    def pop(self):
        return self.q.pop()

    def top(self):
        return self.q[-1]

    def empty(self):
        if not self.q:
            return True
        return False

#Test Cases:
#["MyStack", "push", "push", "top", "pop", "empty"]
#[[], [1], [2], [], [], []]

#Link: https://leetcode.com/problems/implement-stack-using-queues/