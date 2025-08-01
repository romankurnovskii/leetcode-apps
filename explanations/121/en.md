# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy  
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

**Example 1:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

**Constraints:**
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Explanation

### Strategy

This is a **sliding window/dynamic programming problem** that requires finding the maximum profit from buying and selling a stock once. The key insight is to track the minimum price seen so far and calculate potential profit at each step.

**Key observations:**
- We can only buy once and sell once
- We must buy before we sell
- The maximum profit is the difference between the highest selling price and the lowest buying price
- We can track the minimum price as we iterate through the array

**High-level approach:**
1. **Track minimum price**: Keep track of the lowest price seen so far
2. **Calculate potential profit**: At each step, calculate profit if we sell at current price
3. **Update maximum profit**: Keep track of the highest profit found so far
4. **Return result**: Return the maximum profit (or 0 if no profit possible)

### Steps

Let's break down the solution step by step:

**Step 1: Initialize variables**
- `min_price`: Track the minimum price seen so far (starts with first price)
- `max_profit`: Track the maximum profit found so far (starts at 0)

**Step 2: Iterate through the array**
For each price starting from the second:
- Update `min_price` if current price is lower
- Calculate potential profit: `current_price - min_price`
- Update `max_profit` if current profit is higher

**Step 3: Return the result**
- Return `max_profit` (will be 0 if no profit possible)

**Example walkthrough:**
Let's trace through the first example:

```
prices = [7,1,5,3,6,4]

Initial state:
min_price = 7, max_profit = 0

Step 1: price = 1
1 < 7, so min_price = 1
potential_profit = 1 - 1 = 0
max_profit = max(0, 0) = 0

Step 2: price = 5
5 > 1, so min_price stays 1
potential_profit = 5 - 1 = 4
max_profit = max(0, 4) = 4

Step 3: price = 3
3 > 1, so min_price stays 1
potential_profit = 3 - 1 = 2
max_profit = max(4, 2) = 4

Step 4: price = 6
6 > 1, so min_price stays 1
potential_profit = 6 - 1 = 5
max_profit = max(4, 5) = 5

Step 5: price = 4
4 > 1, so min_price stays 1
potential_profit = 4 - 1 = 3
max_profit = max(5, 3) = 5

Result: Return max_profit = 5
```

> **Note:** The key insight is that we don't need to try every possible buy-sell combination. By tracking the minimum price seen so far, we can calculate the maximum possible profit at each step in O(1) time.

### Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Handle edge case
        if not prices:
            return 0
        
        # Initialize variables
        min_price = prices[0]
        max_profit = 0
        
        # Iterate through the array starting from the second element
        for price in prices[1:]:
            # Update minimum price if current price is lower
            min_price = min(min_price, price)
            
            # Calculate potential profit and update maximum profit
            potential_profit = price - min_price
            max_profit = max(max_profit, potential_profit)
        
        # Return the maximum profit
        return max_profit
```

**Time Complexity:** O(n) - we visit each element exactly once  
**Space Complexity:** O(1) - we only use a constant amount of extra space 