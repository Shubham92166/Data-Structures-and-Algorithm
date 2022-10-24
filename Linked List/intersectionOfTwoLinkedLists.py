from createLinkedList import *

node = Node()

def getIntersectionNode(headA, headB):
    nodesList1, nodesList2 = [], []
    
    cur = headA
    
    while cur:
        nodesList1.append(cur)
        cur = cur.next
        
    
    cur = headB
    
    while cur:
        nodesList2.append(cur)
        cur = cur.next
        
    i = len(nodesList1)-1
    j = len(nodesList2)-1
    
    prevMatch = ListNode(-1)
    
    while i >= 0 and j >= 0:
        if nodesList1[i] == nodesList2[j]:
            prevMatch = nodesList1[i]
            i -= 1
            j -= 1 
        else:
            break
    
    if prevMatch.val != -1:
        return prevMatch

#COmplexity:
#Time: O(m+n)
#Space: O(m+n)

#Test Cases:
#[4,1,8,4,5], [5,6,1,8,4,5]
#[1,9,1,2,4], [3,2,4]
#[2,6,4], [1,5]

#Link: https://leetcode.com/problems/intersection-of-two-linked-lists/