from createLinkedList import *

node = Node()

def middleNode(head):
    p, q = head, head
    while(q and q.next):
        p = p.next
        q = q.next.next
    return p

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1], [1, 2]

l1 = node.createLL([1])
ans1 = middleNode(l1)
node.printLL(ans1)

l2 = node.createLL([1, 2])
ans2 = middleNode(l2)
node.printLL(ans2)

l3 = node.createLL([1, 2, 3, 4, 5])
ans3 = middleNode(l3)
node.printLL(ans3)

l4 = node.createLL([1, 2, 3, 4, 5, 6])
ans4 = middleNode(l4)
node.printLL(ans4)

#Link: https://leetcode.com/problems/middle-of-the-linked-list/