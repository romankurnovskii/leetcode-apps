## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the length of the longest subarray where the number of distinct even numbers equals the number of distinct odd numbers.

**1.1 Constraints & Complexity:**

* **Input Size:** The array `nums` can have up to 1500 elements, with values between 1 and 10^5.
* **Time Complexity:** O(n^2) - We check all possible subarrays by fixing start and end positions, and use sets to track distinct values in O(1) per operation.
* **Space Complexity:** O(n) - In the worst case, we store up to n distinct values in the sets.
* **Edge Case:** If no subarray is balanced (e.g., all numbers are even), we return 0.

**1.2 High-level approach:**

The goal is to check all possible subarrays and find the longest one where distinct even numbers equal distinct odd numbers. We use sets to efficiently track distinct values as we extend subarrays.


**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Check all possible subarrays by fixing start and end positions, then count distinct even and odd numbers for each. This is O(n^2) time, which is acceptable for n <= 1500.
* **Optimized (Same as brute force for this constraint):** The brute force approach is already optimal for the given constraints. We can optimize by maintaining sets as we extend subarrays, avoiding redundant counting.
* **Why it's acceptable:** With n <= 1500, O(n^2) = 2.25 million operations is efficient enough.

**1.4 Decomposition:**

1. For each possible starting position i in the array.
2. Initialize empty sets for distinct even and odd numbers.
3. Extend the subarray by moving the end position j from i to n-1.
4. Add each number to the appropriate set (even or odd).
5. Check if the sizes of both sets are equal, and update the maximum length.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [2, 5, 4, 3]`

We initialize:
* `n = 4`
* `res = 0`

**2.2 Start Checking:**

We iterate through each starting position i from 0 to n-1.

**2.3 Trace Walkthrough:**

| Step | i   | j   | nums[j] | even_set | odd_set | Balanced?  | res |
| ---- | --- | --- | ------- | -------- | ------- | ---------- | --- |
| 1    | 0   | 0   | 2       | {2}      | {}      | No         | 0   |
| 2    | 0   | 1   | 5       | {2}      | {5}     | Yes (1==1) | 2   |
| 3    | 0   | 2   | 4       | {2,4}    | {5}     | No         | 2   |
| 4    | 0   | 3   | 3       | {2,4}    | {5,3}   | Yes (2==2) | 4   |
| 5    | 1   | 1   | 5       | {}       | {5}     | No         | 4   |
| 6    | 1   | 2   | 4       | {4}      | {5}     | Yes (1==1) | 4   |
| 7    | 1   | 3   | 3       | {4}      | {5,3}   | No         | 4   |

At step 4, we find the longest balanced subarray [2, 5, 4, 3] with length 4.

**2.4 Increment and Loop:**

For each starting position i, we extend the subarray by incrementing j, adding numbers to sets and checking balance.

**2.5 Return Result:**

After checking all subarrays, we return `res = 4`, representing the length of the longest balanced subarray.
