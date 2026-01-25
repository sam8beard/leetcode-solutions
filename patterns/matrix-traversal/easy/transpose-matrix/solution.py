def transpose(matrix):
    """
    Visual
    [1, 2, 3]
    [4, 5, 6]

    [1, 4]
    [2, 5]
    [3, 6]

    all elements in row i are now shifted to column i and vice versa 
    """

    res = []
    for c in range(len(matrix[0])):
        col = []
        for r in range(len(matrix)):
            col.append(matrix[r][c])
        res.append(col)
    return res
