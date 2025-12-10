## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** Delivery counts `d[i]` can be up to 10^9, recharge intervals `r[i]` up to 3 * 10^4.
* **Time Complexity:** O(log(T_max) * C) where T_max is the maximum possible time and C is constant for the check function. Using binary search on time.
* **Space Complexity:** O(1) - We only use a constant amount of extra space.
* **Edge Case:** When both drones recharge at the same hours (multiples of LCM), those hours are unavailable to both.

**1.2 High-level approach:**

The goal is to find the minimum time T such that both drones can complete their required deliveries. We use binary search on the time T, and for each candidate time, check if both drones have enough available hours (accounting for recharge times and overlap).

![Visualization showing timeline with drone availability, recharge periods, and overlap calculation]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Try each time value from 1 to maximum needed time. This is O(T_max) which is too slow for large T_max.
* **Optimized (Binary Search):** Use binary search on time T, and for each candidate, calculate available hours using inclusion-exclusion principle. This is O(log(T_max)).
* **Why it's better:** Binary search reduces the search space exponentially, making it feasible for large delivery counts.

**1.4 Decomposition:**

1. Use binary search on the total time T.
2. For each candidate time T, calculate available hours for each drone (T - floor(T/r[i])).
3. Calculate overlapping available hours using inclusion-exclusion (hours when both are available).
4. Check if each drone has enough hours individually and if total available hours (accounting for overlap) >= total deliveries needed.
5. Adjust binary search bounds based on the check result.
6. Return the minimum valid time.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `d = [3, 1]`, `r = [2, 3]`

We initialize:
* `lcm_r = lcm(2, 3) = 6`
* Binary search: `left = max(3, 1) = 3`, `right = 10^18`

**2.2 Start Binary Search:**

We try T = 5 as a candidate.

**2.3 Trace Walkthrough:**

| T   | x1 (drone 1) | x2 (drone 2) | x3 (both)   | Check                        | Result |
| --- | ------------ | ------------ | ----------- | ---------------------------- | ------ |
| 5   | 5-2=3        | 5-1=4        | 5-(2+1-0)=2 | 3>=3 ✓, 4>=1 ✓, (3+4-2)>=4 ✓ | Valid  |

For T = 4:
| T   | x1    | x2    | x3          | Check  | Result  |
| --- | ----- | ----- | ----------- | ------ | ------- |
| 4   | 4-2=2 | 4-1=3 | 4-(2+1-0)=1 | 2>=3 ✗ | Invalid |

**2.4 Increment and Loop:**

We continue binary search, adjusting bounds based on whether the time is valid.

**2.5 Return Result:**

After binary search completes, we return `res = 5`, which is the minimum time needed.
