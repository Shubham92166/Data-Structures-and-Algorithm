def hasCycle(head):
    slow = fast = head
    if not head or not head.next:
        return False
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            return True
    return False

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[3,2,0,-4], [1,2], [1]

#Link: https://leetcode.com/problems/linked-list-cycle/