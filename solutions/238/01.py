def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n

    # First pass: Calculate prefix products
    # current_product_from_left accumulates the product of elements encountered so far from the left.
    current_product_from_left = 1
    for i in range(n):
        # res[i] stores the product of all elements to the left of nums[i].
        # For i=0, there are no elements to the left, so it's 1 (initialized value).
        res[i] = current_product_from_left
        # Update current_product_from_left for the next iteration.
        current_product_from_left *= nums[i]

    # Second pass: Calculate suffix products and combine with prefix products
    # current_product_from_right accumulates the product of elements encountered so far from the right.
    current_product_from_right = 1
    for i in range(n - 1, -1, -1):  # Iterate from n-1 down to 0
        # Multiply the already stored prefix product (res[i]) by the suffix product.
        # current_product_from_right holds the product of elements to the right of nums[i].
        # For i=n-1, there are no elements to the right, so it's 1 (initialized value).
        res[i] *= current_product_from_right
        current_product_from_right *= nums[i]

    return res
