from createLinkedList import *

node = Node()

#Approach-1: Using Recursion

count = 0
def findNodeRecursive(head, n) :
	#Your code goes here
    global count
    if(head == None):
        return -1
    if(head.val==n):
        return count+1
    count+=1
    return findNodeRecursive(head.next, n)

#Complexity: 
#Time: O(n)
#Space: O(n)

#Approach-2: Iterative

def findNodeIterative(head, n) :
    if head is None:
        return -1
    cur = head
    count = 0
    
    while(cur):
        if(cur.val != n):
            count+=1
            cur =cur.next
        elif(cur.val == n):
            return count
    return -1

#Complexity: 
#Time: O(n)
#Space: O(1)

#Test Case:
# [], 4
#[1,2,3], 2,
#[1,2,3,4], 7
list1 = node.createLL([])
print(findNodeIterative(list1, 4))
print(findNodeRecursive(list1, 4))

list2 = node.createLL([1,2,3])
print(findNodeIterative(list2, 2))
print(findNodeRecursive(list2, 2))

list3 = node.createLL([1,2,3,4])
print(findNodeIterative(list3, 7))
print(findNodeRecursive(list3, 7))

