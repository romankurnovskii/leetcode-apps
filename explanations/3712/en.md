# Problem 3712: Sum of Elements With Frequency Divisible by K

**Difficulty:** Easy  
**LeetCode Link:** https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find all elements whose frequency (number of occurrences) in the array is divisible by `k`, and sum up all occurrences of those elements.

**1.1 Constraints & Complexity:**

- **Input Size:** We have at most 100 elements, and each element is between 1 and 100.
- **Time Complexity:** $O(n)$ where $n$ is the number of elements. We count frequencies in one pass and then iterate through unique elements.
- **Space Complexity:** $O(n)$ for storing the frequency counter (at most $n$ distinct elements).
- **Edge Case:** If no element has a frequency divisible by `k`, we return 0.

**1.2 High-level approach:**

The goal is to count how many times each element appears, check if that count is divisible by `k`, and if so, add all occurrences of that element to the result.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each unique element, count its occurrences by iterating through the entire array. This is $O(n^2)$ time.
- **Optimized Strategy:** Use a hash map (Counter) to count frequencies in a single pass, then iterate through the unique elements. This is $O(n)$ time.
- **Optimization:** Using a hash map allows us to count all frequencies in one pass, reducing time complexity from $O(n^2)$ to $O(n)$.

**1.4 Decomposition:**

1. Count the frequency of each element in the array using a hash map.
2. Iterate through each unique element and its frequency.
3. Check if the frequency is divisible by `k` (using modulo operator).
4. If divisible, add the element multiplied by its frequency to the result (since we include all occurrences).
5. Return the total sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `nums = [1, 2, 2, 3, 3, 3, 3, 4]`, `k = 2`.

- Frequency counter: `{1: 1, 2: 2, 3: 4, 4: 1}`
- Initialize `res = 0`

**2.2 Start Checking:**

We begin iterating through each unique element and its frequency.

**2.3 Trace Walkthrough:**

| Element | Frequency | Is Frequency % k == 0? | Contribution to Sum | Current `res` |
|---------|-----------|------------------------|---------------------|---------------|
| 1       | 1         | No (1 % 2 = 1)        | 0                   | 0             |
| 2       | 2         | Yes (2 % 2 = 0)       | 2 × 2 = 4           | 4             |
| 3       | 4         | Yes (4 % 2 = 0)       | 3 × 4 = 12          | 16            |
| 4       | 1         | No (1 % 2 = 1)        | 0                   | 16            |

**2.4 Increment and Loop:**

After processing each element, we move to the next unique element in the frequency counter until all elements have been processed.

**2.5 Return Result:**

After processing all elements, `res = 16`, which is the sum of all elements (2 and 3) whose frequencies are divisible by `k = 2`. Specifically, we include both occurrences of 2 (2 + 2 = 4) and all four occurrences of 3 (3 + 3 + 3 + 3 = 12), giving us a total of 16.

