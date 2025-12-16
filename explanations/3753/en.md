## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the total waviness (count of peaks and valleys) for all numbers in the range `[num1, num2]`. A peak is a digit strictly greater than both neighbors; a valley is a digit strictly less than both neighbors.

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= num1 <= num2 <= 10^15` - Very large range
- **Time Complexity:** O(log num2 * 10^5) - Digit DP with memoization
- **Space Complexity:** O(log num2 * 10^5) - Memoization cache
- **Edge Case:** Numbers with < 3 digits have waviness 0

**1.2 High-level approach:**

We use digit dynamic programming (digit DP) to count waviness efficiently. Instead of iterating through all numbers (impossible for ranges up to 10^15), we build numbers digit by digit and track the last two digits to detect peaks/valleys. We compute waviness from 0 to num2 and subtract waviness from 0 to num1-1.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Iterate from num1 to num2, for each number check all middle digits for peaks/valleys. This is O((num2 - num1) * log num2) time, which is impossible for large ranges.
- **Optimized (Digit DP):** Build numbers digit by digit, tracking last two digits. When we have enough digits (p2, p1, current), we check for peak/valley. This is O(log num2 * states) time.
- **Why it's better:** We count waviness for all numbers in a range without explicitly constructing them, using DP states to avoid redundant calculations.

**1.4 Decomposition:**

1. Compute waviness from 0 to num1-1
2. Compute waviness from 0 to num2
3. Return difference (waviness in range [num1, num2])
4. For each range, use digit DP:
   - State: (position, last_digit, second_last_digit, tight, has_started)
   - Track total waviness and count of numbers formed
   - When we have 3+ digits, check for peaks/valleys

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `num1 = 120, num2 = 130`

- Compute `w1 = waviness(0 to 119)`
- Compute `w2 = waviness(0 to 130)`
- Return `w2 - w1`

**2.2 Digit DP Function:**

```python
def dfs(pos, p1, p2, tight, has_started):
    # pos: current digit position
    # p1: last digit
    # p2: second-to-last digit
    # tight: whether we're still matching the prefix of num
    # has_started: whether we've started building the number (non-zero digit)
```

**2.3 Base Case:**

```python
if pos == length:
    return 0, 1  # No more waviness, exactly 1 number formed
```

**2.4 Process Each Digit:**

For each possible digit `d` from 0 to `max_d`:
- Update `next_tight` and `next_started`
- Update last two digits: `nd1 = d`, `nd2 = p1`
- Recursively compute waviness for remaining digits

**2.5 Check for Peak/Valley:**

```python
if has_started and next_started and p1 is not None and p2 is not None:
    if (p2 < p1 > d) or (p2 > p1 < d):
        total_waviness += sub_count
```

When we have three consecutive digits (p2, p1, d), we check:
- Peak: `p2 < p1 > d` (middle digit is highest)
- Valley: `p2 > p1 < d` (middle digit is lowest)

If either condition is true, all numbers formed from this state will have this peak/valley, so we add `sub_count` to waviness.

**2.6 Return Result:**

After processing all digits, return the total waviness for the range.

**Time Complexity:** O(log num2 * states) - Digit DP with memoization  
**Space Complexity:** O(log num2 * states) - Memoization cache
