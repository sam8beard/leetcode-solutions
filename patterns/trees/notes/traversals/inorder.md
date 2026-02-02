# Inorder Traversal

***==(Left -> Root -> Right)==***

## Rule
==**For *each node***:==
1. Visit the **left subtree**
2. Visit the **node itself**
3. Visit the **right subtree**

**==Think of it as:==**
>=="*Go left as far as possible, then come back up*"==

## Visualization

    A
   / \
  B   C
 / \   \
D   E   F

==Order of Visits:==
1. D
2. B
3. E
4. A
5. C
6. F

==Result: ***(D -> B -> E -> A -> C -> F)*** ==

## Key Insight
- For BSTs, inorder traversal gives values in **sorted order**
- This traversal is about **structure**, not speed
