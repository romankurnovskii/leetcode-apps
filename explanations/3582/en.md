## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The string `caption` can have up to 150 characters.
* **Time Complexity:** O(n) where n is the length of the caption. We process each character once.
* **Space Complexity:** O(n) for building the result string.
* **Edge Case:** If the caption is empty, return "#". If the result exceeds 100 characters, truncate it.

**1.2 High-level approach:**

The goal is to transform a caption into a hashtag by: (1) converting to camelCase with '#' prefix, (2) removing non-letter characters, (3) truncating to 100 characters. We process the string step by step according to these rules.

![Visualization showing caption being transformed: split into words, convert to camelCase, filter letters, truncate]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Process the string in multiple passes: split words, convert to camelCase, filter non-letters, truncate. This is O(n) which is optimal.
* **Optimized:** Same as brute force - we need to process each character, so O(n) is the best we can do.
* **Why it's better:** The approach is straightforward and processes the string efficiently in a single logical flow.

**1.4 Decomposition:**

1. Split the caption into words.
2. Build camelCase string: first word lowercase, subsequent words with capitalized first letter.
3. Filter out all non-letter characters except the initial '#'.
4. Truncate to 100 characters if necessary.
5. Return the result.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `caption = "Leetcode daily streak achieved"`

We initialize:
* Split words: `words = ["Leetcode", "daily", "streak", "achieved"]`
* `res = "#"`

**2.2 Start Building:**

We process each word to build the camelCase string.

**2.3 Trace Walkthrough:**

| i   | word       | Action                               | res                            |
| --- | ---------- | ------------------------------------ | ------------------------------ |
| 0   | "Leetcode" | res += "leetcode" (lowercase)        | "#leetcode"                    |
| 1   | "daily"    | res += "Daily" (capitalize first)    | "#leetcodeDaily"               |
| 2   | "streak"   | res += "Streak" (capitalize first)   | "#leetcodeDailyStreak"         |
| 3   | "achieved" | res += "Achieved" (capitalize first) | "#leetcodeDailyStreakAchieved" |

After filtering non-letters (all are letters): `filtered = "#leetcodeDailyStreakAchieved"`
Length check: 30 <= 100, no truncation needed.

**2.4 Increment and Loop:**

We continue processing each word, building the camelCase string, then filter and truncate.

**2.5 Return Result:**

After processing all words, filtering, and checking length, we return `"#leetcodeDailyStreakAchieved"`.
