def missing_number(nums: list[int]) -> int:
    n = len(nums)

    # Calculate the sum of all numbers that SHOULD be in the range [0, n].
    # The formula for the sum of an arithmetic series is n * (n + 1) / 2.
    # Use integer division (//) to ensure the result is an integer.
    expected_sum = n * (n + 1) // 2

    actual_sum = sum(nums)

    # The missing number is the difference between the expected total sum
    # and the actual sum of the numbers we have.
    res = expected_sum - actual_sum

    return res
