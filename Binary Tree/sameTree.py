def isSameTree(p, q):
    if not p and q or p and not q:
        return False
    if not p and not q:
        return True
    if p.val != q.val:
        return False
    res1  = isSameTree(p.left, q.left)
    res2 = isSameTree(p.right, q.right)
    return res1 and res2