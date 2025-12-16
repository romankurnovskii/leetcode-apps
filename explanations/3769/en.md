## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to sort integers by their binary reflection (reversing binary digits and interpreting as decimal). If two numbers have the same reflection, sort by original value.

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= nums.length <= 100`, `1 <= nums[i] <= 10^9`
- **Time Complexity:** O(n log n * log max(nums)) - Sort with comparison function
- **Space Complexity:** O(1) - Sorting in-place
- **Edge Case:** All numbers have same reflection

**1.2 High-level approach:**

For each number, compute its binary reflection. Sort by reflection value first, then by original value if reflections are equal.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Precompute all reflections, store in separate array, sort indices. This is O(n log n) but uses extra space.
- **Optimized (Custom Sort Key):** Use a key function that computes reflection on-the-fly during sorting. This is O(n log n) with O(1) extra space.
- **Why it's better:** The custom key function is clean and doesn't require precomputation or extra storage.

**1.4 Decomposition:**

1. Define function to compute binary reflection
2. Sort array using custom key: (reflection, original_value)
3. Return sorted array

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [4,5,4]`

- Binary reflections:
  - 4 → `100` → reversed `001` → 1
  - 5 → `101` → reversed `101` → 5
  - 4 → `100` → reversed `001` → 1

**2.2 Define Binary Reflection Function:**

```python
def binary_reflection(n):
    binary = bin(n)[2:]  # Remove '0b' prefix: "100"
    reversed_binary = binary[::-1]  # "001"
    return int(reversed_binary, 2)  # 1
```

**2.3 Sort with Custom Key:**

```python
return sorted(nums, key=lambda x: (binary_reflection(x), x))
```

Sort key is `(reflection, original)`:
- `(1, 4)` for first 4
- `(5, 5)` for 5
- `(1, 4)` for second 4

Sorting: `(1, 4) < (1, 4) < (5, 5)` → `[4, 4, 5]`

**2.4 Return Result:**

The sorted array maintains order: same reflection values are sorted by original value.

**Time Complexity:** O(n log n * log max(nums)) - Sort with O(log max) comparison  
**Space Complexity:** O(1) - In-place sort

