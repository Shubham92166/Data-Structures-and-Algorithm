from createLinkedList import *
node = Node()

def sortList(head):
    if(not head or not head.next):
        return head
    first = head
    middle = findMiddle(head)
    second = middle.next
    middle.next = None
    first = sortList(first)
    second = sortList(second)
    return mergeList(first, second)
    

def mergeList(left, right):
    if not left:
        return right
    if not right:
        return left
    dummy = ListNode(0, None)
    cur = dummy
    while(left and right):
        if left.val <= right.val:
            cur.next = left
            left = left.next
        else:
            cur.next = right
            right = right.next
        cur = cur.next
    if left:
        cur.next = left
    elif right:
        cur.next = right
    return dummy.next

def findMiddle(head):
    slow, fast, prev = head, head, None
    while(fast and fast.next):
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    return prev
    
#Complexity:
#Time: O(nlog n)
#Space: O(log n)

#Test Cases:
#[4,2,1,3], [-1,5,3,4,0], []

l1 = node.createLL([4,2,1,3])
res = sortList(l1)
node.printLL(res)

l2 = node.createLL([-1,5,3,4,0])
res = sortList(l2)
node.printLL(res)

l3 = node.createLL([])
res = sortList(l3)
node.printLL(res)

#Link: https://leetcode.com/problems/sort-list/