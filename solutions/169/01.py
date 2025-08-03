def majorityElement(nums: List[int]) -> int:
    candidate = nums[0]
    count = 1

    # starting from the second element
    for i in range(1, len(nums)):
        if nums[i] == candidate:
            count += 1
        else:
            count -= 1
            # If count becomes 0, change candidate
            if count == 0:
                candidate = nums[i]
                count = 1

    return candidate