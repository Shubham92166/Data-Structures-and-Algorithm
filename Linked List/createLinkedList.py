class ListNode:
    def __init__(self, val, Next):
        self.val = val
        self.next = None
class Node:
    def __init__(self):
        pass
    def createLL(self, nums):
        head =None
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

    def printLL(self, head):
        while(head is not None):
            print(str(head.val), "->", end = ' ')
            head = head.next
        print(None)


            