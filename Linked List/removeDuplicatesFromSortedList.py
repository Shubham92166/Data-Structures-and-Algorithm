from createLinkedList import *
node = Node()
def removeDuplicateNodes(head):
    if not head:
        return head
    cur = head
    while(cur and cur.next):
        if(cur.val == cur.next.val):
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

list1 = node.createLL([])
res = removeDuplicateNodes(list1)
node.printLL(res)

list12 = node.createLL([1,1,17,44,50,50])
res = removeDuplicateNodes(list12)
node.printLL(res)


