from createLinkedList import *

node = Node()

def deleteEveryNNodes(head, m, n):
    if not head : return head

    cur = head
    
    if m == 0: return None
    if n == 0: return head
    
    while(cur and cur.next):
        mCount, nCount, mNode, nNode = 0, 0, None, None
        
        while(cur and cur.next and mCount < m):
            mCount, mNode, cur = mCount+1, cur, cur.next
        
        while(cur and cur.next and nCount < n):
            nCount, nNode, cur = nCount+1, cur, cur.next
        
        mNode.next = nNode.next if nCount == n else None
    return head

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1, 2, 3, 4, 5, 6, 7, 8], 2, 2
#[10, 20, 30, 40, 50, 60], 0, 1 
#[1, 2, 3, 4, 5, 6, 7, 8], 2, 3

l1 = node.createLL([1, 2, 3, 4, 5, 6, 7, 8])
node.printLL(deleteEveryNNodes(l1, 2, 2))

l2 = node.createLL([10, 20, 30, 40, 50, 60])
node.printLL(deleteEveryNNodes(l2, 0, 1))

l3 = node.createLL([1, 2, 3, 4, 5, 6, 7, 8])
node.printLL(deleteEveryNNodes(l3, 2, 3))

#Link: https://www.geeksforgeeks.org/delete-n-nodes-after-m-nodes-of-a-linked-list/


        

