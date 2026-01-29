def lengthOfLongestSubstring(s):
    longest = set()
    res = 0
    l = 0
    for r in range(len(s)):

        # left basically serves as the position as the last time this character was seen
        # this says, "would adding this character invalidate our current window?"
        while s[r] in longest:
            longest.remove(s[l])
            l += 1
        longest.add(s[r])
        res = max(res, len(longest))
    return res
