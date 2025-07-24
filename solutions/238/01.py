def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    
    # Initialize the result array with 1s. This array will store the final products.
    # In the first pass, it will temporarily store left products.
    res = [1] * n

    # --- First Pass: Calculate products of elements to the left of each index ---
    # 'left_product' accumulates the product from the beginning of the array.
    left_product = 1
    for i in range(n):
        # At index i, res[i] gets the product of nums[0]...nums[i-1]
        res[i] = left_product
        # Update left_product for the next iteration (include nums[i])
        left_product *= nums[i]

    # --- Second Pass: Calculate products of elements to the right of each index
    #                  and combine with existing left products in 'res' ---
    # 'right_product' accumulates the product from the end of the array.
    right_product = 1
    # Iterate from the second to last element backwards to the first element
    for i in range(n - 1, -1, -1):
        # Multiply the current res[i] (which holds left product) by the right product
        res[i] *= right_product
        # Update right_product for the next iteration (include nums[i])
        right_product *= nums[i]
    
    return res