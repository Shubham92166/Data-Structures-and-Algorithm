from createLinkedList import *

node = Node()

def swapNodes(head, pos1, pos2) :
    firstPrev, first = searchByPosition(head, pos1)
    secondPrev, second = searchByPosition(head, pos2)
    
    #Special case when both the nodes are adjacent to each other
    
    if(firstPrev and secondPrev and second == first.next):
        temp = second.next
        firstPrev.next = second
        second.next = secondPrev
        secondPrev.next = temp
        return head

    temp = second.next
    second.next = first.next
    first.next = temp
    
    #if the first node is the head node

    if(not firstPrev):
        head = second
        secondPrev.next = first
    
    #if the second node is the head node

    elif(not secondPrev):
        head = first
        firstPrev.next = second
    
    #if both the nodes are internal nodes but not adjacent to each other

    elif(firstPrev and secondPrev):
        firstPrev.next = second
        secondPrev.next = first
    return head
    
#for searching the nodes by position

def searchByPosition(head, pos):
        count, prev = 0, None
        while(head and count<pos):
            prev = head
            count += 1
            head = head.next
        return prev, head

#Test Case:
#[3, 4, 5, 2, 6, 1, 9]   3, 4
#[10, 20, 30, 40]  1, 2
#[70, 80, 90, 25, 65, 85, 90]   0, 6

list1 = node.createLL([3, 4, 5, 2, 6, 1, 9])
res = swapNodes(list1, 3,4)
node.printLL(res)

list2 = node.createLL([10, 20, 30, 40])
res = swapNodes(list2, 1, 2)
node.printLL(res)

list3 = node.createLL([70, 80, 90, 25, 65, 85, 90])
res = swapNodes(list3, 0, 6)
node.printLL(res)