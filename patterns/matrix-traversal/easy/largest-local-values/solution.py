def largestLocal(grid):
    res_width = len(grid[0]) - 2
    res_height = len(grid) - 2
    res = [[0] * res_width for _ in range(res_height)]

    drc = [(1, 0), (-1, 0), (1, 1), (-1, -1),
           (0, -1), (1, -1), (0, 1), (0, 0), (-1, 1)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            valid = True
            m = 0
            for d in drc:
                if not (0 <= i + d[0] < len(grid)) or not (0 <= j + d[1] < len(grid[0])):
                    valid = False
                    break
                m = max(m, grid[i + d[0]][j + d[1]])
            if valid:
                res[i - 1][j - 1] = m
    return res
