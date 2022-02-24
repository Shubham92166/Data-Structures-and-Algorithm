from createLinkedList import *
node = Node()

def rotateRight(head, k):
    if not head:
        return head
    n = findLength(head)
    K = k%n
    if K == 0:
        return head
    
    count = 0 
    slow = fast = head
    while(K != 0 and count < K):
        fast = fast.next
        count += 1
    while(fast.next):
        slow = slow.next
        fast = fast.next
    newHead = slow.next 
    fast.next = head
    slow.next = None
    head = newHead
    return head

    
    
def findLength(head):
    count = 0
    while(head):
        count += 1
        head = head.next
    return count 

#Test cases: 
#[1,2,3,4,5], 2
#[0,1,2], 4
#[1,2,3,4], 0
#[], 3


#Complexity:
#Time: O(N)
#Space: O(1)

list1 = node.createLL([1,2,3,4,5])
res = rotateRight(list1, 2)
node.printLL(res)

list2 = node.createLL([])
res = rotateRight(list2, 3)
node.printLL(res)

list3 = node.createLL([1,2,3,4])
res = rotateRight(list3, 4)
node.printLL(res)

list4= node.createLL([1,2,3])
res = rotateRight(list4, 0)
node.printLL(res)