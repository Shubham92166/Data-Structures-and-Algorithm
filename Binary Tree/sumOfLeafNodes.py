def sumOfLeftLeaves(root):
    sum = 0
    return sumLeft(root, False)
def sumLeft(root, isLeft):
    if not root:
        return 0
    if not root.left and not root.right:
        if isLeft:
            return root.val
        else:
            return 0
    return sumLeft(root.left, True) + sumLeft(root.right, False)