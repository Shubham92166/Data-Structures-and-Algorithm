from createLinkedList import *

node = Node()

def reverseEvenLengthGroups(head):
    k = 0
    slow, fast = head, head
    prev = None
    while fast:
        k += 1
        if k == 1:
            prev = slow
            slow, fast = slow.next, slow.next
            continue
        move = k
        length = 1
        while fast.next and move > 1:
            fast = fast.next
            move -= 1
            length += 1
        nextNode = fast.next
        fast.next = None
        
        if length % 2 == 0:
            rev = reverse(slow)
            prev.next = fast
            prev = slow
        else:
            prev.next = slow
            prev = fast
        
        slow, fast = nextNode, nextNode
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

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[5,2,6,3,9,1,7,3,8,4], [1,1,0,6], [1,1,0,6,5]

l1 = node.createLL([5,2,6,3,9,1,7,3,8,4])
res = reverseEvenLengthGroups(l1)
node.printLL(res)

l2 = node.createLL([1,1,0,6])
res = reverseEvenLengthGroups(l2)
node.printLL(res)

l3 = node.createLL([1,1,0,6,5])
res = reverseEvenLengthGroups(l3)
node.printLL(res)

#Link: https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

