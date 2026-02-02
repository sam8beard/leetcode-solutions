# Postorder Traversal

***==(Left -> Right-> Root)==***

## Rule
==**For *each node***:==
1. Visit the **left subtree**
2. Visit the **right subtree**
3. Visit the **node itself**

**==Think of it as:==**
>=="*Handle children completely before the parent*"==

## Visualization

    A
   / \
  B   C
 / \   \
D   E   F

==Order of Visits:==
1. D
2. E
3. B
4. F
5. C
6. A

==Result: ***(D -> E -> B -> F -> C -> A)*** ==

## Key Insight
- Common for **deleting/freeing** trees
- **Parent nodes** are processed **last**
