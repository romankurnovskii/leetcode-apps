## Explanation

### Strategy (The "Why")

**Restate the problem:** We start with numBottles full bottles. We can drink bottles (turning them into empty bottles) and exchange empty bottles for full ones. Each exchange requires numExchange empty bottles and increases the exchange rate by 1. We want to maximize the total bottles drunk.

**1.1 Constraints & Complexity:**
- Input size: `1 <= numBottles <= 100`, `1 <= numExchange <= 100`
- **Time Complexity:** O(numBottles) in the worst case, as we exchange until we can't
- **Space Complexity:** O(1) as we only track a few variables
- **Edge Case:** If numExchange > numBottles initially, we can only drink the initial bottles

**1.2 High-level approach:**
We drink all initial bottles, then repeatedly exchange empty bottles for full ones while the exchange rate allows. Each exchange gives us one more bottle to drink and increases the exchange rate.

![Water bottles exchange visualization](https://assets.leetcode.com/static_assets/others/greedy-algorithm.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Simulate each operation step by step, which is what we do - this is already optimal
- **Optimized Strategy:** Greedily exchange whenever possible, maximizing drinks at each step
- **Emphasize the optimization:** The greedy approach ensures we always maximize drinks by exchanging as soon as we have enough empty bottles

**1.4 Decomposition:**
1. Drink all initial bottles and count them
2. While we have enough empty bottles for an exchange, exchange them for one full bottle
3. Drink the newly obtained full bottle
4. Increase the exchange rate by 1 for the next exchange
5. Repeat until we can't exchange anymore

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `numBottles = 13`, `numExchange = 6`
- Initial state: `res = 0`, `empty = 0`, `exchange = 6`
- Drink all 13 bottles: `res = 13`, `empty = 13`

**2.2 Start Exchanging:**
We check if we can exchange empty bottles for a full one.

**2.3 Trace Walkthrough:**

| Step | Empty | Exchange Rate | Can Exchange? | Action | Empty After | res |
|------|-------|---------------|---------------|--------|-------------|-----|
| Initial | 13 | 6 | Yes | Exchange 6 for 1, drink it | 8 | 14 |
| 1 | 8 | 7 | Yes | Exchange 7 for 1, drink it | 2 | 15 |
| 2 | 2 | 8 | No | Stop | 2 | 15 |

**2.4 Increment and Loop:**
After each exchange, we increment the exchange rate and continue until we can't exchange.

**2.5 Return Result:**
The result is 15, which is the maximum number of bottles we can drink.
