def search_insert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            res = mid
            return res
        elif nums[mid] < target:
            left = mid + 1
        else:  # nums[mid] > target
            right = mid - 1

    # If the loop finishes, it means the target was not found.
    # The 'left' pointer will be at the correct insertion point.
    res = left
    return res
