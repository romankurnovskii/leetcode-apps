## Explanation

### Strategy (The "Why")

**Restate the problem:** We have a circular array where each person can transfer 1 unit to left or right neighbor. Find minimum moves to make all balances non-negative. Return -1 if impossible.

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= n <= 10^5`, `-10^9 <= balance[i] <= 10^9`
- **Time Complexity:** O(n log n) - Sort positive indices by distance
- **Space Complexity:** O(n) - Store positive indices
- **Edge Case:** No negative balance (return 0), total sum < 0 (return -1)

**1.2 High-level approach:**

Find the negative balance index. Sort all positive indices by their circular distance from the negative index. Greedily transfer from closest positive neighbors until the negative is balanced.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible transfer sequences. This is exponential.
- **Optimized (Greedy):** Always transfer from the closest positive neighbor. This minimizes total moves. This is O(n log n) due to sorting.
- **Why it's better:** The greedy approach is optimal because transferring from closer neighbors minimizes the total distance traveled by units.

**1.4 Decomposition:**

1. Check if total sum < 0, return -1
2. Find negative balance index
3. If no negative, return 0
4. Sort positive indices by circular distance from negative
5. Greedily transfer from closest positives until negative is balanced
6. Return total moves

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `balance = [5,1,-4]`

- Total sum: `5 + 1 - 4 = 2 >= 0` ✓
- Negative index: `2` (value -4)

**2.2 Check Total Sum:**

```python
total = sum(balance)
if total < 0:
    return -1
```

**2.3 Find Negative Index:**

```python
for i in range(n):
    if balance[i] < 0:
        neg_idx = i
        break
```

**2.4 Sort Positive Indices by Distance:**

```python
positives = []
for i in range(n):
    if balance[i] > 0:
        dist1 = (i - neg_idx) % n
        dist2 = (neg_idx - i) % n
        dist = min(dist1, dist2)
        positives.append((dist, i, balance[i]))
positives.sort()
```

For `balance = [5,1,-4]`, `neg_idx = 2`:
- Index 0: dist = min(1, 2) = 1, amount = 5
- Index 1: dist = min(2, 1) = 1, amount = 1
- Sorted: `[(1, 0, 5), (1, 1, 1)]`

**2.5 Greedily Transfer:**

```python
needed = abs(balance[neg_idx])  # 4
for dist, idx, amount in positives:
    if needed <= 0:
        break
    transfer = min(needed, amount)
    res += transfer * dist
    needed -= transfer
```

- From index 0: transfer 4, moves = 4 * 1 = 4
- Needed = 0, done

**2.6 Return Result:**

```python
return res if needed <= 0 else -1  # 4
```

**Time Complexity:** O(n log n) - Sort positive indices  
**Space Complexity:** O(n) - Store positive indices

