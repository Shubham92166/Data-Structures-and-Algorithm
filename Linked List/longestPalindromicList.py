from createLinkedList import *

node = Node()

class Solution:
    def solve(self, A):
        prev = None
        cur = A 
        maxLength = 0
        while cur:
            nextNode = cur.next
            cur.next = prev

            maxLength = max(maxLength, 2*self.countCommonNodes(prev, nextNode)+1)
            maxLength = max(maxLength, 2*self.countCommonNodes(nextNode, cur))

            prev = cur
            cur = nextNode
        return maxLength

    
    def countCommonNodes(self, h1, h2):
        count = 0
        while h1 != None and h2 != None:
            if h1.val == h2.val:
                count += 1
            else:
                break
            h1 = h1.next
            h2 = h2.next
        return count

#Complexity:
#Time: O(n^2)
#Space: O(1)

#Test Cases:
#[2, 3, 3, 3], [2, 1, 2, 1, 2, 2, 1, 3, 2, 2]

sol = Solution()

head = node.createLL([2, 3, 3, 3])
print(sol.solve(head))

head = node.createLL([2, 1, 2, 1, 2, 2, 1, 3, 2, 2])
print(sol.solve(head))

#Link: https://practice.geeksforgeeks.org/problems/length-of-longest-palindrome-in-linked-list/1