class Solution:
    def __init__(self):
        self.nodes = []
        self.maxLevel = 0
    def findBottomLeftValue(self, root):
        level = 0
        self.findBottomValue(root, self.nodes, level)
        return self.nodes[0]
    def findBottomValue(self, root, nodes, level):
        if not root:
            return None
        if not root.left and not root.right:
            if level > self.maxLevel:
                self.maxLevel = level
                self.nodes = []
                self.nodes.append(root.val)
            elif level == self.maxLevel:
                self.nodes.append(root.val)
        self.findBottomValue(root.left, nodes, level + 1) 
        self.findBottomValue(root.right, nodes, level + 1) 