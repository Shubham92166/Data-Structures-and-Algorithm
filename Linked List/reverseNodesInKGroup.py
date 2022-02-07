from createLinkedList import *

masterObj = Node() #to import create and print methods from different class for LL

def reverseKGroup(head, k):
    slow = fast = head 

    #ListNode class is provided in the question to create new nodes

    dummy, dummy.next = ListNode(0, head), head
    prev, counter = dummy, 1
    while(fast and fast.next):
        if counter%k != 0:
            fast = fast.next 
        else:
            remaining_nodes = fast.next
            reversed_list = reverse(slow, fast.next)
            prev.next = reversed_list
            slow.next = remaining_nodes
            prev = slow
            slow = fast = remaining_nodes
        counter+=1
            
    if counter%k == 0:
        prev.next = reverse(slow, fast.next)
    return dummy.next

 #Method to reverse k group nodes
    
def reverse(slow, fast):
    cur, prev = slow, None
    while(cur!=fast):
        next_node = cur.next
        cur.next = prev 
        prev = cur
        cur = next_node
    return prev

#Test Case: 
#[1,2,3,4,5], 2
#[1,2,3,4,5], 3
#[1,2], 4

#Complexity:
#Time: O(n)
#Space: O(1)

list = masterObj.createLL([1,2,3,4,5])

res = reverseKGroup(list, 2)
masterObj.printLL(res)

list = masterObj.createLL([1,2,3,4,5])
res = reverseKGroup(list, 3)
masterObj.printLL(res)

list2 = masterObj.createLL([1,2])
#masterObj.printLL(list2)
res = reverseKGroup(list2, 4)
masterObj.printLL(res)