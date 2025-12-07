## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= key.length, value.length <= 100`, `1 <= timestamp <= 10^7`, at most `2 * 10^5` calls to set and get.
- **Time Complexity:** 
  - `set`: O(1) - append to list.
  - `get`: O(log m) where m is the number of timestamps for the key (binary search).
- **Space Complexity:** O(n) where n is the total number of set operations.
- **Edge Case:** If a key doesn't exist or no timestamp <= given timestamp exists, return empty string.

**1.2 High-level approach:**

The goal is to design a time-based key-value store that can store multiple values for the same key at different timestamps and retrieve the value associated with the largest timestamp that is <= the given timestamp. We use a dictionary to map keys to lists of (timestamp, value) pairs, and use binary search to efficiently find the correct value.

![Visualization showing how timestamps are stored and retrieved using binary search to find the largest timestamp <= target]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For `get`, iterate through all timestamps for a key to find the largest one <= target. This takes O(m) time where m is the number of timestamps.
- **Optimized Strategy:** Since timestamps are strictly increasing, we can use binary search to find the answer in O(log m) time.
- **Why it's better:** Binary search reduces the time complexity from O(m) to O(log m), which is crucial when there are many timestamps for a key.

**1.4 Decomposition:**

1. Initialize a dictionary to store key -> list of (timestamp, value) pairs.
2. For `set`: Append (timestamp, value) to the list for the key.
3. For `get`: Use binary search to find the largest timestamp <= target timestamp.
4. Return the corresponding value, or empty string if not found.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through the example operations:
- `set("foo", "bar", 1)`
- `get("foo", 1)` -> should return "bar"
- `get("foo", 3)` -> should return "bar" (largest timestamp <= 3 is 1)
- `set("foo", "bar2", 4)`
- `get("foo", 4)` -> should return "bar2"
- `get("foo", 5)` -> should return "bar2" (largest timestamp <= 5 is 4)

**2.2 Start Checking:**

Initialize: `store = {}`

**2.3 Trace Walkthrough:**

| Operation | Key | Timestamp/Value | Store state | Action |
|-----------|-----|-----------------|-------------|--------|
| set | "foo" | ("bar", 1) | {"foo": [(1, "bar")]} | Append to list |
| get | "foo" | 1 | - | Binary search: find timestamp <= 1 |
| - | - | - | - | Found (1, "bar"), return "bar" |
| get | "foo" | 3 | - | Binary search: find timestamp <= 3 |
| - | - | - | - | Found (1, "bar"), return "bar" |
| set | "foo" | ("bar2", 4) | {"foo": [(1, "bar"), (4, "bar2")]} | Append to list |
| get | "foo" | 4 | - | Binary search: find timestamp <= 4 |
| - | - | - | - | Found (4, "bar2"), return "bar2" |
| get | "foo" | 5 | - | Binary search: find timestamp <= 5 |
| - | - | - | - | Found (4, "bar2"), return "bar2" |

Binary search details for `get("foo", 3)`:
- List: `[(1, "bar"), (4, "bar2")]`
- left = 0, right = 1
- mid = 0, values[0][0] = 1 <= 3, so res = "bar", left = 1
- left = 1, right = 1, mid = 1, values[1][0] = 4 > 3, so right = 0
- left = 1 > right = 0, exit loop
- Return "bar"

**2.4 Increment and Loop:**

Binary search continues until left > right.

**2.5 Return Result:**

Return the value associated with the largest timestamp <= target, or "" if not found.

