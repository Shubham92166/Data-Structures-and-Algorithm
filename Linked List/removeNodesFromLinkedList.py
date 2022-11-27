from createLinkedList import *

ll = Node()

def removeNodes(head):
    cur = head
    stack = []
    newHead = None
    
    while cur:
        stack.append(cur)
        cur = cur.next
        
    while stack:
        node = stack.pop()
        if not newHead:
            newHead = node
        else:
            if node.val >= newHead.val:
                node.next = newHead
                newHead = node
    return newHead

#Complexity:
#Time: O(n)
#Space: O(n)
#Where n is the no. of nodes in the linked list

#Test Cases:
#[5,2,13,3,8], [1,1,1,1]

head = ll.createLL([5,2,13,3,8])
ll.printLL(removeNodes(head))

head = ll.createLL([1,1,1,1])
ll.printLL(removeNodes(head))

#Link: https://leetcode.com/problems/remove-nodes-from-linked-list/

