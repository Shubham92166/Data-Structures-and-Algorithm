def swapPairs(self, head):
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

print(swapPairs([1,2,3,4]))
print(swapPairs([]))
print(swapPairs([1]))