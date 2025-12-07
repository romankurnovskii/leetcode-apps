## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `2 <= costs.length <= 100`, and `costs.length` is even.
- **Value Range:** `1 <= aCost_i, bCost_i <= 1000`.
- **Time Complexity:** O(n log n) where n is the number of people. Sorting takes O(n log n) time.
- **Space Complexity:** O(1) - we sort in place.
- **Edge Case:** If there are only 2 people, send one to each city.

**1.2 High-level approach:**

The goal is to minimize the total cost of sending exactly n people to city A and n people to city B. The key insight is to sort people by the difference `(costA - costB)`. People with a large negative difference (much cheaper to go to A) should go to A, and people with a large positive difference (much cheaper to go to B) should go to B.

![Visualization showing how sorting by cost difference helps determine optimal city assignment]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible ways to assign n people to city A and n to city B. This takes O(C(2n, n)) time, which is exponential.
- **Optimized Strategy:** Sort by the difference `(costA - costB)`, send the first n to city A and the rest to city B. This takes O(n log n) time.
- **Why it's better:** The greedy approach of sorting by difference ensures we minimize the total cost by prioritizing people who save the most by going to their preferred city.

**1.4 Decomposition:**

1. Sort the costs array by the difference `(costA - costB)`.
2. Send the first n people (smallest differences, meaning cheaper to go to A) to city A.
3. Send the remaining n people (largest differences, meaning cheaper to go to B) to city B.
4. Return the total cost.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `costs = [[10, 20], [30, 200], [400, 50], [30, 20]]`.

We need to send 2 people to city A and 2 to city B (n = 2).

**2.2 Start Checking:**

Sort by difference `(costA - costB)`.

**2.3 Trace Walkthrough:**

| Person | costA | costB | Difference (costA - costB) | Sorted order | Assignment |
|--------|-------|-------|---------------------------|--------------|------------|
| 0 | 10 | 20 | -10 | 1 | City A |
| 1 | 30 | 200 | -170 | 0 | City A |
| 2 | 400 | 50 | 350 | 3 | City B |
| 3 | 30 | 20 | 10 | 2 | City B |

After sorting by difference:
- Person 1: difference = -170 (cheapest to go to A) -> City A, cost = 30
- Person 0: difference = -10 (cheaper to go to A) -> City A, cost = 10
- Person 3: difference = 10 (cheaper to go to B) -> City B, cost = 20
- Person 2: difference = 350 (cheapest to go to B) -> City B, cost = 50

**2.4 Increment and Loop:**

Calculate total: 30 + 10 + 20 + 50 = 110.

**2.5 Return Result:**

Return `res = 110` - the minimum total cost.

