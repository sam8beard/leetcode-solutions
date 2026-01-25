Intuition: 

        - What does it mean to rotate 90 degrees in this context? 
        - Rotate by layers of matrix
        - Rotate starting from outer layer -> inner layer
        - How do we define a the first layer? 
            - the first layer contains all positions such that that index of a position is
                - in the first row
                - in the first column
                OR 
                - in the last row
                - in the last column
            - so r = 0 or len(m) - 1 and c = 0 or len(m[0]) - 1
        - So how do we apply this procedurally? 
            - By this intuition
                - the second layer would be positions where
                    - r = 0 + 1 or len(m) - 2 and c = 0 + 1 or len(m[0]) - 2
            - So whats changing? 
                - we need a way to define the bounds of a layer and update it i think

        - Keep a layer var
            - layer 0 --> outermost
            - layer 1 --> one step inward
            ...and so on
        - For an N x M matrix, each layer is defined by
            - top = layer 
            - bottom = n - 1 - layer
            - left = layer 
            - right = n - 1 - layer
        - Within each layer, we rotate groups of cells, NOT individually 
            - top --> right
            - right --> bottom
            - bottom --> left
            - left --> top

        - Within each layer, rotate a group of 4 cells at a time 

        - The number of layers in a m x n matrix are defined as min(m, n) / 2

        layers = m / 2

        [1, 2, 3, 4, 5]
        [6, 7, 8, 9, 1]
        [2, 3, 4, 5, 6]
        [7, 8, 9, 1, 2]
        [3, 4, 5, 6, 7]

        len(m) - 1 = 4
        len(m[0]) = 4
        
        given n = len(m) - 1, for each layer, we need to make n - layer - 1 swaps
        # if bounds % 2 = 0, swaps = bounds - 1
        # if bounds % 2 != 0, swaps = bounds - 1
        # for each layer in m
        for l in range(layers): 
                # define the bounds for this layer
                bounds = len(m) - 1 - l
                # make bounds - 2 swaps per pass in this layer?
                # i should only iterate up to the amount of swaps
                for i in range(bounds - 1):

                    # for each pass in this layer,
                    # define a group of 4 values/positions to rotate

                    # Values to change
                    top = m[i + layer][i + layer]
                    right = m[i + layer][len(m[0]) - 1 - layer]
                    bottom = m[len(m) - 1 - layer][len(m[0]) - 1 - i - layer]
                    left = m[len(m) - 1 - i][layer]

                    layer = 1
                    bottom = ?
                    bounds = 3 -> iterate up to 3 - 1 = 2
                    
                    how many swaps (4 rotations) per pass in layer l? 

                    i = 0
                    col = 4 - 0 - 1
                    [3][3]
                    i = 1
                    col = 4 - 1 - 1 
                    [3][2]
                    

                    # Positions in matrix to change
                    top_pos = [layer, i]
                    right_pos = [i, len(m[0]) - 1 - layer]]
                    bottom_pos = [len(m) - 1 - layer, len(m[0]) - 1 - i]
                    left_pos = [len(m) - 1 - i, layer]

                    # Rotate elements
                    m[right_pos[0]][right_pos[1]] = top
                    m[bottom_pos[0]][bottom_pos[1]] = right
                    m[left_pos[0]][left_pos[1]] = bottom
                    m[top_pos[0]][top_pos[1]] = right
