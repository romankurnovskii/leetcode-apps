## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The array `nums` can have up to 100 elements.
* **Time Complexity:** O(n^3) where n is the array length. We try all possible p and q positions (O(n^2)) and for each, check three segments (O(n)).
* **Space Complexity:** O(1) - We only use a constant amount of extra space.
* **Edge Case:** Each segment must have at least 2 elements for "strictly" to make sense, so p and q must leave enough elements.

**1.2 High-level approach:**

The goal is to check if an array can be divided into three segments: strictly increasing, strictly decreasing, then strictly increasing. We try all possible split points p and q, and verify if the three segments meet the requirements.

![Visualization showing array divided into three segments: increasing, decreasing, then increasing]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Try all possible p and q positions, check if each segment is strictly monotonic. This is O(n^3) which is acceptable for n <= 100.
* **Optimized:** Same as brute force - the problem constraints are small enough that trying all combinations is efficient.
* **Why it's better:** For small input sizes, the brute force approach is simple, clear, and efficient enough.

**1.4 Decomposition:**

1. Try all possible positions for p (must leave at least 2 elements after it) and q (must leave at least 1 element after it).
2. For each (p, q) pair, check if nums[0...p] is strictly increasing.
3. Check if nums[p...q] is strictly decreasing.
4. Check if nums[q...n-1] is strictly increasing.
5. If all three conditions are met, return true.
6. If no valid (p, q) pair is found, return false.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 3, 5, 4, 2, 6]`

We initialize:
* `n = 6`
* Try p in range(1, 4) and q in range(p+1, 5)

**2.2 Start Checking:**

We try p = 2, q = 4:
* nums[0...2] = [1, 3, 5] - check if strictly increasing
* nums[2...4] = [5, 4, 2] - check if strictly decreasing
* nums[4...5] = [2, 6] - check if strictly increasing

**2.3 Trace Walkthrough:**

| p   | q   | Segment 1 | Check 1 | Segment 2 | Check 2 | Segment 3 | Check 3 | Valid? |
| --- | --- | --------- | ------- | --------- | ------- | --------- | ------- | ------ |
| 2   | 4   | [1,3,5]   | 1<3<5 ✓ | [5,4,2]   | 5>4>2 ✓ | [2,6]     | 2<6 ✓   | Yes    |

**2.4 Increment and Loop:**

We continue trying other (p, q) pairs. Once we find a valid one, we return true immediately.

**2.5 Return Result:**

Since we found a valid (p=2, q=4) that satisfies all conditions, we return `true`.
