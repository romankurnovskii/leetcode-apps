## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= cardPoints.length <= 10^5`, `1 <= k <= cardPoints.length`.
- **Value Range:** `1 <= cardPoints[i] <= 10^4`.
- **Time Complexity:** O(n) where n is the length of cardPoints. We calculate the window sum and slide it once.
- **Space Complexity:** O(1) - we only use a few variables.
- **Edge Case:** If k equals the array length, return the sum of all cards.

**1.2 High-level approach:**

The goal is to maximize the sum of k cards taken from either end of the array. The key insight is that taking k cards from the ends is equivalent to leaving a subarray of length (n - k) in the middle. We find the minimum sum of such a subarray, then subtract it from the total sum to get the maximum score.

![Visualization showing how taking k cards from ends leaves a window of (n-k) cards in the middle, and we want to minimize this window's sum]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of taking cards from left and right ends. This is exponential.
- **Optimized Strategy:** Use a sliding window to find the minimum sum of the middle subarray of length (n - k), then subtract from total. This takes O(n) time.
- **Why it's better:** The sliding window approach efficiently finds the minimum middle subarray in a single pass, converting the problem from exponential to linear time.

**1.4 Decomposition:**

1. Calculate the total sum of all cards.
2. Calculate the sum of the first (n - k) cards (initial window).
3. Slide the window from left to right, tracking the minimum window sum.
4. Return total_sum - min_window_sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `cardPoints = [1, 2, 3, 4, 5, 6, 1]`, `k = 3`.

We need to take 3 cards from the ends. This means leaving a window of length 7 - 3 = 4 in the middle.

**2.2 Start Checking:**

Calculate initial window sum and slide to find minimum.

**2.3 Trace Walkthrough:**

| Step | Window start | Window end | Window (indices) | Window sum | Min sum so far |
|------|--------------|------------|------------------|------------|----------------|
| 1 | 0 | 3 | [1,2,3,4] | 10 | 10 |
| 2 | 1 | 4 | [2,3,4,5] | 14 | 10 |
| 3 | 2 | 5 | [3,4,5,6] | 18 | 10 |
| 4 | 3 | 6 | [4,5,6,1] | 16 | 10 |

Total sum = 1 + 2 + 3 + 4 + 5 + 6 + 1 = 22
Minimum window sum = 10 (window [1,2,3,4])
Maximum score = 22 - 10 = 12

This corresponds to taking cards [1, 6, 5] from the ends (left: 1, right: 6 and 5).

**2.4 Increment and Loop:**

Slide the window until we've checked all possible positions.

**2.5 Return Result:**

Return `res = 12` - the maximum score achievable by taking 3 cards from the ends.

