from createLinkedList import *

node = Node()

def nextLargerNodes(head):
    if not head.next:
        return [0]
    ll = reverseLL(head)
    stack = []
    ans = []
    cur = ll
    while cur:
        while stack and stack[-1] <= cur.val:
            stack.pop()
        
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(0)
        
        stack.append(cur.val)
        cur = cur.next
    return ans[::-1]
        
            
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
#Space: O(n)

#Test Cases:
#[2,1,5], [2,7,4,3,5]

l1 = node.createLL([2,1,5])
print(nextLargerNodes(l1))

l2 = node.createLL([2,7,4,3,5])
print(nextLargerNodes(l2))

#Link: https://leetcode.com/problems/next-greater-node-in-linked-list/