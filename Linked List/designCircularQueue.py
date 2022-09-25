from createLinkedList import *

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.size = 0   

    def enQueue(self, value: int):
        newNode = ListNode(value)
        if self.size == 0:
            
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = self.tail
            self.tail.prev = newNode
            
            self.size += 1
            return True

        elif self.size < self.k:
            
            prevNode = self.tail.prev
            prevNode.next = newNode
            newNode.prev = prevNode
            newNode.next = self.tail
            self.tail.prev = newNode
            
            self.size += 1
            return True
        else:
            return False

    def deQueue(self):
        if self.size == 0:
            return False
        else:
            self.size -= 1
            self.head = self.head.next
            return True

    def Front(self):
        if self.size > 0:
            return self.head.next.val
        else:
            return -1

    def Rear(self):
        if self.size > 0:
            return self.tail.prev.val
        else:
            return -1
        
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
        
    def isFull(self):
        if self.size == self.k:
            return True
        else:
            return False

#Test Cases:
#["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
#[[3], [1], [2], [3], [4], [], [], [], [4], []]

#Link: https://leetcode.com/problems/design-circular-queue/