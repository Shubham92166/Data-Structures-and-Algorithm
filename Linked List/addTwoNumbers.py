'''
Approach:
We traverse both the linked lits as long as any one of them has untraversed node present. We create dummy node which would represent the
head of the new linked list which would represent our sum. While traversing, we take the sum of current node from both the linked list
and if sum is greater than or equals to 10 then we take the unit digit and create a new node and attach it to the dummy node. The number
left after taking the unit digit is assigned to a variable called carry. This carry value will get added to the next node sum. We repeat
this process as long as we have atleast one node we have non zero carry. At the end, we return the next node of dummy which would
represent the sum as a linked list.
'''

from createLinkedList import *

node = Node()

def addTwoNumbers(l1, l2):
    if(not l1 and not l2):
        return None

    elif(not l1 and l2):
        return l2

    elif(l1 and not l2):
        return l1

    dummy = ListNode(0, None)
    cur = dummy
    first = l1
    second = l2
    carry = 0

    while(first or second or carry):
        sum = 0
        
        if(first):
            sum += first.val
            first = first.next

        if(second):
            sum += second.val
            second=second.next

        if(carry):
            sum += carry

        digitsum = ListNode(sum%10, None)

        carry = sum//10
        cur.next = digitsum
        cur = cur.next
        
        
    return dummy.next

#Complexity:
#Time: O(n+m) 
#Space: O(n+m)
#where n is the length of l1 and m is the length of l2

#Test Cases:
#[2,4,3], [5,6,4]
#[0], [0]
#[9,9,9,9,9,9,9], [9,9,9,9]
#[5], [5]

l1 = node.createLL([2,4,3])
l2 = node.createLL([5,6,4])
res = addTwoNumbers(l1, l2)
node.printLL(res)

l1 = node.createLL([0])
l2 = node.createLL([0])
res = addTwoNumbers(l1, l2)
node.printLL(res)

l1 = node.createLL([9,9,9,9,9,9,9])
l2 = node.createLL([9,9,9,9])
res = addTwoNumbers(l1, l2)
node.printLL(res)

l1 = node.createLL([5])
l2 = node.createLL([5])
res = addTwoNumbers(l1, l2)
node.printLL(res)

#Link: https://leetcode.com/problems/add-two-numbers/





