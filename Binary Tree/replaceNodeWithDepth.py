def changeToDepthTree(root):
    root = change(root, 0)
    return root

def change(root, level):
    if not root:
        return 

    root.val = level

    change(root.left, level + 1)
    change(root.right, level + 1)
    
#Complexity:
#Time: O(n)
#Space: O(h)
#O(h) in the worst case can be O(n). h is the height and n is the no. of nodes

#Test Cases:
#2, 35, 10, 2, 3, 5, 2, -1, -1, -1, -1, -1, -1, -1, -1 

#Link: https://www.geeksforgeeks.org/replace-node-with-depth-in-a-binary-tree/
