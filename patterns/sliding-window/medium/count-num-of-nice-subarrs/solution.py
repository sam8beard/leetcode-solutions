def numberOfSubarrays(nums, k):
    # variable window size
    l = 0
    res = 0
    odd_count = 0
    for r in range(len(nums)):
        if nums[r] % 2 == 1:
            odd_count += 1
        while odd_count > k:
            if nums[l] % 2 == 1:
                odd_count -= 1
            l += 1

        """
            This counts all valid starting positions for subarrays that:
            - end at r
            AND
            - have exactly k odd numbers
        """
        if odd_count == k:
            # [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
            #  l              r
            #        tl
            temp_left = l
            left_evens = 0
            # count the number of evens before the first odd
            while temp_left <= r and nums[temp_left] % 2 == 0:
                temp_left += 1
            # we add one because we include the position of the first odd
            # in the final count of possible starting positions
            left_evens = temp_left - l + 1
            res += left_evens
    return res
