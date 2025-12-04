## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** The input `n` is a positive integer from 1 to 2^31 - 1.
- **Time Complexity:** O(k) where k is the number of set bits (1s) in the binary representation. In worst case, this is O(32) = O(1) for 32-bit integers.
- **Space Complexity:** O(1) - We use only a constant amount of extra space.
- **Edge Case:** If `n = 0`, there are no set bits, so the result is 0.

**1.2 High-level approach:**
The goal is to count the number of set bits (1s) in the binary representation of a number. We use a clever bit manipulation trick to efficiently count bits.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Check each bit position individually using bitwise AND. This requires 32 iterations for a 32-bit number.
- **Optimized Strategy:** Use the trick `n & (n - 1)` which removes the rightmost set bit. We count how many times we can do this until `n` becomes 0. This only iterates for the number of set bits.
- **Why optimized is better:** We only iterate for the number of set bits, not all 32 positions. For numbers with few set bits, this is much faster.

**1.4 Decomposition:**
1. Initialize a counter to track the number of set bits.
2. While the number is not zero, repeatedly remove the rightmost set bit using `n & (n - 1)`.
3. Increment the counter each time we remove a bit.
4. Return the total count when the number becomes zero.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `n = 11` (binary: `1011`)

Initialize `res = 0`. We'll count set bits by removing them one by one.

**2.2 Start Checking:**
We repeatedly remove the rightmost set bit until `n` becomes 0.

**2.3 Trace Walkthrough:**

| Iteration | n (binary) | n & (n-1) | res | Action |
|-----------|------------|-----------|-----|--------|
| 0 | 1011 | 1010 | 0 | Remove rightmost bit, res = 1 |
| 1 | 1010 | 1000 | 1 | Remove rightmost bit, res = 2 |
| 2 | 1000 | 0000 | 2 | Remove rightmost bit, res = 3 |
| 3 | 0000 | - | 3 | n is 0, stop |

**2.4 Increment and Loop:**
Each iteration:
- `n = n & (n - 1)` removes the rightmost set bit
- `res += 1` increments our count

**2.5 Return Result:**
After all iterations, `res = 3`, which is the number of set bits in 11 (binary: 1011).

