`def lowestCommonAncestor(self, root, p, q):`

> ==What does this case account for?==
- If this node is null -> we return None to signal to the current branch that there is no p or q in this branch
- If this node is p or q -> we return this node to signal to the current branch that there is a potential LCA in this branch
    - Because either -> the other node is in its subtree OR this node itself is the LCA (an LCA of p and q can be p or q itself)

`    if not root or root == p or root == q:`
`        return root`

> == Recursive Case ==
- Search both subtrees for p or q
    - The return value will either be:
        - None -> if neither p nor q is found in this subtree
        - p or q -> if that node (or the LCA below is found)

`    left = self.lowestCommonAncestor(root.left, p, q)`
`    right = self.lowestCommonAncestor(root.right, p, q)`


> ==What does this case account for?==
- If both left and right are non-None -> either p or q was found in one subtree, and the other node was found in the other subtree
- Therefore, the current node root is their LCA

`    if left and right:`
`        return root`

> == Final Return ==
- If only one subtree contains a node -> return the non-None subtree value

`    return left or right`
