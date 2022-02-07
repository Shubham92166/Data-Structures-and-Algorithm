from createLinkedList import *

def mergeTwoLists(list1, list2):
    first = list1
    second = list2
    dummy = ListNode(0) #ListNode is the class given in the question
    cur = dummy
    while(first.next and second.next):
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

list1 = Node().createLL([1,2,4])
#printLL(list1)

list2 = Node().createLL([1,3,4])
#printLL(list2)

res = mergeTwoLists(list1, list2)
Node().printLL(res)
        