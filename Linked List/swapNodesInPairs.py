from createLinkedList import *

node = Node()

def swapPairs(head):
    if not head or not head.next:
        return head
    
    #ListNode is given in the question to create new nodes

    dummy = ListNode(0, head)
    prev, cur = dummy, head
    while(cur and cur.next):
        second_node = cur.next
        remaining_nodes = cur.next.next
        second_node.next = cur
        prev.next = second_node
        cur.next = remaining_nodes
        prev = cur 
        cur = remaining_nodes

    return dummy.next

#link: https://leetcode.com/problems/swap-nodes-in-pairs/

#Test Case: [1,2,3,4], [1], []

#Complexity:
#Time: O(N)
#Space: O(1)

list1 = node.createLL([1,2,3,4])
res = swapPairs(list1)
node.printLL(res)

list2 = node.createLL([])
res = swapPairs(list2)
node.printLL(res)

list3 = node.createLL([1])
res = swapPairs(list3)
node.printLL(res)

#Link: https://leetcode.com/problems/swap-nodes-in-pairs/