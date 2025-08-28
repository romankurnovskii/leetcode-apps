def grayCode(n):
    """
    Generate an n-bit Gray code sequence.
    
    Args:
        n: int - Number of bits for the Gray code sequence
        
    Returns:
        List[int] - Valid n-bit Gray code sequence
    """
    # Handle edge case
    if n == 0:
        return [0]
    
    # Start with base case: 1-bit Gray code
    result = [0, 1]
    
    # Build larger Gray codes using reflection method
    for i in range(2, n + 1):
        # Get the size of the current sequence
        size = len(result)
        
        # Reflect the current sequence and add prefix '1'
        for j in range(size - 1, -1, -1):
            # Add 2^(i-1) to create the reflected part with prefix '1'
            result.append(result[j] + (1 << (i - 1)))
    
    return result
