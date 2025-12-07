## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= m, n <= 50` where m is the number of customers and n is the number of banks.
- **Value Range:** `1 <= accounts[i][j] <= 100`.
- **Time Complexity:** O(m * n) - we iterate through each customer and sum their accounts.
- **Space Complexity:** O(1) - we only use a few variables.
- **Edge Case:** If there's only one customer, return the sum of their accounts.

**1.2 High-level approach:**

The goal is to find the maximum wealth among all customers, where each customer's wealth is the sum of money across all their bank accounts. We iterate through each customer, calculate their total wealth, and keep track of the maximum.

![Visualization showing customers with multiple bank accounts, with wealth calculated as the sum of all accounts, highlighting the richest customer]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Calculate wealth for each customer, store all wealths, then find the maximum. This uses O(m) extra space.
- **Optimized Strategy:** Calculate wealth for each customer and update the maximum on the fly. This uses O(1) extra space.
- **Why it's better:** The optimized approach doesn't need to store all wealth values, just the maximum, saving space while maintaining the same time complexity.

**1.4 Decomposition:**

1. Initialize `res = 0` to track the maximum wealth.
2. For each customer in accounts:
   - Calculate their total wealth by summing all their account balances.
   - Update `res` if this customer's wealth is greater than the current maximum.
3. Return the maximum wealth.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `accounts = [[1, 2, 3], [3, 2, 1]]`.

We initialize:
- `res = 0`

**2.2 Start Checking:**

Calculate wealth for each customer.

**2.3 Trace Walkthrough:**

| Step | Customer | Accounts | Wealth calculation | Wealth | Max so far (res) |
|------|----------|----------|---------------------|--------|------------------|
| 1 | 0 | [1, 2, 3] | 1 + 2 + 3 | 6 | 6 |
| 2 | 1 | [3, 2, 1] | 3 + 2 + 1 | 6 | 6 |

Both customers have wealth 6, so the maximum is 6.

Another example: `accounts = [[1, 5], [7, 3], [3, 5]]`

| Step | Customer | Accounts | Wealth calculation | Wealth | Max so far (res) |
|------|----------|----------|---------------------|--------|------------------|
| 1 | 0 | [1, 5] | 1 + 5 | 6 | 6 |
| 2 | 1 | [7, 3] | 7 + 3 | 10 | 10 |
| 3 | 2 | [3, 5] | 3 + 5 | 8 | 10 |

**2.4 Increment and Loop:**

Continue until all customers are processed.

**2.5 Return Result:**

Return `res = 10` - the maximum wealth among all customers (customer 1 with accounts [7, 3]).

