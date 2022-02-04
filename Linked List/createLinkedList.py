class ListNode:
    def __init__(self, val, Next):
        self.val = val
        self.next = None
def createLL(nums):
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

def printLL(head):
    while(head is not None):
        print(head.val)
        head = head.next

head = createLL([1,2,3])
print(printLL(head))
            