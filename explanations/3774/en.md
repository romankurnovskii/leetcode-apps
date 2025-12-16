## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the absolute difference between the sum of the `k` largest elements and the sum of the `k` smallest elements in the array.

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= n <= 100`, `1 <= nums[i] <= 100`, `1 <= k <= n`
- **Time Complexity:** O(n log n) - Sorting dominates
- **Space Complexity:** O(1) - Only using input array
- **Edge Case:** `k = n` means we use all elements

**1.2 High-level approach:**

Sort the array, then take the `k` largest elements (last `k` elements) and `k` smallest elements (first `k` elements). Calculate the difference between their sums.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Find k largest and k smallest without sorting, using multiple passes. This is O(n * k) time.
- **Optimized (Sorting):** Sort once, then directly access first k and last k elements. This is O(n log n) time.
- **Why it's better:** For small arrays (n <= 100), sorting is efficient and makes the solution simple and clear.

**1.4 Decomposition:**

1. Sort the array in ascending order
2. Sum the first `k` elements (smallest)
3. Sum the last `k` elements (largest)
4. Return absolute difference

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [5,2,2,4], k = 2`

- After sorting: `[2, 2, 4, 5]`

**2.2 Sort the Array:**

```python
nums.sort()  # [2, 2, 4, 5]
```

**2.3 Calculate Sum of k Smallest:**

```python
sum_smallest = sum(nums[:k])  # sum([2, 2]) = 4
```

**2.4 Calculate Sum of k Largest:**

```python
sum_largest = sum(nums[-k:])  # sum([4, 5]) = 9
```

**2.5 Return Absolute Difference:**

```python
return abs(sum_largest - sum_smallest)  # abs(9 - 4) = 5
```

**Time Complexity:** O(n log n) - Sorting  
**Space Complexity:** O(1) - In-place sort

