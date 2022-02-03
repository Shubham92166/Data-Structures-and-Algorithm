#Approach-1: Iterative

def length(head) :
    count = 0
    cur = head
    while(cur):
        count+=1
        cur = cur.next
    return count

#Complexity:
#Time: O(N)
#Space: O(1)



