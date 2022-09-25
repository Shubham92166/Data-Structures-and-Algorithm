from createLinkedList import *

class MyCircularDeque:

    def __init__(self, k):
        self.k = k
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insertFront(self, value):
        newNode = ListNode(value)
        if self.size < self.k:
            nextNode = self.head.next
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = nextNode
            nextNode.prev = newNode
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value: int):
        newNode = ListNode(value)
        if self.size < self.k:
            prevNode = self.tail.prev
            prevNode.next = newNode
            newNode.prev = prevNode
            newNode.next = self.tail
            self.tail.prev = newNode
            self.size += 1
            return True
        else:
            return False
            
    def deleteFront(self):
        if self.size > 0:
            nextNode = self.head.next.next
            self.head.next = nextNode
            nextNode.prev = self.head
            self.size -= 1
            return True
        else:
            return False
    
    def deleteLast(self):
        if self.size > 0:
            prevNode = self.tail.prev.prev
            prevNode.next = self.tail
            self.tail.prev = prevNode
            self.size -= 1
            return True
        else:
            return False
        

    def getFront(self):
        if self.size > 0:
            return self.head.next.val
        else:
            return -1

    def getRear(self):
        if self.size > 0:
            return self.tail.prev.val
        else:
            return -1

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
        

    def isFull(self):
        if self.size == self.k:
            return True
        else:
            return False

#Test Cases:
#["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
#[[3], [1], [2], [3], [4], [], [], [], [4], []]

#Link: https://leetcode.com/problems/design-circular-deque/