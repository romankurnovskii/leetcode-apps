## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the maximum number of points we can earn by pairing compatible cards. Each card contains two lowercase letters, and we can only pair cards that both contain a given letter x and differ in exactly one position.

**1.1 Constraints & Complexity:**

- **Input Size:** Number of cards can be up to 10^5, each card has exactly 2 characters.
- **Time Complexity:** O(n + 26) where n is the number of cards - we iterate through cards once and then through at most 26 characters.
- **Space Complexity:** O(26) - we store counts for at most 26 different characters in first and second positions.
- **Edge Case:** If no cards contain the letter x, we cannot form any pairs.

**1.2 High-level approach:**

The goal is to categorize cards into three groups: cards with x in both positions, cards with x only in the first position, and cards with x only in the second position. Then we maximize pairs by optimally distributing "both" cards between the first and second groups.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible ways to pair cards, which would be exponential.
- **Optimized Strategy:** Categorize cards, count pairs within each category, then optimally distribute "both" cards to maximize additional pairs. This is O(n) time.
- **Optimization:** By categorizing cards upfront and using greedy pairing within categories, we can efficiently compute the maximum pairs.

**1.4 Decomposition:**

1. Categorize cards: count cards with x in both positions, first position only, and second position only.
2. Count pairs within first group (cards with same second character).
3. Count pairs within second group (cards with same first character).
4. Pair cards between first and second groups (e.g., "xa" with "ax").
5. Distribute "both" cards optimally between remaining first and second groups to maximize additional pairs.
6. Return the maximum total pairs.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `cards = ["aa","ab","ba","ac"], x = "a"`

- Cards containing 'a': "aa" (both), "ab" (first), "ba" (second), "ac" (first)
- Categories:
  - both = 1 ("aa")
  - first = {"b": 1, "c": 1} ("ab", "ac")
  - second = {"b": 1} ("ba")

**2.2 Start Processing:**

We count pairs within each category and between categories.

**2.3 Trace Walkthrough:**

| Step | Action | Pairs Found | Total |
|------|--------|-------------|-------|
| 1 | Pair within first group | None (different second chars) | 0 |
| 2 | Pair within second group | None (only one card) | 0 |
| 3 | Pair "ab" with "ba" | 1 pair (compatible) | 1 |
| 4 | Remaining: first={"c":1}, second={}, both=1 | - | - |
| 5 | Distribute "aa" to first: ("ac" + "aa") = 2 cards, 1 pair | 1 pair | 2 |
| 6 | Or distribute to second: ("ba" already paired) | - | - |

Maximum: 2 pairs

For `cards = ["aa","ab","ba"], x = "a"`:
- both = 1, first = {"b": 1}, second = {"b": 1}
- Pair "ab" with "ba": 1 pair
- Remaining: first={}, second={}, both=1
- No more pairs possible
- Result: 1

**2.4 Increment and Loop:**

The algorithm processes all cards once to categorize them, then computes pairs efficiently.

**2.5 Return Result:**

For `cards = ["aa","ab","ba","ac"], x = "a"`, the result is 2. We can form 2 pairs: ("ab", "ba") and ("ac", "aa").
