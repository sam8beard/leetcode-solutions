def isValidBST(root):
    def validate(root, left, right):
        if not root:
            return True
        if not (right > root.val and left < root.val):
            return False

        return validate(root.left, left, root.val) \
            and validate(root.right, root.val, right)

    validate(root, float("-inf"), float("inf"))
