def deleteNode(root, key):
    if not root:
        return None
    if root.val > key:
        newLeft = deleteNode(root.left, key)
        root.left = newLeft
        return root
    if root.val < key:
        newRight = deleteNode(root.right, key)
        root.right = newRight
        return root
    if not root.left and not root.right:
        return None
    if not root.left:
        return root.right
    if not root.right:
        return root.left
    minNode = min(root.right)
    root.val = minNode
    root.right = deleteNode(root.right, minNode)
    return root
    
def min(root):
    if not root:
        return 10000
    if not root.left:
        return root.val
    return min(root.left)