def matrixReshape(mat, r, c):
    if (r * c) != (len(mat) * len(mat[0])):
        return mat

    res = []
    values = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            values.append(mat[i][j])

    idx = 0
    for i in range(r):
        row = []
        for j in range(c):
            row.append(values[idx])
            idx += 1
        res.append(row)
    return res
