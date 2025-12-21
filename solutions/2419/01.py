def longestSubarray(nums: List[int]) -> int:
    res = 0
    max_val = max(nums)
    size = 0
    for num in nums:
        if num == max_val:
            size += 1
            res = max(res, size)
        else:
            size = 0
    return res
