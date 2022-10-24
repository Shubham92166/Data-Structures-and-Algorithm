from createLinkedList import *

node = Node()

def removeDuplicates(head):
    visitedNodes = set()
    cur = head
    dummy = ListNode(-1)
    visited = []
    while cur:
        if cur.val not in visitedNodes:
            visited.append(cur.val)
            visitedNodes.add(cur.val)
        cur = cur.next
    
    cur = dummy
    i = 0

    while i < len(visited):
        cur.next = ListNode(visited[i])
        i += 1
        cur = cur.next
    
    return dummy.next

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[5,2,2,4], [2,2,2,2,2]

l1 = node.createLL([5,2,2,4])
node.printLL(removeDuplicates(l1))

l2 = node.createLL([2,2,2,2,2])
node.printLL(removeDuplicates(l2))

#Link: https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1
