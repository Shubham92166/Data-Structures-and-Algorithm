from createLinkedList import *

node = Node() #to import create and print methods from different class for LL

def reverseKGroup(head, k):
    slow, fast = head, head
    prev = None
    while fast:
        K = k
        while fast.next and K > 1:
            fast = fast.next
            K -= 1
            
        if K > 1:
            prev.next = slow
            return head
        
        nextNode = fast.next
        fast.next = None

        rev = reverse(slow)

        if not prev:
            head = fast
        else:
            prev.next = fast
        
        prev = slow
        slow = nextNode
        fast = nextNode
    return head

def reverse(head):
    prev = None
    cur = head
    while cur:
        nextNode = cur.next
        cur.next = prev
        prev = cur
        cur = nextNode
    return prev

#Test Case: 
#[1,2,3,4,5], 2
#[1,2,3,4,5], 3
#[1,2], 4

#Complexity:
#Time: O(n)
#Space: O(1)

list = node.createLL([1,2,3,4,5])

res = reverseKGroup(list, 2)
node.printLL(res)

list = node.createLL([1,2,3,4,5])
res = reverseKGroup(list, 3)
node.printLL(res)

#Link: https://leetcode.com/problems/reverse-nodes-in-k-group/