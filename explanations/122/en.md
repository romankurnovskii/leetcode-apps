# 122. Best Time to Buy and Sell Stock II

## Description

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can buy it then immediately sell it on the **same day**.

Find and return *the **maximum** profit you can achieve*.

**Example 1:**
```tex
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
```

**Example 2:**
```tex
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
```

**Example 3:**
```tex
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
```

**Constraints:**
- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`

## Explanation

### Strategy

This is a **greedy algorithm problem** that allows multiple buy-sell transactions. The key insight is that we can capture all positive price differences by buying and selling whenever the price increases.

**Key observations:**
- We can buy and sell multiple times
- We can buy and sell on the same day
- The maximum profit comes from capturing all positive price differences
- We don't need to track buy/sell decisions, just sum up positive differences

**High-level approach:**
1. **Iterate through prices**: Compare each price with the previous one
2. **Capture positive differences**: If current price > previous price, add the difference to profit
3. **Ignore negative differences**: If price decreases, we don't lose money (we just don't buy)
4. **Return total profit**: Sum of all positive price differences

### Steps

Let's break down the solution step by step:

**Step 1: Initialize profit**
- Start with `profit = 0`

**Step 2: Iterate through the array**
For each price starting from the second:
- Calculate the difference: `current_price - previous_price`
- If the difference is positive, add it to profit
- If the difference is negative or zero, ignore it

**Step 3: Return the result**
- Return the total accumulated profit

**Example walkthrough:**
Let's trace through the first example:

```sh
prices = [7,1,5,3,6,4]

Initial state:
profit = 0

Step 1: Compare prices[1] with prices[0]
difference = 1 - 7 = -6 (negative, ignore)
profit = 0

Step 2: Compare prices[2] with prices[1]
difference = 5 - 1 = 4 (positive, add to profit)
profit = 0 + 4 = 4

Step 3: Compare prices[3] with prices[2]
difference = 3 - 5 = -2 (negative, ignore)
profit = 4

Step 4: Compare prices[4] with prices[3]
difference = 6 - 3 = 3 (positive, add to profit)
profit = 4 + 3 = 7

Step 5: Compare prices[5] with prices[4]
difference = 4 - 6 = -2 (negative, ignore)
profit = 7

Result: Return profit = 7
```

> **Note:** The greedy approach works because we can buy and sell on the same day. This means we can capture every positive price movement without any transaction costs. The optimal strategy is to buy whenever the price is about to go up and sell whenever it's about to go down.
