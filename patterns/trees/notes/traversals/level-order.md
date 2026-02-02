# Level Order Traversal

***==(Breadth-First)==***

## Rule
- ==Visit nodes **level by level**==
- ==From **top to bottom**, **left to right**==
- ==This is **NOT** recursive by nature==

**==Think of it as:==**
>=="*Scan the tree row by row*"==

## Visualization

**Level 1**:     A
            / \
**Level 2**:   B   C
          / \   \
**Level 3**: D   E   F

==Order of Visits:==
1. A
2. B, C
3. D, E, F

==Result: ***(A -> B -> C -> D -> E -> F)*** ==

## Key Insight
- Uses a **queue** conceptually
- Useful when distance from the root matters
