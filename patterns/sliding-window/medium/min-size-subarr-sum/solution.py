def minSubArrayLen(target, nums):
    # variable window size, return smallest window size
    l = 0
    curr_sum = 0
    res = 10**5
    match = False
    for r in range(len(nums)):
        curr_sum += nums[r]
        while curr_sum >= target:
            match = True
            res = min(res, r - l + 1)
            curr_sum -= nums[l]
            l += 1

    if not match:
        return 0

    return res
