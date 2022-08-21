from createLinkedList import *

node = Node()

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        newNode.prev = self.head
        self.head.next = newNode
        self.head = self.head.next
        

    def back(self, steps: int) -> str:
        while(self.head.prev and steps):
            self.head = self.head.prev
            steps -= 1
        return self.head.val

    def forward(self, steps: int) -> str:
        cur = self.head
        while(self.head.next and steps):
            self.head = self.head.next
            steps -= 1
        return self.head.val

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"], [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

#Link: https://leetcode.com/problems/design-browser-history/