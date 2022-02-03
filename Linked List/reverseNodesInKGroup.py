def reverseKGroup(self, head, k):
    slow = fast = head 

    #ListNode class is provided in the question to create new nodes

    dummy = ListNode(0, head)
    prev, i = dummy, 1
    while(fast and fast.next):
        if i%k != 0:
            fast = fast.next 
            i+=1
        else:
            remaining_nodes = fast.next
            reversed_list = self.reverse(slow, fast.next)
            prev.next = reversed_list
            slow.next = remaining_nodes
            prev = slow
            slow = fast = remaining_nodes
            i+=1
            
    if i%k == 0:
        prev.next = self.reverse(slow, fast.next)
    return dummy.next
    
def reverse(self, slow, fast):
    cur, prev = slow, None
    while(cur!=fast):
        next_node = cur.next
        cur.next = prev 
        prev = cur
        cur = next_node
    return prev
        