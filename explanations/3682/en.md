## Explanation

### Strategy (The "Why")

**Restate the problem:** Given two lists of strings, we need to find the common strings with the minimum sum of their indices.

**1.1 Constraints & Complexity:**

- **Input Size:** Each list can have up to 10^3 elements.
- **Time Complexity:** O(n * m) where n and m are list lengths - we check all pairs.
- **Space Complexity:** O(min(n, m)) - we need to store results.
- **Edge Case:** If there are no common strings, return empty list. If multiple strings have the same index sum, return all of them.

**1.2 High-level approach:**

The goal is to find common strings and return those with the minimum index sum.

![Index sum visualization](https://assets.leetcode.com/static_assets/others/index-sum.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all pairs. This is O(n * m) which is acceptable.
- **Optimized Strategy:** Create a map from list1, then check list2 against it. This is O(n + m) time.
- **Optimization:** By using a hash map, we can check membership in O(1) instead of O(n).

**1.4 Decomposition:**

1. Create a map from words in list1 to their indices.
2. Initialize minimum sum to infinity and result list.
3. For each word in list2:
   - If word is in map, calculate index sum.
   - If sum < minimum, update minimum and reset result list.
   - If sum == minimum, add word to result list.
4. Return the result list.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `list1 = ["a", "b", "c"]`, `list2 = ["b", "a", "d"]`

- Map: `{"a": 0, "b": 1, "c": 2}`
- Minimum sum: `min_sum = float('inf')`
- Result list: `res = []`

**2.2 Start Checking:**

We check each word in list2.

**2.3 Trace Walkthrough:**

| Step | Word | In map? | Index sum | min_sum | res |
| ---- | ---- | ------- | --------- | ------- | --- |
| 1    | "b" | Yes | 1+0=1 | 1 | ["b"] |
| 2    | "a" | Yes | 0+1=1 | 1 | ["b","a"] |
| 3    | "d" | No | - | 1 | ["b","a"] |

**2.4 Increment and Loop:**

After checking each word, we update the minimum and result list.

**2.5 Return Result:**

The result is `["b", "a"]`, which are the common strings with minimum index sum of 1.

