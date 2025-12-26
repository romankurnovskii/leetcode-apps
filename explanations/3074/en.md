## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the minimum number of boxes needed to pack all apples. Since apples from the same pack can be distributed into different boxes, we only care about the total number of apples, not how they were originally packed.

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= n == apple.length <= 50`, `1 <= m == capacity.length <= 50`, and each value is between 1 and 50.
- **Time Complexity:** O(n + m log m) where n is the number of apple packs and m is the number of boxes - we sum apples in O(n) and sort boxes in O(m log m).
- **Space Complexity:** O(1) - we only use a constant amount of extra space (sorting may use O(m) but we consider it O(1) for in-place sort).
- **Edge Case:** If all apples fit in a single box, we return 1.

**1.2 High-level approach:**

The goal is to use a greedy strategy: always select boxes with the largest capacity first. This minimizes the number of boxes needed because larger boxes can hold more apples.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of boxes to find the minimum. This would be exponential O(2^m) in the worst case.
- **Optimized Strategy:** Sort boxes by capacity in descending order, then greedily select boxes until all apples are packed. This is O(n + m log m) time.
- **Optimization:** By always choosing the largest available box, we minimize the number of boxes needed. This greedy approach is optimal because if a smaller box is chosen at any step, it can always be replaced by a larger box to achieve a better result.

**1.4 Decomposition:**

1. Calculate the total number of apples needed by summing all apple packs.
2. Sort the boxes by capacity in descending order (largest first).
3. Iterate through sorted boxes, subtracting each box's capacity from remaining apples.
4. Count how many boxes are used until all apples are packed.
5. Return the count of boxes used.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `apple = [1, 3, 2]`, `capacity = [4, 3, 1, 5, 2]`

- Total apples needed: 1 + 3 + 2 = 6
- Boxes sorted by capacity (descending): [5, 4, 3, 2, 1]
- Remaining apples: 6
- Boxes used: 0

**2.2 Start Checking:**

We begin selecting boxes starting with the largest capacity.

**2.3 Trace Walkthrough:**

| Box Capacity | Remaining Apples Before | Remaining Apples After | Boxes Used |
| ------------ | ----------------------- | ---------------------- | ---------- |
| 5            | 6                       | 6 - 5 = 1              | 1          |
| 4            | 1                       | 1 - 4 = -3 (≤ 0)       | 2          |

**2.4 Increment and Loop:**

After selecting the box with capacity 5, we have 1 apple remaining. We then select the box with capacity 4, which can hold the remaining 1 apple (and has extra space). Since remaining apples is now ≤ 0, we stop.

**2.5 Return Result:**

We used 2 boxes (capacities 5 and 4) to pack all 6 apples. The result is `res = 2`.
