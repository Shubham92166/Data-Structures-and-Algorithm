def insertIntoBST(root, val):
    if not root:
        node = TreeNode(val)
        return node
    if root.val > val:
        root.left = insertIntoBST(root.left, val)
        return root
    if root.val <= val:
        root.right = insertIntoBST(root.right, val)
        return root

        