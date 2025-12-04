## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Word length is 1 to 25, and there are at most 10^4 calls to `addWord` and `search`. Search queries have at most 2 dots.
- **Time Complexity:** 
  - `addWord`: O(m) where m is the word length
  - `search`: O(m * 26^k) in worst case where k is the number of dots, but typically much better
- **Space Complexity:** O(N * M) where N is the number of words and M is the average word length.
- **Edge Case:** Searching for a word with no dots is O(m) time, same as a regular trie search.

**1.2 High-level approach:**
The goal is to design a data structure that supports adding words and searching with wildcard characters (dots). A trie (prefix tree) is perfect for this, with special handling for dots during search.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Store words in a list. For search with dots, check each word character by character. This is O(N * M) per search.
- **Optimized Strategy:** Use a trie to store words. For dots, recursively search all possible children. This is much more efficient for prefix matching.
- **Why optimized is better:** Trie allows early termination when prefixes don't match and efficiently handles wildcard searches.

**1.4 Decomposition:**
1. Build a trie data structure with nodes containing children and an `is_end` flag.
2. For `addWord`, traverse the trie, creating nodes as needed, and mark the end.
3. For `search`, use DFS to handle dots by recursively searching all children when encountering a dot.
4. Return true if we find a complete word matching the pattern.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Initialize: `root = TrieNode()`

Add words: "bad", "dad", "mad"

**2.2 Start Checking:**
Search for: ".ad"

**2.3 Trace Walkthrough:**

| Step | Current Node | Char | Action |
|------|---------------|------|--------|
| 0 | root | '.' | Check all children (b, d, m) |
| 1 | node['b'] | 'a' | Check if 'a' in children |
| 2 | node['b']['a'] | 'd' | Check if 'd' in children and is_end |
| 3 | - | - | Found "bad", return True |

For ".ad", we check all first-level children (b, d, m), then continue with 'a' and 'd'.

**2.4 Increment and Loop:**
For each character in the search word:
- If it's a dot, recursively search all children
- If it's a regular character, follow that child if it exists
- If we reach the end and `is_end` is true, return true

**2.5 Return Result:**
The search ".ad" matches "bad", "dad", or "mad", so return `True`.

