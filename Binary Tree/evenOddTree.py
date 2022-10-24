import queue
def isEvenOddTree(root):
    q = queue.Queue()
    q.put(root)
    q.put(None)
    level = 0
    levelOrder = []
    while not q.empty():
        node = q.get()
        if node:
            if level % 2 == 0:
                if node.val % 2 == 0:
                    return False
                if not levelOrder:
                    levelOrder.append(node.val)
                else:
                    if levelOrder[-1] < node.val:
                        levelOrder.append(node.val)
                    else:
                        return False     
            else:
                if node.val % 2 != 0:
                    return False
                if not levelOrder:
                    levelOrder.append(node.val)
                else:
                    if levelOrder[-1] > node.val:
                        levelOrder.append(node.val)
                    else:
                        return False
        else:
            if not q.empty():
                levelOrder.clear()
                q.put(None)
                level += 1
            continue
        if node.left:
            q.put(node.left) 
        if node.right:
            q.put(node.right)
    return True

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1,10,4,3,null,7,9,12,8,6,null,null,2], [5,4,2,3,3,7], [5,9,1,3,5,7]

#Link: https://leetcode.com/problems/even-odd-tree/
    