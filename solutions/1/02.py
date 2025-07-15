def two_sum_v2(nums, target):
    """Brute-force approach to find two numbers that add up to target."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
