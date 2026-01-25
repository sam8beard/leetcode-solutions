def findDiagonalOrder(mat):
    """
    1. For every position on a given diagonal:
        -> r + c == d
    2. There are (m + n) - 1 diagonals on an m x n matrix
    3. The traversal alternates direction when:
        -> if d % 2 == 0, traverse upward
        -> if d % 2 != 0, traverse downward
    4. How would we group all cells in a given diagonal?
        -> if r + c == d, diags[d].append(mat[r][c])
    """

    m, n = len(mat), len(mat[0])
    diags = [(d, []) for d in range(m + n - 1)]
    diags = dict(diags)

    for i in range(m):
        for j in range(n):
            if (i + j) % 2 == 0:
                diags[i + j].insert(0, mat[i][j])
            else:
                diags[i + j].append(mat[i][j])

    return [i for v in diags.values() for i in v]
