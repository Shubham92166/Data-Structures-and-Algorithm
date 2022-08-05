from createLinkedList import *
import math 

node = Node()

def mergeKLists(lists):
    if len(lists) == 0:
        return None
    dummy = ListNode(-math.inf, None)
    cur = dummy
    for l in lists:
        if l:
            cur = mergeList(cur, l)
    return cur.next

def mergeList(first, second):
    dummy = ListNode(0, None)
    cur = dummy
    while(first and second):
        if(first.val <= second.val):
            cur.next, first = first, first.next
        else:
            cur.next, second = second, second.next
        cur = cur.next
    if(second):
        cur.next = second
    elif(first):
        cur.next = first
    return dummy.next

#Complexity:
#Time: O(n(k^2))
#Space: O(1)

#Test Cases:
#[[1,4,5],[1,3,4],[2,6]]
#[[2],[],[-1]]
#[]
