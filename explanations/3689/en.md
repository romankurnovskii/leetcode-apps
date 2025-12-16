## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to choose exactly `k` non-empty subarrays from `nums` such that the sum of their values is maximized. The value of a subarray is `max(subarray) - min(subarray)`.

**1.1 Constraints & Complexity:**

- **Input Size:** `n <= 5 * 10^4`, `k <= 10^5`, `nums[i] <= 10^9`
- **Time Complexity:** O(n) - We only need to find max and min once
- **Space Complexity:** O(1) - Only storing max and min values
- **Edge Case:** If `k = 0`, but constraints say `k >= 1`, so we don't need to handle this

**1.2 High-level approach:**

The key insight is that to maximize the total value, we should choose the subarray with the maximum value `k` times. The subarray with maximum value is the entire array itself, since it contains both the global maximum and minimum elements.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of `k` subarrays, calculate each value, and find the maximum sum. This would be exponential in complexity.
- **Optimized (Greedy):** Since we can choose the same subarray multiple times, and the entire array has the maximum value (max - min), we simply choose it `k` times. This gives us `(max - min) * k`.
- **Why it's better:** The entire array always has the maximum possible value because it contains both the maximum and minimum elements of the array.

**1.4 Decomposition:**

1. Find the maximum value in the array
2. Find the minimum value in the array
3. Calculate the value of the entire subarray: `max - min`
4. Multiply by `k` to get the maximum total value

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1,3,2], k = 2`

- Maximum value: 3
- Minimum value: 1
- Value of entire subarray: `3 - 1 = 2`
- Maximum total value: `2 * 2 = 4`

**2.2 Find Maximum and Minimum:**

We iterate through the array once to find the maximum and minimum values. This is O(n) time.

```python
max_val = max(nums)  # 3
min_val = min(nums)  # 1
```

**2.3 Calculate Maximum Total Value:**

The value of choosing the entire array once is `max_val - min_val`. Since we can choose it `k` times, the maximum total value is:

```python
return (max_val - min_val) * k  # (3 - 1) * 2 = 4
```

**2.4 Return Result:**

We return the calculated maximum total value.

**Time Complexity:** O(n) - Single pass to find max and min  
**Space Complexity:** O(1) - Only storing two variables

