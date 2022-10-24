from audioop import add
from createLinkedList import *

node = Node()

def addTwoNumbers(l1, l2):
    first = l1
    second = l2
    carry = 0
    cur = None
    fl = []
    sl = []
    while(first or second):
        if first:
            fl.append(first.val)
            first = first.next
        if(second):
            sl.append(second.val)
            second = second.next
    while(len(fl) != 0 or len(sl) != 0 or carry):
        ele1,ele2 = 0,0
        sum = 0
        if(len(fl)!=0):
            ele1 = fl.pop()
            sum += ele1
        if(len(sl) != 0):
            ele2 = sl.pop()
            sum += ele2
        if(carry):
            sum += carry
        carry = sum//10
        digit = ListNode(sum%10, None)
        if(not cur):
            cur = digit
        else:
            digit.next = cur
            cur = digit
    return cur

#Complexity:
#Time: O(n+m)
#Space: O(n+m)

#Test Cases:
#[7,2,4,3], [5,6,4]
#[2,4,3], [5,6,4]
#[0], [0]

l1 = node.createLL([7,2,4,3])
l2 = node.createLL([5,6,4])
res = addTwoNumbers(l1, l2)
node.printLL(res)

l3 = node.createLL([2,4,3])
l4 = node.createLL([5,6,4])
res = addTwoNumbers(l3, l4)
node.printLL(res)

l5 = node.createLL([0])
l6 = node.createLL([0])
res = addTwoNumbers(l5, l6)
node.printLL(res)

#Link: https://leetcode.com/problems/add-two-numbers-ii/