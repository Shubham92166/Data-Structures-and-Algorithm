class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr

def addPolynomial(poly1, poly2):
    cur1 = poly1
    cur2 = poly2
    dummy = node(-1, -1)
    cur = dummy
    while cur1 and cur2:
        if cur1.power > cur2.power:
            cur.next = cur1
            cur1 = cur1.next
        elif cur2.power > cur1.power:
            cur.next = cur2
            cur2 = cur2.next
        else:
            sum = cur1.coef + cur2.coef
            newNode = node(sum, cur1.power)
            cur.next = newNode
            cur1 = cur1.next
            cur2 = cur2.next
        cur = cur.next
    
    if cur1:
        cur.next = cur1
        
        if cur2:
            cur.next = cur2
        
        return dummy.next

#Complexity:
#Time: O(m+n)
#Space: O(1)

#Test Cases:
#1st test case:
#1
#1 2
#0

#2nd test case:
#1
#1 2
#1
#1 3

#Link: https://www.geeksforgeeks.org/adding-two-polynomials-using-linked-list/


