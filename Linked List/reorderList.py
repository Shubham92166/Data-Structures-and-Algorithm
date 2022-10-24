from createLinkedList import * 

node = Node()

def reorderList(head):      
    dummy = ListNode(-1)
    cur = dummy
    
    if(not head.next):
        return head
    slow = fast = head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    
    nextNode = slow.next
    slow.next = None
    
    first = head
    second = reverseLL(nextNode)

    while(first and second):
        cur.next = first
        first = first.next
        cur = cur.next
        
        cur.next = second
        second = second.next 
        cur = cur.next 
        
    while first:
        cur.next = first
        first = first.next
        cur = cur.next
    
    while second:
        cur.next = second
        second = second.next
        cur = cur.next
    
    return dummy.next
               
def reverseLL(head):
    prev = None
    cur = head
    while(cur):
        nextNode = cur.next
        cur.next = prev
        prev = cur
        cur = nextNode
    return prev

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1], [1,2,3,4,5], [1, 2, 3, 4] 

l1 = node.createLL([1, 2, 3, 4])
res1 = reorderList(l1)
node.printLL(res1)

l2 = node.createLL([1, 2, 3, 4, 5])
res2 = reorderList(l2)
node.printLL(res2)

l3 = node.createLL([1])
res3 = reorderList(l3)
node.printLL(l3)

#Link: https://leetcode.com/problems/reorder-list/
