from createLinkedList import *

node = Node()

class ListNode:
    def __init__(self, val, Next = None):
        self.val = val
        self.next = None 

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
            sum+=first.val
            first=first.next

        if(second):
            sum+=second.val
            second=second.next

        if(carry):
            sum+=carry

        digitsum=ListNode(sum%10, None)

        carry=sum//10
        cur.next=digitsum
        cur=cur.next
        
        
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





