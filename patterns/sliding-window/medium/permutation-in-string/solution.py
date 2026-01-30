def checkInclusion(s1, s2):
    from collections import Counter, defaultdict
    # fixed window size of len(s1)
    l = 0
    s2_freq = defaultdict(int)
    s1_freq = Counter(s1)
    for r in range(len(s2)):
        s2_freq[s2[r]] += 1
        while r - l + 1 > len(s1):
            s2_freq[s2[l]] -= 1
            if s2_freq[s2[l]] == 0:
                del s2_freq[s2[l]]
            l += 1
        if s2_freq == s1_freq:
            return True
    return False
