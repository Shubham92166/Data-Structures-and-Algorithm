from createLinkedList import *

node = Node()

#Approach-1: Iterative

def findLengthIterative(head):
    count = 0
    cur = head
    while(cur):
        count+=1
        cur = cur.next
    return count

#Complexity:
#Time: O(N)
#Space: O(1)

#Approach-2: Recursive:

def findLengthRecursive(head):
    if head is None:
        return 0
    return 1+findLengthRecursive(head.next)

#Complexity:
#Time: O(n)
#Space: O(n) #space for stack

#Tese Case: [], [1,2,3], [1,2,3,4]

list1 = node.createLL([1,2,3,4])
print(findLengthIterative(list1))
print(findLengthRecursive(list1))

list2 = node.createLL([])
print(findLengthIterative(list2))
print(findLengthRecursive(list2))

list3 = node.createLL([1,2,3])
print(findLengthIterative(list3))
print(findLengthRecursive(list3))




