from createBinaryTree import TreeNode
def addOneRow(self, root,  val, depth):
        if not root:
            return None
        level = 1
        if depth == 1:
            leftSubTree = root
            root = TreeNode(val)
            root.left = leftSubTree
            return root
        self.addRow(root, level, val, depth)
        return root
def addRow(self, root, level, val, depth):
    if not root:
            return None
    if level == depth-1:
        leftSubTree = root.left
        root.left = TreeNode(val)
        root.left.left = leftSubTree

        rightSubTree = root.right
        root.right = TreeNode(val)
        root.right.right = rightSubTree
        
    self.addRow(root.left, level + 1, val, depth)
    self.addRow(root.right, level + 1, val, depth)
    
        