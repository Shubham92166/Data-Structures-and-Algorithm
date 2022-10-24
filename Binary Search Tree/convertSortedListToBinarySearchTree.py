#Approach-1: By converting Linked list to array

import sys
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Linked List")

from createBinaryTree import *
from createLinkedList import *

ll = Node()

tree = BinaryTee()
         
def sortedListToBST1(head):
    allNodes = []
    cur = head
    while cur:
        allNodes.append(cur.val)
        cur = cur.next
        
    root = sortedArrayToBST(allNodes)
    return root

def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root

#Complexity:
#Time: O(n)
#Space: O(n)

#Approach-2: Without converting Linked list into Array

def sortedListToBST2(head):
    if not head:
        return
    
    if not head.next:
        return TreeNode(head.val)
    
    rootNode, prev = findMiddle(head)

    root = TreeNode(rootNode.val)
    prev.next = None
    first = head
    second = rootNode.next
    rootNode.next = None
    
    root.left = sortedListToBST2(first)
    root.right = sortedListToBST2(second)
    return root
            

def findMiddle(head):
    slow, fast = head, head
    prevNode = None
    
    while fast and fast.next:
        prevNode = slow
        slow = slow.next
        fast = fast.next.next
    
    return slow, prevNode

#Complexity:
#Time: O(nlog n)
#Space: O(log n)
#where in worst case O(H) can be O(n)

#Test Cases:
#[-10,-3,0,5,9], []

head = ll.createLL([-10,-3,0,5,9])

root = sortedListToBST1(head)

res = tree.printTree(root)
print(res)

head = ll.createLL([-10,-3,0,5,9])

root = sortedListToBST2(head)

res = tree.printTree(root)
print(res)

#Link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

