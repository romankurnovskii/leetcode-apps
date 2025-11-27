## Explanation

### Strategy (The "Why")

Given an array `gain` where `gain[i]` is the net gain in altitude between points $i$ and $i+1$, we need to find the highest altitude reached. We start at altitude 0.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be between $1$ and $100$.
- **Value Range:** Each gain value is between $-100$ and $100$.
- **Time Complexity:** $O(n)$ - We iterate through the gain array once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for variables.
- **Edge Case:** If all gains are negative, the highest altitude is 0 (starting altitude).

**1.2 High-level approach:**

The goal is to find the maximum altitude reached during the journey.

![Highest Altitude](https://assets.leetcode.com/uploads/2021/06/26/largest-altitude.png)

We track the current altitude as we process each gain. The current altitude starts at 0, and we add each gain to it. We keep track of the maximum altitude seen.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must process each gain sequentially.
- **Optimized Strategy (Prefix Sum):** Calculate the running sum (prefix sum) of gains, which represents the altitude at each point. Track the maximum. This is the natural and efficient approach.
- **Why it's better:** The prefix sum approach is straightforward and optimal. We process each gain once, maintaining the current altitude and maximum altitude.

**1.4 Decomposition:**

1. Initialize `current_altitude = 0` and `max_altitude = 0`.
2. Iterate through each gain value.
3. Add the gain to `current_altitude`.
4. Update `max_altitude` to be the maximum of `max_altitude` and `current_altitude`.
5. Return `max_altitude`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $gain = [-5,1,5,0,-7]$

We initialize:
- `current_altitude = 0`
- `max_altitude = 0`

**2.2 Start Processing:**

We iterate through each gain.

**2.3 Trace Walkthrough:**

| Gain | current_altitude Before | current_altitude After | max_altitude |
|------|------------------------|----------------------|--------------|
| -5 | 0 | $0 + (-5) = -5$ | 0 |
| 1 | -5 | $-5 + 1 = -4$ | 0 |
| 5 | -4 | $-4 + 5 = 1$ | 1 |
| 0 | 1 | $1 + 0 = 1$ | 1 |
| -7 | 1 | $1 + (-7) = -6$ | 1 |

**2.4 Altitude Progression:**

- Start: altitude = 0
- After gain -5: altitude = -5
- After gain 1: altitude = -4
- After gain 5: altitude = 1 (highest so far)
- After gain 0: altitude = 1
- After gain -7: altitude = -6

**2.5 Return Result:**

We return 1, which is the highest altitude reached during the journey.

> **Note:** This is essentially a prefix sum problem. The altitude at each point is the cumulative sum of gains from the start, and we're finding the maximum of these cumulative sums.
