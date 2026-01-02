## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array and a target frequency k, we need to find the minimum operations to make each number appear at least k times.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^5 elements.
- **Time Complexity:** O(n) - we count frequencies once, where n is the array length.
- **Space Complexity:** O(n) - we need to store frequency counts.
- **Edge Case:** If k is 0, return 0. If k is greater than array length, return -1 (impossible).

**1.2 High-level approach:**

The goal is to count how many additional occurrences of each number are needed to reach frequency k, then sum these operations.

![Frequency equalization visualization](https://assets.leetcode.com/static_assets/others/freq-equal.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible ways to add elements. This is impractical.
- **Optimized Strategy:** Count current frequencies and calculate how many more are needed for each number. This is O(n) time.
- **Optimization:** By counting frequencies first and calculating needed operations, we solve efficiently.

**1.4 Decomposition:**

1. Count the frequency of each number in the array.
2. For each number, if frequency < k, calculate operations needed = k - frequency.
3. Sum all operations needed.
4. Return the total.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 2, 2, 3]`, `k = 3`

- Frequency counts: `{1: 1, 2: 2, 3: 1}`
- Result variable: `res = 0`

**2.2 Start Checking:**

We iterate through frequency counts.

**2.3 Trace Walkthrough:**

| Step | Number | Frequency | Needed | Operations | res |
| ---- | ------ | --------- | ------ | ---------- | --- |
| 1    | 1 | 1 | 3 | 2 | 2 |
| 2    | 2 | 2 | 3 | 1 | 3 |
| 3    | 3 | 1 | 3 | 2 | 5 |

**2.4 Increment and Loop:**

After processing each number, we add operations to the total.

**2.5 Return Result:**

The result is `5`, which is the minimum operations to make each number appear at least 3 times.

