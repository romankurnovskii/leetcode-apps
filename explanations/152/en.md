# 152. Maximum Product Subarray

**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/maximum-product-subarray/

## Problem Description

Given an integer array `nums`, find a **subarray** that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a **32-bit** integer.

**Example 1:**
```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:**
```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

**Constraints:**
- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.

## Explanation

### Strategy

This is a **dynamic programming problem** that requires finding the maximum product of a contiguous subarray. The key insight is that we need to track both the maximum and minimum products at each position, because a negative number can turn a minimum into a maximum.

**Key observations:**
- We need to track both max and min products at each position
- A negative number can turn a minimum into a maximum
- We need to consider starting a new subarray at each position
- The current element can be the start of a new subarray

**High-level approach:**
1. **Track both max and min**: At each position, track the maximum and minimum products ending at that position
2. **Consider three cases**: For each element, consider:
   - The element itself (start new subarray)
   - The element times the previous max (extend positive subarray)
   - The element times the previous min (negative can become positive)
3. **Update global max**: Keep track of the overall maximum product

### Steps

Let's break down the solution step by step:

**Step 1: Initialize variables**
- `max_product`: Track the overall maximum product
- `curr_max`: Track the maximum product ending at current position
- `curr_min`: Track the minimum product ending at current position

**Step 2: Iterate through the array**
For each element:
- Calculate new max: `max(element, element * curr_max, element * curr_min)`
- Calculate new min: `min(element, element * curr_max, element * curr_min)`
- Update global max: `max_product = max(max_product, curr_max)`

**Step 3: Return result**
- Return the `max_product`

**Example walkthrough:**
Let's trace through the first example:

```
nums = [2,3,-2,4]

Initial state:
max_product = 2, curr_max = 2, curr_min = 2

Step 1: element = 3
new_max = max(3, 3*2, 3*2) = max(3, 6, 6) = 6
new_min = min(3, 3*2, 3*2) = min(3, 6, 6) = 3
curr_max = 6, curr_min = 3
max_product = max(2, 6) = 6

Step 2: element = -2
new_max = max(-2, -2*6, -2*3) = max(-2, -12, -6) = -2
new_min = min(-2, -2*6, -2*3) = min(-2, -12, -6) = -12
curr_max = -2, curr_min = -12
max_product = max(6, -2) = 6

Step 3: element = 4
new_max = max(4, 4*-2, 4*-12) = max(4, -8, -48) = 4
new_min = min(4, 4*-2, 4*-12) = min(4, -8, -48) = -48
curr_max = 4, curr_min = -48
max_product = max(6, 4) = 6

Result: Return 6
```

> **Note:** The key insight is that we need to track both the maximum and minimum products because a negative number can turn a minimum into a maximum. This is different from the maximum subarray sum problem where we only need to track the maximum.

### Solution

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Handle edge case
        if not nums:
            return 0
        
        # Initialize variables
        max_product = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Store previous values to avoid overwriting
            prev_max = curr_max
            prev_min = curr_min
            
            # Calculate new maximum and minimum products
            curr_max = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            curr_min = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            
            # Update the overall maximum product
            max_product = max(max_product, curr_max)
        
        # Return the maximum product
        return max_product
```

**Time Complexity:** O(n) - we visit each element exactly once  
**Space Complexity:** O(1) - we only use a constant amount of extra space 