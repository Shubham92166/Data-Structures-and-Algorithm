from createLinkedList import *

node = Node()

def removeNthFromEnd(head, n):
    if head is None or head.next is None:
        return None

    slow = fast = head

    for i in range(n):
        fast = fast.next

    if(not fast and slow is head):
        return slow.next

    while(fast.next):
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head

#Complexity:
#Time: O(n)
#Space O(1)

#Test Cases:
#[1,2,3,4,5], 2
#[1], 1
#[1,2], 1

l1 = node.createLL([1, 2, 3, 4, 5])
res1 = removeNthFromEnd(l1, 2)
node.printLL(res1)

l2 = node.createLL([1])
res2 = removeNthFromEnd(l2, 1)
node.printLL(res2)

l3 = node.createLL([1, 2])
res3 = removeNthFromEnd(l3, 1)
node.printLL(res3)

l4 = node.createLL([1, 2])
res4 = removeNthFromEnd(l4, 2)
node.printLL(res4)

#Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/