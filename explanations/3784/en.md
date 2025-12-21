## Explanation

### Strategy (The "Why")

**Restate the problem:** We are given a string `s` and an integer array `cost` of the same length, where `cost[i]` is the cost to delete the i-th character. We can delete any number of characters such that the resulting string is non-empty and consists of equal characters. We need to find the minimum total deletion cost.

**1.1 Constraints & Complexity:**

- **Input Size:** Up to 10^5 characters in the string.
- **Time Complexity:** O(n) where n is the length of the string - we iterate through the string once to sum costs for each character.
- **Space Complexity:** O(1) if we use a dictionary with at most 26 keys (for lowercase letters), effectively O(1).
- **Edge Case:** If all characters are already equal, we don't need to delete anything, so the cost is 0.

**1.2 High-level approach:**

The goal is to find which character has the maximum total deletion cost (meaning it's most expensive to delete), then keep that character and delete all others. This minimizes the total cost because we avoid deleting the most expensive character.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try keeping each possible character, calculate the cost of deleting all others, and find the minimum. This is O(n) for each character, so O(26n) = O(n) which is already efficient.
- **Optimized Strategy:** Sum costs for each character, find the character with maximum total cost, then return total cost minus that maximum. This is O(n) time.
- **Optimization:** By finding the character with maximum deletion cost and keeping it, we minimize the total cost we need to pay. The answer is simply total cost minus the maximum character cost.

**1.4 Decomposition:**

1. Sum up the deletion costs for each character in the string.
2. Find the character with the maximum total deletion cost.
3. Keep that character and delete all others.
4. Return the total cost minus the maximum character cost (this is the cost of deleting all other characters).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "aabaac"`, `cost = [1, 2, 3, 4, 1, 10]`

- Character cost mapping:
  - 'a': 1 + 2 + 4 + 1 = 8
  - 'b': 3
  - 'c': 10
- Total cost: 1 + 2 + 3 + 4 + 1 + 10 = 21

**2.2 Start Processing:**

We iterate through the string and sum costs for each character.

**2.3 Trace Walkthrough:**

| Step | Character | Cost | Running Total for Character | Total Cost |
| ---- | --------- | ---- | --------------------------- | ---------- |
| 1    | 'a' | 1 | a: 1 | 1 |
| 2    | 'a' | 2 | a: 3 | 3 |
| 3    | 'b' | 3 | b: 3 | 6 |
| 4    | 'a' | 4 | a: 7 | 10 |
| 5    | 'a' | 1 | a: 8 | 11 |
| 6    | 'c' | 10 | c: 10 | 21 |

After processing:
- 'a' total cost: 8
- 'b' total cost: 3
- 'c' total cost: 10 (maximum)
- Keep 'c', delete others: 21 - 10 = 11

**2.4 Increment and Loop:**

We continue processing each character until we've processed the entire string.

**2.5 Return Result:**

The result is 11, which is the minimum cost to delete all characters except 'c' (the character with maximum deletion cost).

