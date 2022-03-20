def invertTree(root):
    if not root:
        return None
    leftTree = root.left
    root.left = root.right
    root.right = leftTree

    invertTree(root.left)
    invertTree(root.right)

    return root