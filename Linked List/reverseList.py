#Approach-1: Iterative:

from createLinkedList import *

node = Node()

def printReverse(head) :
    prev, cur = None, head
    while(cur):
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    Node().printLL(prev)

def reverse(head):
    if not head or not head.next:
        return head
    smallHead = reverse(head.next)
    tail=head.next
    tail.next=head
    head.next=None
    return smallHead

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Case: [1,2,3,4], [], [1,2,3]

list1 = node.createLL([1,2,3,4])
print(printReverse(list1))

list2 = node.createLL([])
print(printReverse(list2))

list3 = node.createLL([1,2,3])
print(printReverse(list3))

ll = reverse(list2)

print(node.printLL(ll))
