from createLinkedList import *

node = Node()

def removeNthFromEnd(head, n):
    if head is None or head.next is None:
        return None
    p=head
    q=head
    for i in range(n):
        p=p.next
    if(not p and q is head):
        return q.next
    while(p.next):
        p=p.next
        q=q.next
    q.next=q.next.next
    del q
    return head

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1,2], 2
#[1,2,3,4,5], 2
#[1,2], 1
#[1], 1

l1 = node.createLL([1,2])
node.printLL(removeNthFromEnd(l1, 2))

l2 = node.createLL([1,2,3,4,5])
node.printLL(removeNthFromEnd(l2, 2))

l3 = node.createLL([1])
node.printLL(removeNthFromEnd(l3, 1))

l4 = node.createLL([1, 2])
node.printLL(removeNthFromEnd(l4, 1))

#Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
