## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the length of the longest Fibonacci subarray, where each element (starting from the third) equals the sum of the two preceding elements. Subarrays of length 1 or 2 are always valid.

**1.1 Constraints & Complexity:**

* **Input Size:** The array `nums` can have up to 10^5 elements, with positive integers up to 10^9.
* **Time Complexity:** O(n) - We iterate through the array once, checking each position to see if it extends the current Fibonacci sequence.
* **Space Complexity:** O(1) - We only use a constant amount of extra space for tracking the current length.
* **Edge Case:** If the array has length <= 2, we return the array length directly.

**1.2 High-level approach:**

The goal is to scan through the array and track the longest contiguous sequence that follows the Fibonacci property. We maintain a running length and extend it when the current element equals the sum of the previous two.

![Visualization showing Fibonacci subarray with each element being the sum of previous two]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Check all possible subarrays by fixing start and end positions, then verify if each follows the Fibonacci property. This is O(n^2) time.
* **Optimized (Greedy):** Scan through the array once, maintaining the current valid length. When we find a position that extends the sequence, increment the length. When we find a break, update the maximum and reset. This is O(n) time.
* **Why it's better:** By processing in a single pass and maintaining state, we avoid checking all subarrays and achieve linear time complexity.

**1.4 Decomposition:**

1. Handle the edge case where array length <= 2.
2. Initialize the result and current length to 2 (minimum valid length).
3. Iterate from index 2 onwards, checking if nums[i] == nums[i-1] + nums[i-2].
4. If the condition holds, extend the current length.
5. Otherwise, update the maximum and reset the current length to 2.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 1, 1, 1, 2, 3, 5, 1]`

We initialize:
* `n = 8`
* `res = 2` (minimum valid length)
* `current_length = 2`

**2.2 Start Checking:**

We iterate from index 2 onwards, checking if each element extends the Fibonacci sequence.

**2.3 Trace Walkthrough:**

| Step | i | nums[i] | nums[i-1]+nums[i-2] | Match? | current_length | res |
|------|---|---------|---------------------|--------|----------------|-----|
| 1    | 2 | 1       | 1+1=2               | No     | 2              | 2   |
| 2    | 3 | 1       | 1+1=2               | No     | 2              | 2   |
| 3    | 4 | 2       | 1+1=2               | Yes    | 3              | 2   |
| 4    | 5 | 3       | 2+1=3               | Yes    | 4              | 2   |
| 5    | 6 | 5       | 3+2=5               | Yes    | 5              | 2   |
| 6    | 7 | 1       | 5+3=8               | No     | 2              | 5   |

At step 5, we find the longest Fibonacci subarray [1, 1, 2, 3, 5] with length 5.

**2.4 Increment and Loop:**

For each index i >= 2, we check if it extends the sequence. If yes, we increment current_length; otherwise, we reset it to 2.

**2.5 Return Result:**

After processing all positions, we return `res = 5`, representing the length of the longest Fibonacci subarray.
