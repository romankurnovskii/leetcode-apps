## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a string containing HTML entities (like `&quot;`, `&apos;`, etc.), we need to replace them with their corresponding characters.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be up to 10^5 characters.
- **Time Complexity:** O(n * m) where n is the string length and m is the number of entities - we need to check and replace each entity, and string replacement is O(n) in worst case.
- **Space Complexity:** O(n) - we need to store the result string, which has the same or smaller length than the input.
- **Edge Case:** If the string contains `&amp;`, we need to replace it with `&`, but we must be careful about the order of replacements to avoid replacing parts of other entities.

**1.2 High-level approach:**

The goal is to use a dictionary mapping HTML entities to their character equivalents and replace all occurrences in the string. We need to replace `&amp;` last to avoid interfering with other entity replacements.

![HTML entity parsing visualization](https://assets.leetcode.com/static_assets/others/html-entity.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check each position in the string for each possible entity. This is O(n * m) which is acceptable for this problem.
- **Optimized Strategy:** Use Python's string replace method with a dictionary. We replace `&amp;` last to avoid conflicts. This is efficient and clear.
- **Optimization:** By replacing `&amp;` last, we ensure that other entities containing `&` are replaced correctly first.

**1.4 Decomposition:**

1. Create a dictionary mapping HTML entities to their character equivalents.
2. Iterate through the dictionary and replace each entity in the string.
3. Make sure to replace `&amp;` last to avoid replacing parts of other entities.
4. Return the parsed string.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `text = "&amp; is an HTML entity but &quot; is also one"`

- Entity dictionary: `{"&quot;": '"', "&apos;": "'", "&amp;": "&", "&gt;": ">", "&lt;": "<", "&frasl;": "/"}`
- Result string: `res = text`

**2.2 Start Checking:**

We begin replacing entities in the string.

**2.3 Trace Walkthrough:**

| Step | Entity | Replacement | res before | res after |
| ---- | ------ | ----------- | ---------- | --------- |
| 1    | &quot; | "           | "&amp; is..." | "&amp; is an HTML entity but \" is also one" |
| 2    | &apos; | '           | ...        | ... |
| 3    | &gt;   | >           | ...        | ... |
| 4    | &lt;   | <           | ...        | ... |
| 5    | &frasl;| /           | ...        | ... |
| 6    | &amp;  | &           | "&amp; is..." | "& is an HTML entity but \" is also one" |

**2.4 Increment and Loop:**

We iterate through each entity in the dictionary and perform the replacement.

**2.5 Return Result:**

The result is `"& is an HTML entity but \" is also one"`, with all HTML entities properly decoded.

