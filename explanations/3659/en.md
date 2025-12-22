## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to determine if we can partition all elements of an array into groups such that each group contains exactly k distinct elements, and each element is assigned to exactly one group.

**1.1 Constraints & Complexity:**

- **Input Size:** Array length can be up to 10^5, and each element can be up to 10^5.
- **Time Complexity:** O(n) where n is the array length - we count frequencies and check each frequency once.
- **Space Complexity:** O(n) - we store frequency counts for each distinct element.
- **Edge Case:** If the total number of elements is not divisible by k, partitioning is impossible.

**1.2 High-level approach:**

The goal is to check if the frequency constraints allow us to form groups of k distinct elements. Each element can appear at most once per group, so if an element appears more times than the number of groups, it's impossible to partition.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible ways to assign elements to groups, which would be exponential.
- **Optimized Strategy:** Count the frequency of each element. If total elements is divisible by k and no element appears more than (n/k) times, partitioning is possible. This is O(n) time.
- **Optimization:** By checking frequency constraints upfront, we avoid exploring impossible partitions.

**1.4 Decomposition:**

1. Check if total number of elements is divisible by k (if not, return False).
2. Count the frequency of each element in the array.
3. Calculate the number of groups needed: n / k.
4. Check if any element appears more than the number of groups (if yes, return False).
5. If all constraints are satisfied, return True.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1,2,3,4], k = 2`

- Total elements: 4
- Number of groups needed: 4 / 2 = 2
- Frequencies: {1:1, 2:1, 3:1, 4:1}

**2.2 Start Checking:**

We count frequencies and verify constraints.

**2.3 Trace Walkthrough:**

| Element | Frequency | Max Groups | Valid? |
|---------|-----------|------------|--------|
| 1 | 1 | 2 | Yes (1 <= 2) |
| 2 | 1 | 2 | Yes (1 <= 2) |
| 3 | 1 | 2 | Yes (1 <= 2) |
| 4 | 1 | 2 | Yes (1 <= 2) |

All elements appear at most 2 times (number of groups), so partitioning is possible.

For `nums = [3,5,2,2], k = 2`:
- Total elements: 4, divisible by 2 ✓
- Number of groups: 2
- Frequencies: {3:1, 5:1, 2:2}
- All frequencies <= 2 ✓
- Result: True

For `nums = [1,5,2,3], k = 3`:
- Total elements: 4, NOT divisible by 3 ✗
- Result: False

**2.4 Increment and Loop:**

The algorithm checks each element's frequency once, ensuring no element appears too many times.

**2.5 Return Result:**

For `nums = [1,2,3,4], k = 2`, the result is True. We can form 2 groups: [1,2] and [3,4], each with 2 distinct elements.

