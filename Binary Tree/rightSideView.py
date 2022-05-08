    import queue
    def rightSideView(root):
        if not root:
            return None
        q = queue.Queue()
        ans = []
        temp = [] 
        q.put(root)
        temp.append(root.val)
        q.put(None)
        if not root.left and not root.right:
            return [root.val]
        ans.append(root.val)
        while(not q.empty()):
            node = q.get()
            if node == None:
                if temp:
                    ans.append(temp[-1])
                if not q.empty():
                    q.put(None)
                    temp = []
                continue
            if node.left:
                temp.append(node.left.val)
                q.put(node.left)
            if node.right:
                temp.append(node.right.val)
                q.put(node.right)
        return ans