def contains_duplicate(nums: list[int]) -> bool:
    seen_numbers = set()

    for num in nums:
        if num in seen_numbers:
            res = True
            return res
        seen_numbers.add(num)

    res = False
    return res
