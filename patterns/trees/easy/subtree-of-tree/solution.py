def isSubtree(self, root, subRoot):
    # if subtree is empty, then it is technically a subtree of the other tree
    if not subRoot:
        return True
    # if tree is empty, but subtree is not, subtree cannot be a subtree of tree
    if not root and subRoot:
        return False

    # check both trees to see if they are the same
    if self.sameTree(root, subRoot):
        return True

    # if not, check the left and right subtrees of root to see if there is a subtree that matches
    if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
        return True

    return False


def sameTree(self, rootNode, subRootNode):
    # Both are null, both subtrees end here
    if not rootNode and not subRootNode:
        return True
    # Only one is null or values are not equal
    if not rootNode or not subRootNode or rootNode.val != subRootNode.val:
        return False
    return (self.sameTree(rootNode.left, subRootNode.left)) and (self.sameTree(rootNode.right, subRootNode.right))
