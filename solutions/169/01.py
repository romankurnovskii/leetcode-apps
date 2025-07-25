def majority_element(nums: list[int]) -> int:
    n = len(nums)

    majority_threshold = n // 2
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

        if counts[num] > majority_threshold:
            res = num
            return res

    return -1
