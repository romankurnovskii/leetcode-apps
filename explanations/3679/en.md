## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the minimum number of arrivals to discard so that in every sliding window of `w` days, each item type appears at most `m` times among kept arrivals.

**1.1 Constraints & Complexity:**

- **Input Size:** `arrivals.length <= 10^5`, `1 <= w <= arrivals.length`, `1 <= m <= w`
- **Time Complexity:** O(n) - Single pass through arrivals with sliding window
- **Space Complexity:** O(max(arrivals)) - Counter array for item types
- **Edge Case:** Empty arrivals array returns 0

**1.2 High-level approach:**

We use a sliding window approach with a counter to track item frequencies. When an item arrives, we check if keeping it would violate the constraint. If so, we discard it (mark as 0) and don't add it to the counter. When items leave the window, we only decrement the counter if they were kept (not 0).

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each arrival, check all windows containing it to see if keeping it violates constraints. This is O(n * w) time.
- **Optimized (Sliding Window):** Maintain a counter for the current window. When adding an item, if its count is already `m`, we must discard it. This is O(n) time.
- **Why it's better:** We only need to check the current item's count, not all windows, because if an item type appears `m` times in the current window, adding one more would violate the constraint.

**1.4 Decomposition:**

1. Initialize counter array for item types
2. For each arrival, remove items that left the window
3. Check if current item can be kept (count < m)
4. If yes, increment counter; if no, discard (mark as 0) and increment result
5. Return total discards

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `arrivals = [1,2,3,3,3,4], w = 3, m = 2`

- Initialize `ctr = [0] * (max(arrivals) + 1)` to count each item type
- Initialize `res = 0` to count discards

**2.2 Process Each Arrival:**

For each arrival at index `idx` with item type `item`:

**2.3 Remove Items That Left Window:**

```python
if idx >= w:
    left_item = arrivals[idx - w]
    if left_item != 0:  # Only decrement if it was kept
        ctr[left_item] -= 1
```

When `idx >= w`, the item at `idx - w` has left the window. We only decrement if it was kept (not marked as 0).

**2.4 Check If We Need to Discard:**

```python
if ctr[item] >= m:
    res += 1
    arrivals[idx] = 0  # Mark as discarded
else:
    ctr[item] += 1
```

If the current item type already appears `m` times in the window, we must discard it. Otherwise, we keep it and increment the counter.

**2.5 Return Result:**

After processing all arrivals, return the total number of discards.

**Time Complexity:** O(n) - Single pass through arrivals  
**Space Complexity:** O(max(arrivals)) - Counter array

