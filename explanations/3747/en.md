## Explanation

### Strategy (The "Why")

**Restate the problem:** For every integer from 1 to `n`, we remove all zeros from its decimal representation and count how many distinct integers we get.

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= n <= 10^15` - Very large, can't iterate through all numbers
- **Time Complexity:** O(log n) - Process digits of n
- **Space Complexity:** O(log n) - Store digit string and powers of 9
- **Edge Case:** `n = 1` returns 1

**1.2 High-level approach:**

The key insight is that after removing zeros, we only get numbers with digits 1-9 (zero-free numbers). So the problem reduces to counting how many zero-free numbers are <= n. We use digit DP (dynamic programming) to count these numbers efficiently.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Iterate from 1 to n, remove zeros from each, add to a set, return set size. This is O(n) time, which is impossible for n up to 10^15.
- **Optimized (Digit DP/Combinatorics):** Count zero-free numbers using digit-by-digit construction. For numbers with fewer digits than n, we have 9^d possibilities (9 choices per digit). For numbers with same length as n, we count digit by digit. This is O(log n) time.
- **Why it's better:** We don't need to iterate through all numbers; we can count them combinatorially by considering digit positions.

**1.4 Decomposition:**

1. Convert n to string to process digits
2. Precompute powers of 9 (9^1, 9^2, ..., 9^length)
3. Count zero-free numbers with fewer digits than n
4. Count zero-free numbers with same length as n, digit by digit
5. If n itself is zero-free, add 1

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 10`

- String representation: `"10"`, length = 2
- Precompute `pow9 = [1, 9, 81]` (9^0, 9^1, 9^2)

**2.2 Count Numbers with Fewer Digits:**

```python
for d in range(1, length):
    res += pow9[d]
```

For `n = 10`, we count:
- 1-digit numbers: 9 (1-9)
- Total so far: 9

**2.3 Count Numbers with Same Length:**

```python
for i, ch in enumerate(s):
    digit = int(ch)
    if digit == 0:
        return res  # Can't form any more zero-free numbers
    res += (digit - 1) * pow9[length - i - 1]
```

For `n = 10`:
- First digit: `1`
  - We can use digits 1-0 (but 0 is not allowed for zero-free)
  - Actually, we can use digits 1-0, but if we use 0, the number becomes invalid
  - Wait, let me reconsider: for first digit position, if digit is `1`, we can use `1` only (since we can't use 0)
  - Actually, the logic is: for digit `d`, we can use digits 1 to (d-1) freely, each giving `9^(remaining)` possibilities
  - For `n = 10`: first digit is `1`, so we can use `1` only (0 choices for digits < 1)
  - Second digit: if we used `1` for first, second digit is `0`, which means we can't form any zero-free numbers starting with `1` and second digit < `0`
  - So we return 9 (from step 2.2)

**2.4 Handle n Itself:**

If we process all digits without hitting 0, `n` itself is zero-free, so we add 1.

**2.5 Return Result:**

Return the total count of distinct zero-free numbers.

**Time Complexity:** O(log n) - Process each digit of n  
**Space Complexity:** O(log n) - Store digit string and powers
