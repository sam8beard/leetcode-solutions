def isSameTree(self, p, q):

    # structurally identical -> both trees have same level of depth on all branches
    # nodes have the same value -> every node on a given level for both trees has the same value

    # Both are null, both subtrees end here
    if not p and not q:
        return True
    # Only one is null or values are not equal
    if not p or not q or p.val != q.val:
        return False

    # Why do we not need this case?
    # -> Given two nodes, false will only return when:
    #   -> one node doesn't exist
    #   OR
    #   -> the values of both nodes are not equal
    # -> This means the function will continue down that subtree
    #    while both nodes exist at that level and their values are equal

    return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
