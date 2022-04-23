class Solution:
    def __init__(self):
        self.sum = 0
        self.maxdepth = 0
    def deepestLeavesSum(self, root):
        if not root:
            return 0
        depth = 0
        self.deepestSum(root, depth, self.maxdepth)
        return self.sum
    def deepestSum(self, root, depth, maxdepth):
        if not root:
            return 0
        if root.left == None and root.right == None:
            if depth > self.maxdepth:
                self.sum = root.val
                self.maxdepth = depth
            elif depth == self.maxdepth:
                self.sum += root.val
        self.deepestSum(root.left, depth+1, maxdepth)
        self.deepestSum(root.right, depth+1, maxdepth)