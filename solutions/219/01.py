def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    window_set = set()

    for i, num in enumerate(nums):
        if i > k:
            window_set.remove(nums[i - k - 1])

        if num in window_set:
            res = True
            return res

        window_set.add(num)

    res = False
    return res
