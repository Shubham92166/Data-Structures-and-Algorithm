import imp
from createLinkedList import *

node = Node()

def solve(head):
    if not head or not head.next:
        return None
    
    slow = fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    prev.next = slow.next
    return head

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1,3,4,7,1,2,6], [1,2,3,4], [2,1]

l1 = node.createLL([1,3,4,7,1,2,6])
res1 = solve(l1)
node.printLL(res1)

l2 = node.createLL([1,2,3,4])
res2 = solve(l2)
node.printLL(res2)

l3 = node.createLL([2,1])
res3 = solve(l3)
node.printLL(res3)

#Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/