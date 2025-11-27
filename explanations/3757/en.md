# Problem 3757: Number of Effective Subsequences

**Difficulty:** Hard  
**LeetCode Link:** https://leetcode.com/problems/number-of-effective-subsequences/

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count subsequences that, when removed, cause at least one bit in the total OR to turn off. Think of each bit as a **light bulb** and each number as a **guardian** that powers certain bulbs.

**1.1 Constraints & Complexity:**

- **Input Size:** We have up to $10^5$ elements, and each element is at most $10^6$ (about 20 bits).
- **Time Complexity:** $O(B \cdot 2^B + n)$ where $B$ is the number of bits set in the total OR (at most 20). The SOS DP step takes $O(B \cdot 2^B)$ and inclusion-exclusion takes $O(2^B)$.
- **Space Complexity:** $O(2^B + n)$ for the frequency array, DP array, and power-of-2 array.
- **Edge Case:** If the total OR is 0 (all elements are 0), no subsequence can decrease it, so return 0.

**1.2 High-level approach:**

The goal is to count subsequences that remove all "guardians" of at least one bit. Each bit is like a light bulb that stays on as long as at least one number (guardian) powers it. A subsequence is effective if removing it causes at least one bulb to turn off.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all $2^n$ possible subsequences, calculate the OR of remaining elements for each, and count those where the OR is strictly less than the total OR. This is $O(2^n \cdot n)$ which is too slow for $n = 10^5$.
- **Optimized Strategy:** Use the "light bulb" analogy: identify which bits are on (total OR), find guardians for each bit, and use inclusion-exclusion to count subsequences that remove all guardians of at least one bit. This reduces the problem to working with at most 20 bits instead of $10^5$ elements.
- **Optimization:** By focusing on bits rather than individual elements, we reduce the exponential factor from $2^n$ to $2^B$ where $B \leq 20$, making the solution feasible.

**1.4 Decomposition:**

1. **Calculate Total OR:** Find all "light bulbs" (bits) that are currently on.
2. **Identify Guardians:** For each bit, find all numbers that contribute to it (have that bit set).
3. **Compress Representation:** Map each number to a bitmask showing which of the relevant bits it contributes to.
4. **SOS DP:** Count how many numbers contribute only to bits within each mask (for efficient counting).
5. **Inclusion-Exclusion:** Count subsequences that remove all guardians of at least one bit, avoiding double counting.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `nums = [2, 2, 1]`.

- Total OR = $2 | 2 | 1 = 3$ (binary `11`)
- Bits that are on: bit 0 and bit 1
- Guardians:
  - Bit 0: `[1]` (only the number 1 has bit 0 set)
  - Bit 1: `[2, 2]` (both 2s have bit 1 set)

**2.2 Start Processing:**

We compress the representation to work only with the relevant bits (0 and 1 in this case), creating a mapping from each number to a 2-bit mask.

**2.3 Trace Walkthrough:**

| Number | Binary | Contributes to Bits | Compressed Mask |
|--------|--------|---------------------|-----------------|
| 2      | 10     | Bit 1              | 10 (mask = 2)   |
| 2      | 10     | Bit 1              | 10 (mask = 2)   |
| 1      | 01     | Bit 0              | 01 (mask = 1)   |

After SOS DP:
- `dp[00] = 0` (numbers contribute to neither bit)
- `dp[01] = 1` (1 number contributes only to bit 0)
- `dp[10] = 2` (2 numbers contribute only to bit 1)
- `dp[11] = 3` (all numbers contribute to at least one bit)

**2.4 Inclusion-Exclusion Counting:**

We iterate over all non-empty subsets of bits to keep. For each subset `s`:
- `comp = full_mask ^ s` represents bits we're removing
- `count_zero = dp[comp]` counts numbers that contribute only to removed bits
- These numbers can be freely included or excluded: $2^{count\_zero}$ ways
- Apply inclusion-exclusion: the sign is determined by `popcount(s)` (number of bits kept), following the inclusion-exclusion formula structure

**2.5 Return Result:**

After processing all subsets, `res` contains the count of effective subsequences. For `[2, 2, 1]`, we get 5 effective subsequences:
- Removing all guardians of bit 0: `[1]`, `[2, 1]`, `[2, 1]`, `[2, 2, 1]` (4 ways)
- Removing all guardians of bit 1: `[2, 2]`, `[2, 2, 1]` (2 ways, but `[2, 2, 1]` counted twice)
- Using inclusion-exclusion: $4 + 2 - 1 = 5$

