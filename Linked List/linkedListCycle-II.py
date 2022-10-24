def detectCycle(head):
    slow = head
    fast = head
    
    if(not head or not head.next):
        return None
    
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            break
    if(not fast or not fast.next):
        return None
    
    slow = head
    while(slow != fast):
        slow = slow.next
        fast = fast.next
    return slow

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[3,2,0,-4], [1,2], [1]

#Link: https://leetcode.com/problems/linked-list-cycle-ii/