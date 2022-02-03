#Approach-1: Iterative:

def printReverse(head) :
    prev, cur = None, head
    while(cur):
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    while(prev):
        print(prev.data, end = ' ')
        prev = prev.next

#Complexity:
#Time: O(n)
#Space: O(1)
