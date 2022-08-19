#Approach: We split the linked list into two halves and then we reverse the second half. We keep comparing the the values of each node as
#long as they are equal we continue. If we find any mismath we stop the process and return False. If all nodes have same value then at the
#end, we return True. 
#In order to split the linked list into two halves, we use slow and fast pointer. Basically, we try to get the middle node of the linked
#list. We also maintain a prev variable to keep track of previous node before the middle node so that we can split the linked list by
#making the next of prev as Null

from createLinkedList import *

node = Node()

def isPalindrome(head):
    if not head.next:
        return True 
    
    slow = fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    nextNode = prev.next
    prev.next = None
    
    first = head
    second = reverseLL(nextNode)
    
    while first and second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True

def reverseLL(head):
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
#[1,2,2,1], [1,2], [1]

l1 = node.createLL([1,2,2,1])
print(isPalindrome(l1))

l2 = node.createLL([1,2])
print(isPalindrome(l2))

l3 = node.createLL([1])
print(isPalindrome(l3))

#Link: https://leetcode.com/problems/palindrome-linked-list/
