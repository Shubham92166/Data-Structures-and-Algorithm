from createLinkedList import *

node = Node()

def reverse(head, k):
    fast = head
    for i in range(k-1):
        fast = fast.next
    head1 = head
    head2 = fast.next
    fast.next = None

    rhead1 = reverseLL(head1)
    rhead2 = reverseLL(head2)
    head.next = rhead2
    head = rhead1
    return rhead1
    
    
def reverseLL(head):
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1,2,3,4,5], 2
#[1,2,4,3], 3

h1 = node.createLL([1,2,3,4,5])
h2 = node.createLL([1,2,4,3])

ans1 = reverse(h1, 2)
node.printLL(ans1)

ans2 = reverse(h2, 3)
node.printLL(ans2)


