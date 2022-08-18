from createLinkedList import * 

node = Node()

def pairSum(head):
    slow, fast = head, head.next
    
    while(fast and fast.next):
        slow, fast = slow.next, fast.next.next
    
    first, second=head, slow.next
    slow.next, prev, cur, max_sum, sum = None, None, second, 0, 0
    
    while(cur):
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    second = prev
    
    while(first and second):
        sum = first.val + second.val
        max_sum = max(sum, max_sum)
        first, second = first.next, second.next
        
    return max_sum

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[5,4,2,1], [4,2,2,3], [1,100000]

l1 = node.createLL([5,4,2,1])
print(pairSum(l1))

l2 = node.createLL([4,2,2,3])
print(pairSum(l2))

l3 = node.createLL([1,100000])
print(pairSum(l3))

#Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

