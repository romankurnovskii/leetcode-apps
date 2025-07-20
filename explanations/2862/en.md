## 2862. Maximum Element-Sum of a Complete Subset of Indices (Hard)

https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices

## Description

You are given a **1-indexed** array `nums`. Your task is to select a **complete subset** from `nums` where every pair of selected indices multiplied is a perfect square, i.e., if you select `a_i` and `a_j`, `i * j` must be a perfect square.

Return the *sum* of the complete subset with the *maximum sum*.

**Examples**

**Example 1:**

    Input: nums = [8,7,3,5,7,2,4,9]
    Output: 16
    Explanation: We select elements at indices 2 and 8 and 2 * 8 is a perfect square.

**Example 2:**

    Input: nums = [8,10,3,8,1,13,7,9,4]
    Output: 20
    Explanation: We select elements at indices 1, 4, and 9. 1 * 4, 1 * 9, 4 * 9 are perfect squares.

**Constraints**

```
1 <= n == nums.length <= 10^4
1 <= nums[i] <= 10^9
```

## Top Community Explanations

### 1. [Java/C++/Python] Square Factorization, O(n) O(1) ([lee215](https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/solutions/4053876/javacpython-square-factorization-on-o1-b-2r31))

**Explanation:**
- For each index `i`, divide it by all possible square numbers until you get its "key" (the product of primes with odd exponents in its factorization).
- In a complete set, all indices have the same key.
- For all indices, group by key and sum the corresponding `nums[i]` values. The answer is the maximum group sum.

**Python:**
```python
from collections import Counter
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        count = Counter()
        for i in range(len(nums)):
            x, v = i + 1, 2
            while x >= v * v:
                while x % (v * v) == 0:
                    x //= v * v
                v += 1
            count[x] += nums[i]
        return max(count.values())
```

### 2. Simple square root calculation ([manmee](https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/solutions/4054028/simple-square-root-calculation-by-manmee-x697))

**Explanation:**
- For each possible starting index `i`, consider the sequence `{i, i*4, i*9, i*16, ...}` (i.e., `i * m^2` for `m = 1, 2, ...`).
- For each such sequence, sum the corresponding `nums` values and keep the maximum.

**Python:**
```python
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        squares = [k * k for k in range(1, 101)]
        ans = -1
        for i in range(n):
            curr = 0
            for sq in squares:
                idx = (i + 1) * sq - 1
                if idx >= n:
                    break
                curr += nums[idx]
            ans = max(ans, curr)
        return ans
```

### 3. i * m * m sequence ([votrubac](https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/solutions/4080073/i-m-m-sequence-by-votrubac-6lev))

**Explanation:**
- For any starting index `i`, the valid indices are `i * m^2` for `m = 1, 2, ...`.
- For each `i`, sum the values at these indices and keep the maximum.

**Python:**
```python
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(1, n + 1):
            cur = 0
            m = 1
            while i * m * m <= n:
                cur += nums[i * m * m - 1]
                m += 1
            res = max(res, cur)
        return res
```

## Explanation

### Strategy

Let's restate the problem:
- You have a 1-indexed array `nums`.
- You want to select a subset of indices such that for every pair `(i, j)` in the subset, `i * j` is a perfect square.
- What is the maximum possible sum of the elements at those indices?

**Type:** Array, Math, Number Theory

**What is given:**
- An array of positive integers (the values).

**What is asked:**
- The maximum sum of a complete subset (as defined above).

**Constraints/Edge Cases:**
- Array can be large (up to 10,000 elements).
- All values are positive integers.

**High-level plan:**
- For each index, compute its "key" (the product of primes with odd exponents in its factorization).
- Group indices by key, sum the corresponding values, and return the maximum sum.
- Alternatively, for each possible starting index, consider the sequence `i * m^2` and sum the values.

### Steps

Let's walk through an example: `nums = [8, 7, 3, 5, 7, 2, 4, 9]`

1. For each index, compute its key:
    - Index 1: key = 1
    - Index 2: key = 2
    - Index 3: key = 3
    - Index 4: key = 1 (since 4 = 2^2)
    - ...
2. Group indices by key and sum the corresponding values:
    - key 1: indices 1, 4, ...
    - key 2: indices 2, ...
    - ...
3. The answer is the maximum sum among all groups.

**Key insight:**
> Indices with the same key can be grouped together, and their products will always be perfect squares.

### Solution

```python
from collections import Counter

def maximumSum(nums):
    count = Counter()
    for i in range(len(nums)):
        x, v = i + 1, 2
        while x >= v * v:
            while x % (v * v) == 0:
                x //= v * v
            v += 1
        count[x] += nums[i]
    return max(count.values())
```

**Time Complexity:** O(n * sqrt(n)) (worst case, but much faster in practice)

**Space Complexity:** O(n) (for the Counter) 