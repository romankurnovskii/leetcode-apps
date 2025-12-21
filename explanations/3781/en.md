## Explanation

### Strategy (The "Why")

**Restate the problem:** We are given an integer array `nums` and a binary string `s` of the same length. Initially, score is 0. Each index where `s[i] = '1'` contributes `nums[i]` to the score. We can swap '0' and '1' if they are adjacent and '0' is before '1' (swap "01" to "10"). We can do this any number of times. We need to find the maximum possible score.

**1.1 Constraints & Complexity:**

- **Input Size:** Up to 10^5 elements in the array.
- **Time Complexity:** O(n log n) where n is the length - we use a max heap which takes O(log n) per operation.
- **Space Complexity:** O(n) for the heap storage.
- **Edge Case:** If all characters in `s` are '0', the score is 0 and no swaps are possible.

**1.2 High-level approach:**

The goal is to use a greedy approach with a max heap. As we process from left to right, we add all numbers to a heap. When we encounter a '1', we take the maximum value from the heap and add it to our score. This maximizes the score because we always use the largest available number when forced to select.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible sequences of swaps, calculate the score for each, and find the maximum. This would be exponential and too slow.
- **Optimized Strategy:** Use a max heap to track all numbers seen so far. When we must select (at a '1'), always choose the maximum. This is O(n log n) time.
- **Optimization:** The key insight is that we can effectively "move" '1's backward by swapping, so when we see a '1', we want to use the best number we've seen so far. The heap allows us to efficiently get the maximum.

**1.4 Decomposition:**

1. Initialize a max heap (using negative values for Python's min heap).
2. Process the array from left to right:
   - Add each number to the heap.
   - If the current character is '1', pop the maximum from the heap and add it to the score.
3. Return the total score.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [2, 1, 5, 2, 3]`, `s = "01010"`

- Heap: `[]` (empty)
- Score `res = 0`
- Process indices 0 to 4

**2.2 Start Processing:**

We begin processing from left to right, adding numbers to the heap.

**2.3 Trace Walkthrough:**

| Step | Index | nums[i] | s[i] | Heap (max first) | Action | res |
| ---- | ----- | ------- | ---- | ---------------- | ------ | --- |
| 1    | 0 | 2 | '0' | `[2]` | Add to heap | 0 |
| 2    | 1 | 1 | '1' | `[2, 1]` | Add to heap, then pop max (2) | 2 |
| 3    | 2 | 5 | '0' | `[5, 1]` | Add to heap | 2 |
| 4    | 3 | 2 | '1' | `[5, 2, 1]` | Add to heap, then pop max (5) | 7 |
| 5    | 4 | 3 | '0' | `[3, 2, 1]` | Add to heap | 7 |

Final score: 2 + 5 = 7

**2.4 Increment and Loop:**

After processing each index, we move to the next. We continue until all indices are processed.

**2.5 Return Result:**

The result is 7, which is the maximum score achievable by selecting the largest available numbers (2 and 5) when we encounter '1's in the string.

