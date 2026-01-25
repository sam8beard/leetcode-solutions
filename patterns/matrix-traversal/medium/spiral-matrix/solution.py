def spiralOrder(matrix):
    """
    For visualization
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    """
    res = []
    depth = len(matrix)
    width = len(matrix[0])

    # Directions
    right = [0, +1]
    left = [0, -1]
    up = [-1, 0]
    down = [+1, 0]

    visited = set()

    # go right until c == width or position in visited
    # go down until r == depth or position in visited
    # go left until c == 0 or position in visited
    # go up until r == 0 or position in visited
    # repeat while len(visited) < depth * width
    r, c = 0, 0
    visited.add((r, c))
    while len(visited) < (depth * width):
        # go right
        while c < width - 1 and (r, c + 1) not in visited:
            print(r, c)

            print("going right")
            res.append(matrix[r][c])
            r, c = r + right[0], c + right[1]
            visited.add((r, c))

        print(r, c)
        # go down
        while r < depth - 1 and (r + 1, c) not in visited:
            print(r, c)
            print("going down")
            res.append(matrix[r][c])
            r, c = r + down[0], c + down[1]
            visited.add((r, c))

        print(r, c)

        # go left
        while c > 0 and (r, c - 1) not in visited:
            print(r, c)
            print("going left")
            res.append(matrix[r][c])
            r, c = r + left[0], c + left[1]
            visited.add((r, c))

        print(r, c)

        # go up
        while r > 0 and (r - 1, c) not in visited:
            print(r, c)
            print("going up")
            res.append(matrix[r][c])

            r, c = r + up[0], c + up[1]
            visited.add((r, c))
        print("outside any direction change", r, c)

    res.append(matrix[r][c])
    print(res)
    return res
