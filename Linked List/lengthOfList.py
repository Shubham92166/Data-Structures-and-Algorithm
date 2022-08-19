from createLinkedList import *

node = Node()

#Approach-1: Iterative

#We traverse through the linked list and increment the count. 

def findLengthIterative(head):
    count = 0
    cur = head
    while(cur):
        count += 1
        cur = cur.next
    return count

#Complexity:
#Time: O(N)
#Space: O(1)

#Approach-2: Recursive:

#We call the function recursively and add 1 to the result. After hitting the base case, it will return 0 and thus, we will get the 
#length of the linked list

def findLengthRecursive(head):
    if head is None: #Base case
        return 0
    return 1 + findLengthRecursive(head.next)

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

#Link: https://www.geeksforgeeks.org/find-length-of-a-linked-list-iterative-and-recursive/


