## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array of integers, we need to find the minimum number of operations to make all elements distinct. Each operation can remove one occurrence of a number.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^5 elements.
- **Time Complexity:** O(n) - we iterate through the array once to count frequencies, where n is the array length.
- **Space Complexity:** O(n) - we need to store frequency counts for each unique number.
- **Edge Case:** If an element appears only once, we cannot make it distinct by removing it (would need to return -1). If all elements are already distinct, return 0.

**1.2 High-level approach:**

The goal is to count how many duplicate elements need to be removed. For each number that appears more than once, we need to remove all but one occurrence.

![Array distinctness visualization](https://assets.leetcode.com/static_assets/others/array-distinct.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible removal combinations. This is exponential and impractical.
- **Optimized Strategy:** Count frequencies and for each number with frequency > 1, calculate how many operations needed to reduce it to 1. This is O(n) time.
- **Optimization:** By grouping by frequency and calculating operations needed per group, we solve in linear time.

**1.4 Decomposition:**

1. Count the frequency of each number in the array.
2. For each frequency count:
   - If frequency is 1, we cannot remove it (return -1 if any number has frequency 1).
   - If frequency > 1, calculate operations needed: (freq + 2) // 3 operations.
3. Sum all operations needed.
4. Return the total.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 2, 2, 3, 3, 3]`

- Frequency counts: `{1: 1, 2: 2, 3: 3}`
- Result variable: `res = 0`

**2.2 Start Checking:**

We iterate through frequency counts and calculate operations.

**2.3 Trace Walkthrough:**

| Step | Number | Frequency | Operations | res |
| ---- | ------ | --------- | ---------- | --- |
| 1    | 1      | 1         | Check: freq == 1? | Return -1 if any |
| 2    | 2      | 2         | (2+2)//3 = 1 | 1 |
| 3    | 3      | 3         | (3+2)//3 = 1 | 2 |

**2.4 Increment and Loop:**

After processing each frequency, we add the operations to the total.

**2.5 Return Result:**

The result is `2` (or -1 if any number has frequency 1), which represents the minimum operations to make all elements distinct.
