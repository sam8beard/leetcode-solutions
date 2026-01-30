def characterReplacement(s, k):
    from collections import defaultdict
    # how many times does the most frequent character appear in our window?
    # while the window size - the highest frequency in our window is larger than k, shrink the window

    l = 0
    char_freq = defaultdict(int)
    max_freq = 0
    res = 0
    for r in range(len(s)):
        # increase the frequency of this character
        char_freq[s[r]] += 1
        # update the most frequent character in this window
        max_freq = max(max_freq, char_freq[s[r]])

        """
            While the current window size minus the amount of times the 
            most frequent appears is greater than the amount of replacements needed:
            --> update the frequency of the first character in the window by removing one
            --> shrink the window from the left

            i.e. if the current window size is 4 with chars ABAB,
                 then we shrink the window
            
            This basically means that if the most frequent character 
            does not occupy the whole window, then look at how many replacements 
            would be needed to make this so. If this number of replacements 
            is greater than the allowed replacements (k) then shrink the window to look
            for other possible candidates.
            """
        while (r - l + 1) - max_freq > k:
            char_freq[s[l]] -= 1
            l += 1

        # update the longest window with the greater window size between the last window
        # and the current window
        res = max(res, r - l + 1)

    return res
