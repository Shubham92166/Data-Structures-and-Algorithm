from createLinkedList import *

node = Node()

def partition(head, x):
    firstHead, secondHead = ListNode(-1), ListNode(-1)
    
    cur1 = firstHead
    cur2 = secondHead
    
    cur = head
    
    while cur:
        if cur.val < x:
            cur1.next = cur
            cur = cur.next
            cur1 = cur1.next
            cur1.next = None
            
        else:
            cur2.next = cur
            cur = cur.next
            cur2 = cur2.next
            cur2.next = None
    
    cur1.next = secondHead.next
    
    return firstHead.next

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1,4,3,2,5,2], 3
#[2,1], 2

ll1 = node.createLL([1,4,3,2,5,2])
node.printLL(partition(ll1, 3))

ll2 = node.createLL([2,1])
node.printLL(partition(ll2, 2))

#Link: https://leetcode.com/problems/partition-list/