def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """

    layers = int(len(matrix) / 2)
    for layer in range(layers):
        swaps = len(matrix) - 1 - (2 * layer)
        for i in range(swaps):
            # Values to change
            top = matrix[layer][layer + i]
            right = matrix[i + layer][len(matrix[0]) - 1 - layer]
            bottom = matrix[len(matrix) - 1 -
                            layer][len(matrix[0]) - 1 - i - layer]
            left = matrix[len(matrix) - 1 - i - layer][layer]

            # Positions in matrix to change
            top_pos = [layer, layer + i]
            right_pos = [i + layer, len(matrix[0]) - 1 - layer]
            bottom_pos = [len(matrix) - 1 - layer,
                          len(matrix[0]) - 1 - i - layer]
            left_pos = [len(matrix) - 1 - i - layer, layer]

            # Rotate elements
            matrix[right_pos[0]][right_pos[1]] = top
            matrix[bottom_pos[0]][bottom_pos[1]] = right
            matrix[left_pos[0]][left_pos[1]] = bottom
            matrix[top_pos[0]][top_pos[1]] = left
