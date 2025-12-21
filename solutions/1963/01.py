def getXORSum(arr1, arr2):
    """
    Find the XOR sum of all pairs bitwise AND results.

    Args:
        arr1: List[int] - First array of integers
        arr2: List[int] - Second array of integers

    Returns:
        int - XOR sum of all (arr1[i] AND arr2[j]) pairs
    """
    # Compute XOR sum of arr2
    arr2_xor_sum = 0
    for num in arr2:
        arr2_xor_sum ^= num

    # For each element in arr1, compute (element AND arr2_xor_sum)
    # Then XOR all these results together
    result = 0
    for num in arr1:
        result ^= num & arr2_xor_sum

    return result
