from createLinkedList import *

node = Node()

def mergeTwoLists(list1, list2):
    first = list1
    second = list2
    dummy = ListNode(0) #ListNode is the class given in the question
    cur = dummy
    while(first and second):
        if(first.val <= second.val):
            cur.next = first
            first = first.next
        else:
            cur.next = second
            second = second.next
        cur = cur.next
    if(second):
        cur.next = second
    elif(first):
        cur.next = first
    return dummy.next

#Test Case: [1,2,4], [1,3,4]

#Complexity:
#Time: O(m+n)
#Space: O(1)

list1 = node.createLL([1,2,4])
list2 = node.createLL([1,3,4])
res = mergeTwoLists(list1, list2)
node.printLL(res)

#Link: https://leetcode.com/problems/merge-two-sorted-lists/        