## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= n <= 1000`.
- **Time Complexity:** O(n) - we iterate n/2 times to create pairs.
- **Space Complexity:** O(n) - we create an array of size n.
- **Edge Case:** If n = 1, return [0]. If n = 2, return [1, -1].

**1.2 High-level approach:**

The goal is to create an array of n unique integers that sum to zero. The key insight is to use pairs of positive and negative numbers that cancel each other out. For even n, we can use n/2 pairs. For odd n, we use (n-1)/2 pairs plus 0.

![Visualization showing how positive and negative number pairs cancel out to sum to zero, with 0 added for odd n]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of n unique integers and check if they sum to zero. This is exponential and impractical.
- **Optimized Strategy:** Use symmetric pairs (x, -x) for even n, or pairs plus 0 for odd n. This is simple and efficient.
- **Why it's better:** The symmetric pair approach guarantees a sum of zero and is straightforward to implement in O(n) time.

**1.4 Decomposition:**

1. For each integer from 1 to n/2, add both the positive and negative versions to the result.
2. If n is odd, add 0 to the result.
3. Return the result array.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 5`.

We initialize:
- `res = []`

**2.2 Start Checking:**

Create pairs of positive and negative numbers.

**2.3 Trace Walkthrough:**

| Step | i | Positive number | Negative number | res after step |
|------|---|-----------------|------------------|----------------|
| 1 | 1 | 1 | -1 | [1, -1] |
| 2 | 2 | 2 | -2 | [1, -1, 2, -2] |

After creating pairs:
- We have 2 pairs: [1, -1, 2, -2]
- Since n = 5 is odd, we need to add 0
- Final: [1, -1, 2, -2, 0]

**2.4 Increment and Loop:**

Continue until we've created n/2 pairs.

**2.5 Return Result:**

Return `res = [1, -1, 2, -2, 0]` - an array of 5 unique integers that sum to zero (1 + (-1) + 2 + (-2) + 0 = 0).

