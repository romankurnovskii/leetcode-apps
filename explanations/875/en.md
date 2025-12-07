## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** Piles array can have up to 10^4 elements, each pile can have up to 10^9 bananas, h can be up to 10^9.
* **Time Complexity:** O(n * log(max(piles))) - Binary search over possible speeds, and for each speed we check all piles.
* **Space Complexity:** O(1) - We only use a constant amount of extra space.
* **Edge Case:** If h equals the number of piles, Koko must eat each pile in one hour, so speed = max(piles).

**1.2 High-level approach:**

The goal is to find the minimum eating speed k such that Koko can finish all bananas within h hours. We use binary search on the possible speed values.

![Binary search on speed values showing how we find the minimum valid speed]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Try every possible speed from 1 to max(piles). This is O(n * max(piles)) time.
* **Optimized (Binary Search):** Binary search on speed range [1, max(piles)]. For each candidate speed, calculate total hours needed. This is O(n * log(max(piles))) time.
* **Why it's better:** Binary search reduces the number of speed values we need to test from max(piles) to log(max(piles)).

**1.4 Decomposition:**

1. Set search range: left = 1, right = max(piles).
2. While left <= right:
   - Calculate mid speed.
   - Calculate total hours needed at this speed.
   - If hours <= h, try slower speed (right = mid - 1).
   - Otherwise, try faster speed (left = mid + 1).
3. Return the minimum valid speed.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: piles = [3,6,7,11], h = 8

We initialize:
* `left = 1`
* `right = 11` (max of piles)
* `res = 11`

**2.2 Start Checking/Processing:**

We enter a while loop while `left <= right`.

**2.3 Trace Walkthrough:**

| Step | left | right | mid | Hours Calculation | Hours | Action |
|------|------|-------|-----|-------------------|-------|--------|
| 1 | 1 | 11 | 6 | ceil(3/6)+ceil(6/6)+ceil(7/6)+ceil(11/6) | 1+1+2+2=6 | hours <= 8, right = 5 |
| 2 | 1 | 5 | 3 | ceil(3/3)+ceil(6/3)+ceil(7/3)+ceil(11/3) | 1+2+3+4=10 | hours > 8, left = 4 |
| 3 | 4 | 5 | 4 | ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) | 1+2+2+3=8 | hours <= 8, right = 3 |
| 4 | 4 | 3 | - | left > right, exit | - | Return res = 4 |

**2.4 Increment and Loop:**

After each speed test, we adjust the search range and try again.

**2.5 Return Result:**

After binary search completes, `res = 4` is returned as the minimum eating speed.

