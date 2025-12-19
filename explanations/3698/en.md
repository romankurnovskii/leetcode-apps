## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to split an array into two subarrays: left (strictly increasing) and right (strictly decreasing), such that the absolute difference between their sums is minimized.

**1.1 Constraints & Complexity:**

- **Input Size:** Array length can be up to 10^5.
- **Time Complexity:** O(n) - we use two pointers that each traverse the array once.
- **Space Complexity:** O(1) - we only use a few variables for sums and pointers.
- **Edge Case:** If no valid split exists (not a mountain array), return -1.

**1.2 High-level approach:**

The goal is to find the peak of the array and split there, with the left part strictly increasing and right part strictly decreasing.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible split points and check validity, calculating sums each time. This would be O(n^2).
- **Optimized Strategy:** Use two pointers from both ends, expanding while maintaining strict increase/decrease, then handle the peak element. This is O(n).
- **Optimization:** Two pointers allow us to process the array in a single pass, accumulating sums as we go.

**1.4 Decomposition:**

1. Use two pointers: left starts at 0, right starts at n-1.
2. Expand left pointer while array is strictly increasing, accumulating left sum.
3. Expand right pointer while array is strictly decreasing, accumulating right sum.
4. Handle the peak element (where pointers meet): try assigning it to either side.
5. Return the minimum absolute difference, or -1 if no valid split exists.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1,3,2]`

- Left pointer l=0, right pointer r=2, lsum=0, rsum=0.

**2.2 Start Processing:**

We expand both pointers while maintaining strict increase/decrease.

**2.3 Trace Walkthrough:**

| Step | Action             | l   | r   | lsum | rsum | nums[l] | nums[r] |
| ---- | ------------------ | --- | --- | ---- | ---- | ------- | ------- |
| 1    | Expand left (1<3)  | 0→1 | 2   | 1    | 0    | 3       | 2       |
| 2    | Expand right (3>2) | 1   | 2→1 | 1    | 2    | 3       | 3       |
| 3    | Pointers meet      | 1   | 1   | 1    | 2    | 3       | 3       |

Since l==r, we have a single peak. Try both options:

- Option 1: lsum + nums[l] = 1+3=4, rsum=2, diff=|4-2|=2
- Option 2: lsum=1, rsum + nums[r]=2+3=5, diff=|1-5|=4
- Minimum: 2

**2.4 Increment and Loop:**

The algorithm handles all cases: single peak, flat peak, or invalid.

**2.5 Return Result:**

The result is 2, the minimum absolute difference.
