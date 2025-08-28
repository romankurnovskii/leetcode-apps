def countPairs(deliciousness):
    """
    Count the number of good meals (pairs that sum to a power of 2).
    
    Args:
        deliciousness: List[int] - Array of food deliciousness values
        
    Returns:
        int - Number of good meals modulo 10^9 + 7
    """
    # Handle edge case
    if len(deliciousness) < 2:
        return 0
    
    # Create frequency hash table
    freq = {}
    for num in deliciousness:
        freq[num] = freq.get(num, 0) + 1
    
    # Generate powers of 2 up to maximum possible sum
    max_sum = 2 * max(deliciousness)
    powers_of_2 = []
    power = 1
    while power <= max_sum:
        powers_of_2.append(power)
        power *= 2
    
    # Count pairs that sum to each power of 2
    result = 0
    MOD = 10**9 + 7
    
    for target in powers_of_2:
        for num in freq:
            complement = target - num
            
            # Check if complement exists and is different from num
            if complement in freq and complement != num:
                result = (result + freq[num] * freq[complement]) % MOD
            # Handle case where complement equals num (same value)
            elif complement == num and freq[num] >= 2:
                # Calculate combinations: C(freq[num], 2)
                combinations = (freq[num] * (freq[num] - 1)) // 2
                result = (result + combinations) % MOD
    
    # Divide by 2 since we counted each pair twice
    return result // 2
