## Explanation

### Strategy

**Constraints & Edge Cases**

* **String Length:** The tiles string has length 1-7, consisting of uppercase English letters. This small constraint allows for backtracking solutions.
* **Time Complexity:** We generate all possible sequences using backtracking. The number of sequences depends on the character frequencies. **Time Complexity: O(2^n)** where n is the number of unique sequences, **Space Complexity: O(n)** for recursion stack and character counts.
* **Edge Case:** If tiles has only one character, there's exactly one sequence (the character itself).

**High-level approach**

The problem asks us to count all possible non-empty sequences we can form from the given tiles. Each tile can be used at most as many times as it appears in the original string.

**Brute force vs. optimized strategy**

* **Brute Force:** Generate all possible sequences and count them. This is what we do, but we use backtracking to avoid duplicates efficiently.
* **Optimized:** Use backtracking with character frequency counting. For each character, we can either use it (if available) or skip it. Count each valid sequence as we build it.

**Decomposition**

1. **Count Characters:** Create a frequency map of all characters in tiles.
2. **Backtrack:** For each character, try using it (if available) and recursively count sequences.
3. **Count Sequences:** Each time we add a character, we have a new sequence, so increment the count.

### Steps

1. **Initialization & Example Setup**
   Let's use `tiles = "AAB"` as our example.
   - Count characters: `count = {'A': 2, 'B': 1}`.

2. **Backtrack Function**
   The `backtrack(count)` function:
   - Initialize `res = 0` to count sequences.
   - For each character in count:
     - If count[char] > 0, we can use it.
     - Increment `res` by 1 (this character alone is a sequence).
     - Decrement count[char], recursively call backtrack, then restore count[char].

3. **Trace Walkthrough**

Starting with `count = {'A': 2, 'B': 1}`:

| Step | Character | Count After | Sequences Found | Action |
|------|-----------|-------------|-----------------|--------|
| 1    | 'A'       | {'A':1,'B':1} | 1 ("A")      | Use A, recurse |
| 2    | 'A'       | {'A':0,'B':1} | 1 ("AA")     | Use A again, recurse |
| 3    | 'B'       | {'A':0,'B':0} | 1 ("AAB")    | Use B, recurse |
| 4    | 'B'       | {'A':1,'B':0} | 1 ("AB")     | Backtrack, use B instead |
| 5    | 'A'       | {'A':0,'B':0} | 1 ("ABA")    | Use A, recurse |
| 6    | 'B'       | {'A':2,'B':0} | 1 ("B")      | Backtrack, use B first |
| 7    | 'A'       | {'A':1,'B':0} | 1 ("BA")     | Use A, recurse |
| 8    | 'A'       | {'A':0,'B':0} | 1 ("BAA")    | Use A again |

Total: 8 sequences ("A", "AA", "AAB", "AB", "ABA", "B", "BA", "BAA")

4. **Return Result**
   Return the total count from backtrack function.
