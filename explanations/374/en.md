## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** n can be up to 2^31 - 1.
* **Time Complexity:** O(log n) - Binary search reduces the search space by half in each iteration.
* **Space Complexity:** O(1) - We only use a constant amount of extra space.
* **Edge Case:** If n = 1, the answer is 1 since there's only one possible number.

**1.2 High-level approach:**

The goal is to find the picked number by using binary search with the guess API. We narrow down the search range based on whether our guess is too high or too low.

![Binary search visualization showing how the search range narrows with each guess]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Try every number from 1 to n sequentially. This takes O(n) time.
* **Optimized (Binary Search):** Use binary search to eliminate half of the remaining numbers with each guess. This takes O(log n) time.
* **Why it's better:** Binary search is exponentially faster, especially for large n.

**1.4 Decomposition:**

1. Initialize search range: left = 1, right = n.
2. Calculate mid point.
3. Call guess(mid) to get feedback.
4. If guess returns 0, we found the number.
5. If guess returns -1, the number is smaller, so set right = mid - 1.
6. If guess returns 1, the number is larger, so set left = mid + 1.
7. Repeat until found.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: n = 10, pick = 6

We initialize:
* `left = 1`
* `right = 10`

**2.2 Start Checking/Processing:**

We enter a while loop while `left <= right`.

**2.3 Trace Walkthrough:**

| Step | left | right | mid | guess(mid) | Action |
|------|------|-------|-----|------------|--------|
| 1 | 1 | 10 | 5 | 1 (too low) | left = 6 |
| 2 | 6 | 10 | 8 | -1 (too high) | right = 7 |
| 3 | 6 | 7 | 6 | 0 (found!) | Return 6 |

**2.4 Increment and Loop:**

After each guess, we adjust left or right based on the result and calculate a new mid.

**2.5 Return Result:**

When guess(mid) returns 0, we return mid = 6.

