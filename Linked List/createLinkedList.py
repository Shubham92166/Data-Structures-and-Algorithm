class ListNode:
    def __init__(self, val, Next = None):
        self.val = val
        self.next = None

class Node:
    def __init__(self):
        pass
    def createLL(self,nums):
        head = None
        cur = None
        for val in nums:
            newNode = ListNode(val, None)
            if head is None:
                head = newNode
                cur = newNode
            else:
                cur.next = newNode
                cur = newNode
        #cur.next = None
        return head

    def printLL(self,head):
        if not head:
            return head
        while(head):
            if head.next:
                print(str(head.val)+"->", end='')
            else:
                print(str(head.val))
            head = head.next
        return

  

            