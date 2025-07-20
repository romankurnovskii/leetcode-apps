## 1798. Maximum Number of Consecutive Values You Can Make [Medium]

https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make

## Description

You are given an integer array `coins` of length `n` which represents the `n` coins that you own. The value of the `i`th coin is `coins[i]`. You can **make** some value `x` if you can choose some of your `n` coins such that their values sum up to `x`.

Return the *maximum number of consecutive integer values that you **can** **make** with your coins **starting** from and **including** 0*.

Note that you may have multiple coins of the same value.

**Examples**

**Example 1:**

    Input: coins = [1,3]
    Output: 2
    Explanation: You can make the following values:
    - 0: take []
    - 1: take [1]
    You can make 2 consecutive integer values starting from 0.

**Example 2:**

    Input: coins = [1,1,1,4]
    Output: 8
    Explanation: You can make the following values:
    - 0: take []
    - 1: take [1]
    - 2: take [1,1]
    - 3: take [1,1,1]
    - 4: take [4]
    - 5: take [4,1]
    - 6: take [4,1,1]
    - 7: take [4,1,1,1]
    You can make 8 consecutive integer values starting from 0.

**Example 3:**

    Input: coins = [1,4,10,3,1]
    Output: 20

**Constraints**

```
coins.length == n
1 <= n <= 4 * 10^4
1 <= coins[i] <= 4 * 10^4
```

## Explanation

### Strategy

Let's restate the problem:
- You have a set of coins, each with a positive integer value.
- You can use any subset of these coins (including none) to make sums.
- What is the largest number of *consecutive* values (starting from 0) you can make?

Consecutive is 0, 1, 2, ... So when you have coins `[1,2,3]`:

    - sum of them is 6
    - consecutive sequence will be up to `6` starting from `0`: `0, 1, 2, 3, 4, 5, 6` 

**Type:** Array, Greedy, Sorting

**What is given:**
- An array of positive integers (the coin values).

**What is asked:**
- The maximum number of consecutive values (starting from 0) you can make by summing up any subset of the coins.

**Constraints/Edge Cases:**
- Coins can have repeated values.
- The array can be large (up to 40,000 elements).
- All coin values are at least 1.

**High-level plan:**
- Sort the coins in ascending order.
- Track the smallest value you *cannot* make yet (let's call it `res`, start at 1).
- For each coin:
    - If the coin is greater than `res`, you can't make `res` (or anything larger), so stop.
    - Otherwise, you can now make all values up to `res + coin - 1`, so update `res += coin`.
- Return `res`.

### Steps

Let's walk through an example: `coins = [1, 1, 1, 4]`

1. **Sort the coins:** `[1, 1, 1, 4]`
2. **Initialize `res = 1`** (the smallest value we can't make yet)
3. **First coin (1):**
    - 1 <= (sequence value 1), so we can make 1. Now we can make all values up to 1 + 1 - 1 = 1.
    - Update `res = 2`.
4. **Second coin (1):**
    - 1 <= (sequence value 2), so we can make 2. Now we can make up to 2 + 1 - 1 = 2.
    - Update `res = 3`.
5. **Third coin (1):**
    - 1 <= (sequence value 3), so we can make 3. Now we can make up to 3 + 1 - 1 = 3.
    - Update `res = 4`.
6. **Fourth coin (4):**
    - 4 <= (sequence value 4), so we can make 4. Now we can make up to 4 + 4 - 1 = 7.
    - Update `res = 8`.
7. **No more coins.**

So, we can make all values from 0 to 7 (8 values).

**Another example:** `coins = [1, 3]`
- Sort: [1, 3]
- res = 1
- First coin: 1 <= 1 → res = 2
- Second coin: 3 > 2 → stop
- Answer: 2

**Key insight:**
> If you ever encounter a coin that is greater than the smallest value you can't make yet, you can't fill the gap, so you must stop.
