class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
        if not head:
            return
    
        cur = head
        while cur:
            node = Node(cur.val)
            node.next = cur.next
            cur.next = node
            cur = cur.next.next
        
        cur1 = head
        cur2 = head.next
        
        while cur1:
            if cur1.random:
                cur2.random =  cur1.random.next
            
            cur1 = cur1.next.next
            
            if cur2 and cur2.next:
                cur2 = cur2.next.next
        
        cur = head
        dummy = Node(-1)
        newList = dummy
        while cur and cur.next:
            newList.next = cur.next
            newList = newList.next
            cur = cur.next.next
        return dummy.next   

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[[7,null],[13,0],[11,4],[10,2],[1,0]], [[1,1],[2,1]], [[3,null],[3,0],[3,null]]

#Link: https://leetcode.com/problems/copy-list-with-random-pointer/