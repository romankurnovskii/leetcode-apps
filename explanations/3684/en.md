# Problem 3684: Maximize Sum of At Most K Distinct Elements

**Difficulty:** Easy  
**LeetCode Link:** https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

## Problem Description

You are given a **positive** integer array `nums` and an integer `k`.

Choose at most `k` elements from `nums` so that their sum is maximized. However, the chosen numbers must be **distinct**.

Return an array containing the chosen numbers in **strictly descending** order.

**Example 1:**
- **Input:** `nums = [84,93,100,77,90]`, `k = 3`
- **Output:** `[100,93,90]`
- **Explanation:** The maximum sum is 283, which is attained by choosing 93, 100 and 90. We rearrange them in strictly descending order as `[100, 93, 90]`.

**Example 2:**
- **Input:** `nums = [84,93,100,77,93]`, `k = 3`
- **Output:** `[100,93,84]`
- **Explanation:** The maximum sum is 277, which is attained by choosing 84, 93 and 100. We rearrange them in strictly descending order as `[100, 93, 84]`. We cannot choose 93, 100 and 93 because the chosen numbers must be distinct.

**Example 3:**
- **Input:** `nums = [1,1,1,2,2,2]`, `k = 6`
- **Output:** `[2,1]`
- **Explanation:** The maximum sum is 3, which is attained by choosing 1 and 2. We rearrange them in strictly descending order as `[2, 1]`.

**Constraints:**
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= nums.length`

## Explanation

### Strategy (The "Why")

We need to select at most `k` **distinct** elements from the array to maximize their sum. Since we want the maximum sum, we should choose the largest available numbers. The constraint that elements must be distinct means we can only use each unique value once, even if it appears multiple times in the array.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 100 elements, and each element can be as large as $10^9$.
- **Time Complexity:** Converting to a set takes $O(n)$ where $n$ is the array length. Sorting the distinct elements takes $O(d \log d)$ where $d$ is the number of distinct elements (at most $n$). Taking the first $k$ elements is $O(k)$. Since $d \leq n$ and $k \leq n$, the **Final Time Complexity** is $O(n \log n)$.
- **Space Complexity:** The set stores at most $n$ distinct elements, and the sorted list also stores at most $n$ elements. The **Final Space Complexity** is $O(n)$.
- **Edge Case:** If the array has fewer than $k$ distinct elements, we return all distinct elements in descending order.

**1.2 High-level approach:**

The goal is to maximize the sum by selecting the largest distinct values. Since we want the maximum sum, we should greedily choose the largest available distinct numbers.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Generate all possible combinations of at most $k$ distinct elements, calculate each sum, and find the maximum. This would require checking $\binom{d}{1} + \binom{d}{2} + ... + \binom{d}{k}$ combinations, which is exponential and inefficient.
- **Optimized Strategy (Greedy):** Since we want to maximize the sum, we should choose the largest distinct elements. We can achieve this by: (1) getting all distinct elements, (2) sorting them in descending order, and (3) taking the top $k$ elements. This is $O(n \log n)$ and much more efficient.
- **Emphasize the optimization:** The greedy approach works because selecting larger numbers always yields a larger sum. By sorting and taking the top $k$, we guarantee the maximum possible sum without checking all combinations.

**1.4 Decomposition:**

1. Extract all distinct elements from the array to ensure uniqueness.
2. Sort the distinct elements in descending order to prioritize larger values.
3. Select the first $k$ elements from the sorted list (or all elements if there are fewer than $k$ distinct values).
4. Return the selected elements, which are already in descending order.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [84, 93, 100, 77, 90]$, $k = 3$.

First, we convert the array to a set to get distinct elements:
$$\text{Set} = \{84, 93, 100, 77, 90\}$$

**2.2 Start Processing:**

We convert the set back to a list and prepare to sort it in descending order.

**2.3 Trace Walkthrough:**

After converting to a list and sorting in descending order, we get:
$$\text{Distinct (sorted)} = [100, 93, 90, 84, 77]$$

Now we select the top $k = 3$ elements:

| Step | Element | Action | Selected So Far |
|------|---------|--------|-----------------|
| 1 | 100 | Take (largest) | [100] |
| 2 | 93 | Take (2nd largest) | [100, 93] |
| 3 | 90 | Take (3rd largest) | [100, 93, 90] |
| 4 | 84 | Skip (already have k elements) | [100, 93, 90] |
| 5 | 77 | Skip | [100, 93, 90] |

**2.4 Selection Process:**

We take the first $k$ elements from the sorted descending list using slicing: `distinct[:k]`.

**2.5 Return Result:**

The final result is $[100, 93, 90]$, which gives the maximum sum of $100 + 93 + 90 = 283$.

> **Note:** If there are duplicate values in the original array (like in Example 2), the set automatically removes duplicates, ensuring we only consider each unique value once.

