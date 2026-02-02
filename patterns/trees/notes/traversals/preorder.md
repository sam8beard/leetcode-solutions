# Preorder Traversal

***==(Root -> Left -> Right)==***

## Rule
==**For *each node***:==
1. Visit the **node itself**
2. Visit the **left subtree**
3. Visit the **right subtree**

**==Think of it as:==**
>=="*Visit the node as soon as you see it*"==

## Visualization

    A
   / \
  B   C
 / \   \
D   E   F

==Order of Visits:==
1. A
2. B
3. D
4. E
5. C
6. F

==Result: ***(A -> B -> D -> E -> C -> F)*** ==

## Key Insight
- Useful for **copying or serializing** a tree
- The **root** is always visited **first**
