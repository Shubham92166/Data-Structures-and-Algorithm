from createBinaryTree import *

tree = BinaryTee()

def createBinaryTree(descriptions):
    dic = {}
    children = set()
    for i in descriptions:
        if i[0] not in dic:
            parent = TreeNode(i[0])
            dic[i[0]] = parent
        else:
            parent = dic.get(i[0])
        
        if i[1] not in dic:
            child = TreeNode(i[1])
            children.add(i[1])
            dic[i[1]] = child
        else:
            child = dic.get(i[1])
            children.add(i[1])
        
        
        if i[2] == 1:
            parent.left = child
        else:
            parent.right = child
    
    root = None
    allNodes = list(dic.keys())
    
    for node in allNodes:
        if node not in children:
            root = dic.get(node)
            
    return root

#Complexity:
#Time: O(n) #if we ignore the complexity for node creation else it is O(n^2)
#Space: O(n)

#Test Cases:
#[[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]], [[1,2,1],[2,3,0],[3,4,1]]

root = createBinaryTree([[1,2,1],[2,3,0],[3,4,1]])
print(tree.printTree(root))

root = createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
print(tree.printTree(root))
