## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the most common response across all days, but each response should only be counted once per day (duplicates within a day are removed). If there's a tie in frequency, return the lexicographically smallest response.

**1.1 Constraints & Complexity:**

- **Input Size:** Up to 1000 days, each with up to 1000 responses, each response string up to 10 characters.
- **Time Complexity:** O(n * m) where n is the number of days and m is the average number of responses per day. We iterate through each day, convert to set (O(m)), and count unique responses.
- **Space Complexity:** O(k) where k is the total number of unique responses across all days. We store counts in a dictionary.
- **Edge Case:** If all responses appear the same number of times, we return the lexicographically smallest one.

**1.2 High-level approach:**

The goal is to count how many days each unique response appears in (counting each response only once per day), then find the response with the highest count. If multiple responses have the same highest count, return the lexicographically smallest one.

![Response counting visualization](https://assets.leetcode.com/static_assets/others/response-counting.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each response, iterate through all days and count occurrences, then find the maximum. This would be O(n * m * k) where k is unique responses.
- **Optimized Strategy:** Use a dictionary to count frequencies, processing each day once and using a set to remove duplicates within each day. This is O(n * m) time.
- **Optimization:** By using a set to deduplicate within each day first, we ensure each response is counted at most once per day, and the dictionary allows O(1) counting updates.

**1.4 Decomposition:**

1. Initialize a dictionary to count response frequencies.
2. For each day's responses, convert to a set to remove duplicates.
3. For each unique response in that day, increment its count in the dictionary.
4. Find the maximum count value in the dictionary.
5. Among all responses with the maximum count, find the lexicographically smallest one.
6. Return that response.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]`

- Day 0: `["good","ok","good","ok"]` → unique: `{"good", "ok"}`
- Day 1: `["ok","bad","good","ok","ok"]` → unique: `{"ok", "bad", "good"}`
- Day 2: `["good"]` → unique: `{"good"}`
- Day 3: `["bad"]` → unique: `{"bad"}`
- Count dictionary: `count = {}`
- Result: `res = ""`

**2.2 Start Checking:**

We begin processing each day's responses, removing duplicates and counting unique responses.

**2.3 Trace Walkthrough:**

| Step | Day | Daily Responses | Unique Set | Action | count after |
| ---- | --- | --------------- | ---------- | ------ | ----------- |
| 1    | 0   | ["good","ok","good","ok"] | {"good", "ok"} | count["good"] = 1, count["ok"] = 1 | {"good": 1, "ok": 1} |
| 2    | 1   | ["ok","bad","good","ok","ok"] | {"ok", "bad", "good"} | count["ok"] = 2, count["bad"] = 1, count["good"] = 2 | {"good": 2, "ok": 2, "bad": 1} |
| 3    | 2   | ["good"] | {"good"} | count["good"] = 3 | {"good": 3, "ok": 2, "bad": 1} |
| 4    | 3   | ["bad"] | {"bad"} | count["bad"] = 2 | {"good": 3, "ok": 2, "bad": 2} |

After processing all days:
- `max_count = 3` (from "good")
- Responses with count 3: `["good"]`
- Lexicographically smallest: `"good"`

**2.4 Increment and Loop:**

We continue processing each day, converting to set and updating counts, until all days are processed.

**2.5 Return Result:**

The result is `"good"` because it appears in 3 days (the highest frequency), and among responses with the same frequency, it's the lexicographically smallest.

