def moveZeroes(nums: List[int]) -> None:
    insert_pos = 0

    # First pass: Move all non-zero elements to the beginning of the array
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1

    # Second pass: Fill the remaining positions with zeros
    # These are the positions from insert_pos to the end of the array
    for i in range(insert_pos, len(nums)):
        nums[i] = 0
