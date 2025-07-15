def two_sum(nums, target):
    """Find two numbers that add up to target using a hash map for O(n) time complexity."""
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []
