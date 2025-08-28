## 89. Gray Code [Medium]

https://leetcode.com/problems/gray-code

## Description
An **n-bit gray code sequence** is a sequence of `2ⁿ` integers where:

- Every integer is in the **inclusive** range `[0, 2ⁿ - 1]`,
- The first integer is `0`,
- An integer appears **no more than once** in the sequence,
- The binary representation of every pair of **adjacent** integers differs by **exactly one bit**, and
- The binary representation of the **first** and **last** integers differs by **exactly one bit**.

Given an integer `n`, return *any valid **n-bit gray code sequence***.

**Examples**

```tex
Example 1:
Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit

Example 2:
Input: n = 1
Output: [0,1]
```

**Constraints**
```tex
- 1 <= n <= 16
```

## Explanation

### Strategy
Let's restate the problem: You need to generate a sequence of `2ⁿ` numbers from 0 to `2ⁿ - 1` where each adjacent pair differs by exactly one bit, and the first and last numbers also differ by exactly one bit.

This is a **bit manipulation problem** that involves understanding binary representations and finding patterns in how numbers can be arranged to satisfy the Gray code properties.

**What is given?** An integer `n` representing the number of bits.

**What is being asked?** Generate any valid n-bit Gray code sequence.

**Constraints:** `n` is between 1 and 16, so the sequences can be quite long.

**Edge cases:** 
- `n = 1`: Simple case with only two numbers
- `n = 2`: Small enough to visualize easily
- Large `n`: Requires efficient algorithm

**High-level approach:**
The solution involves understanding the mathematical properties of Gray codes and using a recursive or iterative approach to generate them.

**Decomposition:**
1. **Understand Gray code properties**: Each adjacent pair differs by exactly one bit
2. **Use reflection method**: Build larger Gray codes from smaller ones
3. **Generate sequence**: Create the complete sequence efficiently
4. **Return result**: Return the valid Gray code sequence

**Brute force vs. optimized strategy:**
- **Brute force**: Try all possible permutations and check Gray code properties. This is extremely inefficient.
- **Optimized**: Use the reflection method or mathematical properties to generate Gray codes directly.

### Steps
Let's walk through the solution step by step using the example `n = 2`:

**Step 1: Start with base case**
- For `n = 1`, the Gray code is `[0, 1]`
- Binary: `[0, 1]` or `[00, 01]`

**Step 2: Use reflection method**
- Take the existing sequence: `[0, 1]`
- Reflect it: `[1, 0]`
- Add prefix `0` to first half: `[00, 01]`
- Add prefix `1` to reflected half: `[11, 10]`
- Combine: `[00, 01, 11, 10]`

**Step 3: Convert to decimal**
- `00` = 0
- `01` = 1
- `11` = 3
- `10` = 2
- Result: `[0, 1, 3, 2]`

**Step 4: Verify properties**
- Adjacent pairs differ by exactly one bit:
  - `00` and `01`: differ in last bit
  - `01` and `11`: differ in first bit
  - `11` and `10`: differ in last bit
  - `10` and `00`: differ in first bit
- First and last differ by exactly one bit: `00` and `10` differ in first bit

**Why this works:**
The reflection method works because:
1. **Prefix property**: Adding `0` or `1` as a prefix preserves the one-bit difference property
2. **Reflection symmetry**: Reflecting the sequence and adding `1` as prefix creates the necessary transitions
3. **Mathematical induction**: If it works for `n-1`, it works for `n`

> **Note:** The key insight is that Gray codes can be built recursively by reflecting smaller Gray codes and adding appropriate prefixes. This is much more efficient than trying to find valid sequences through brute force.

**Time Complexity:** O(2ⁿ) - we generate exactly 2ⁿ numbers  
**Space Complexity:** O(2ⁿ) - we need to store the entire sequence
