## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array of strings, we need to find all strings that are substrings of at least one other string in the array.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 100 strings, each with length up to 100.
- **Time Complexity:** O(n² * m) where n is the number of strings and m is the average string length - we compare each string with every other string.
- **Space Complexity:** O(n) - we need to store the result list, which can contain up to n strings.
- **Edge Case:** If a string appears multiple times, it should only appear once in the result. If no string is a substring of another, return an empty list.

**1.2 High-level approach:**

The goal is to check each string against all other strings to see if it's a substring. We can optimize by using a set to avoid duplicate checks and results.

![String matching visualization](https://assets.leetcode.com/static_assets/others/string-matching.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check each string against all others using substring search. This is what we do, and it's reasonable for the given constraints.
- **Optimized Strategy:** The brute force approach is already efficient enough for the problem constraints. We can use a set to store results to avoid duplicates.
- **Optimization:** By using a set for the words and checking membership, we can avoid redundant substring checks.

**1.4 Decomposition:**

1. Create a set of all words for efficient lookup.
2. For each word in the array:
   - Check if it's a substring of any other word in the set.
   - If yes, add it to the result.
3. Return the result list.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `words = ["mass", "as", "hero", "superhero"]`

- Words set: `{"mass", "as", "hero", "superhero"}`
- Result list: `res = []`

**2.2 Start Checking:**

We iterate through each word and check if it's a substring of any other word.

**2.3 Trace Walkthrough:**

| Step | Word | Check against | Is substring? | Action | res |
| ---- | ---- | ------------- | ------------- | ------ | --- |
| 1    | "mass" | "as", "hero", "superhero" | No | Skip | [] |
| 2    | "as" | "mass", "hero", "superhero" | Yes (in "mass") | Add | ["as"] |
| 3    | "hero" | "mass", "as", "superhero" | Yes (in "superhero") | Add | ["as", "hero"] |
| 4    | "superhero" | "mass", "as", "hero" | No | Skip | ["as", "hero"] |

**2.4 Increment and Loop:**

After checking each word, we move to the next word in the array.

**2.5 Return Result:**

The result is `["as", "hero"]`, which are the strings that appear as substrings of other words in the array.

