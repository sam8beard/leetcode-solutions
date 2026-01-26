def largestOverlap(img1, img2):
    from collections import Counter

    # Get positions of all 1s and 0s in img1 and img2
    img2_pos = {1: [], 0: []}
    img1_pos = {1: [], 0: []}
    for i in range(len(img2)):
        for j in range(len(img2[0])):
            img2_pos[img2[i][j]].append((i, j))
            img1_pos[img1[i][j]].append((i, j))

    # Iterate through all positions in both images containing 1s
    offsets = []
    for (val1, idxs1), (val2, idxs2) in zip(img1_pos.items(), img2_pos.items()):
        # Evaluate the positions where 1s exist in img1 and img2
        if val1 == 1 and val2 == 1:
            """
            For every possible pair of positions of 1s in both img1 and img2, 
            calculate the offset from position 2 to position 1. 

            The offset that occurs the most frequently is the maximum overlap
            that any valid translation could produce.
            """
            for i in range(len(idxs1)):
                idxs1_pos = (idxs1[i][0], idxs1[i][1])
                for j in range(len(idxs2)):
                    idxs2_pos = (idxs2[j][0], idxs2[j][1])
                    offsets.append(
                        (idxs2_pos[0] - idxs1_pos[0], idxs2_pos[1] - idxs1_pos[1]))

    # The frequency of each translation corresponds to the
    # overlap produced by that translation
    counts = Counter(offsets)
    overlap = 0
    if counts:
        # Return the maxium overlap
        return max(counts.values())
    return overlap
