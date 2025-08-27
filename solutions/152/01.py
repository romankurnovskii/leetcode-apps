def maxProduct(nums: List[int]) -> int:
    if not nums:
        return 0

    max_product = nums[0]
    curr_max = nums[0]
    curr_min = nums[0]

    for i in range(1, len(nums)):
        prev_max = curr_max
        prev_min = curr_min

        curr_max = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
        curr_min = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)

        max_product = max(max_product, curr_max)

    return max_product