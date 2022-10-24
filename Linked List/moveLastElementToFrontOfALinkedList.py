from createLinkedList import *

ll = Node()

def moveToFront(head):    
    if not head.next:
        return head
        
    cur = head
    while cur.next.next:
        cur = cur.next
    
    lastNode = cur.next
    cur.next = None
    lastNode.next = head
    head = lastNode
    
    return head

#Complexity:
#Time: O(n)
#Space: O(1)
#where n is the length of the linked list

#Test Cases:
#[2], [2,5,6,2,1]

head = ll.createLL([2])
ll.printLL(moveToFront(head))

head = ll.createLL([2,5,6,2,1])
ll.printLL(moveToFront(head))

#Link: https://practice.geeksforgeeks.org/problems/move-last-element-to-front-of-a-linked-list/1