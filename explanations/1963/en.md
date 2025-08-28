## 1963. Find XOR Sum of All Pairs Bitwise AND [Hard]

https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and

## Description
The **XOR sum** of a list is the bitwise `XOR` of all its elements. If the list only contains one element, then its **XOR sum** will be equal to this element.

- For example, the **XOR sum** of `[1,2,3,4]` is equal to `1 XOR 2 XOR 3 XOR 4 = 4`, and the **XOR sum** of `[3]` is equal to `3`.

You are given two **0-indexed** arrays `arr1` and `arr2` that consist only of non-negative integers.

Consider the list containing the result of `arr1[i] AND arr2[j]` (bitwise `AND`) for every `(i, j)` pair where `0 <= i < arr1.length` and `0 <= j < arr2.length`.

Return *the **XOR sum** of the aforementioned list*.

**Examples**

```tex
Example 1:
Input: arr1 = [1,2,3], arr2 = [6,5]
Output: 0
Explanation: The list = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5] = [0,1,2,0,2,1].
The XOR sum = 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0.

Example 2:
Input: arr1 = [12], arr2 = [4]
Output: 4
Explanation: The list = [12 AND 4] = [4]. The XOR sum = 4.
```

**Constraints**
```tex
- 1 <= arr1.length, arr2.length <= 10^5
- 0 <= arr1[i], arr2[j] <= 10^9
```

## Explanation

### Strategy
Let's restate the problem: You're given two arrays, and you need to compute the XOR sum of all possible bitwise AND results between pairs of elements from the two arrays. This involves understanding bitwise operations and finding an efficient way to compute the result without explicitly generating all pairs.

This is a **bit manipulation problem** that requires understanding the properties of XOR and AND operations to find an optimized solution.

**What is given?** Two arrays of non-negative integers, each potentially up to 100,000 elements long.

**What is being asked?** Find the XOR sum of all possible bitwise AND results between pairs from the two arrays.

**Constraints:** The arrays can be very large (up to 100,000 elements each), with values up to 10⁹.

**Edge cases:** 
- Single element arrays
- Arrays with all zeros
- Arrays with identical values

**High-level approach:**
The solution involves using mathematical properties of XOR and AND operations to avoid explicitly computing all pairs. We can use the distributive property and XOR properties to simplify the computation.

**Decomposition:**
1. **Understand the problem**: We need to compute XOR of all (arr1[i] AND arr2[j]) pairs
2. **Use mathematical properties**: Leverage XOR and AND properties to simplify
3. **Compute XOR sums**: Find XOR sum of each array separately
4. **Apply final operation**: Use the relationship between the XOR sums

**Brute force vs. optimized strategy:**
- **Brute force**: Generate all pairs, compute AND, then XOR. This takes O(n*m) time.
- **Optimized**: Use mathematical properties to compute in O(n+m) time.

### Steps
Let's walk through the solution step by step using the first example: `arr1 = [1,2,3]`, `arr2 = [6,5]`

**Step 1: Understand what we need to compute**
- We need: (1 AND 6) XOR (1 AND 5) XOR (2 AND 6) XOR (2 AND 5) XOR (3 AND 6) XOR (3 AND 5)
- This equals: 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0

**Step 2: Use the key mathematical property**
- For any element `a` in arr1: (a AND b₁) XOR (a AND b₂) XOR ... XOR (a AND bₘ) = a AND (b₁ XOR b₂ XOR ... XOR bₘ)
- This is because: (a AND b) XOR (a AND c) = a AND (b XOR c)

**Step 3: Apply the property to our problem**
- For arr1[0] = 1: (1 AND 6) XOR (1 AND 5) = 1 AND (6 XOR 5)
- For arr1[1] = 2: (2 AND 6) XOR (2 AND 5) = 2 AND (6 XOR 5)
- For arr1[2] = 3: (3 AND 6) XOR (3 AND 5) = 3 AND (6 XOR 5)

**Step 4: Compute intermediate values**
- `arr2_xor_sum = 6 XOR 5 = 3`
- `arr1_xor_sum = 1 XOR 2 XOR 3 = 0`

**Step 5: Apply the final relationship**
- Final result = (1 AND 3) XOR (2 AND 3) XOR (3 AND 3)
- = 1 XOR 2 XOR 3 = 0

**Why this works:**
The key insight is the distributive property of AND over XOR:
1. **Distributive property**: `(a AND b) XOR (a AND c) = a AND (b XOR c)`
2. **XOR properties**: XOR is associative and commutative
3. **Elimination**: We can eliminate the need to compute all pairs explicitly

> **Note:** The key insight is that we can compute the XOR sum of arr2 first, then for each element in arr1, compute its AND with the XOR sum, and finally XOR all these results together. This reduces the complexity from O(n*m) to O(n+m).

**Time Complexity:** O(n + m) - we only need to iterate through each array once  
**Space Complexity:** O(1) - we only need a few variables to store the XOR sums
