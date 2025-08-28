def trap(height):
    """
    Calculate the amount of water that can be trapped between walls.
    
    Args:
        height: List[int] - Array representing wall heights
        
    Returns:
        int - Total amount of water trapped
    """
    # Handle edge cases
    if not height or len(height) < 3:
        return 0
    
    n = len(height)
    
    # Step 1: Precompute left maximums
    # left_max[i] = highest wall to the left of position i (including i)
    left_max = [0] * n
    left_max[0] = height[0]
    
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    # Step 2: Precompute right maximums
    # right_max[i] = highest wall to the right of position i (including i)
    right_max = [0] * n
    right_max[n-1] = height[n-1]
    
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    # Step 3: Calculate trapped water at each position
    res = 0
    for i in range(n):
        # Water trapped = min(left_max, right_max) - current_height
        # But only if positive (can't have negative water)
        water = min(left_max[i], right_max[i]) - height[i]
        if water > 0:
            res += water
    
    return res


# Example usage and testing
if __name__ == "__main__":
    # Test case 1
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"Input: {height1}")
    print(f"Output: {trap(height1)}")  # Expected: 6
    
    # Test case 2
    height2 = [4,2,0,3,2,5]
    print(f"\nInput: {height2}")
    print(f"Output: {trap(height2)}")  # Expected: 9
    
    # Edge case: empty array
    height3 = []
    print(f"\nInput: {height3}")
    print(f"Output: {trap(height3)}")  # Expected: 0
    
    # Edge case: single element
    height4 = [5]
    print(f"\nInput: {height4}")
    print(f"Output: {trap(height4)}")  # Expected: 0
