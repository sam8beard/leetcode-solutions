def occurrencesOfElement(nums, queries, x):
    """
    keep a hashmap of occurences mapped to the index it occurs
    """
    from collections import defaultdict
    pos = defaultdict(list)
    occur = 0
    for i in range(len(nums)):
        if nums[i] == x:
            occur += 1
            pos[occur] = i
    res = []
    for i in range(len(queries)):
        if queries[i] in pos.keys():
            res.append(pos[queries[i]])
        else:
            res.append(-1)
    return res
