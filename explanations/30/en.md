## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The string $s$ has length up to $10^4$, and the array $words$ has up to 5000 words, each of length up to 30.
* **Time Complexity:** $O(n \times m \times k)$ where $n$ is the length of $s$, $m$ is the number of words, and $k$ is the length of each word. For each starting position, we check if a substring matches all words.
* **Space Complexity:** $O(m \times k)$ for storing word frequencies and the seen dictionary.
* **Edge Case:** If $words$ is empty, return empty list. All words have the same length, which simplifies the matching process.

**1.2 High-level approach**

The goal is to find all starting indices in $s$ where a concatenated substring (formed by all words in any order) begins. We check each possible starting position and verify if the substring matches all words.

![Sliding window with word matching showing how we check for concatenated substrings]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Generate all permutations of words, then search for each permutation in $s$. This is factorial in complexity.
* **Optimized (Fixed Window):** For each starting position, extract words of fixed length and check if they match the word list (accounting for frequency). This avoids generating permutations.

**1.4 Decomposition**

1. Count the frequency of each word in the `words` array.
2. For each possible starting position in $s$:
   - Extract consecutive words of fixed length.
   - Track which words we've seen and their frequencies.
   - If all words match with correct frequencies, add the starting index.
3. Return all valid starting indices.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $s = "barfoothefoobarman"$, $words = ["foo","bar"]$.

We initialize:
* `word_len = 3` (length of each word)
* `total_len = 6` (2 words × 3 characters)
* `word_count = {"foo": 1, "bar": 1}` (frequency map)
* `res = []` (result list)

**2.2 Start Checking/Processing**

We iterate through starting positions from 0 to `len(s) - total_len` (inclusive).

**2.3 Trace Walkthrough**

| i | Substring | Extracted Words | seen | Match? | Action |
|---|-----------|-----------------|------|--------|--------|
| 0 | "barfoothefoobarman"[0:6] | "barfoo" | {} | - | Start |
| 0 | - | "bar" (0-3) | {"bar": 1} | - | Continue |
| 0 | - | "foo" (3-6) | {"bar": 1, "foo": 1} | Yes | Add 0 |
| 1 | "arfoothefoobarman"[0:6] | "arfoot" | {} | - | "arfoot" not valid |
| 2 | "rfoothefoobarman"[0:6] | "rfoothe" | {} | - | "rfoothe" not valid |
| ... | ... | ... | ... | ... | ... |
| 9 | "foobarman"[0:6] | "foobar" | {} | - | Start |
| 9 | - | "foo" (9-12) | {"foo": 1} | - | Continue |
| 9 | - | "bar" (12-15) | {"foo": 1, "bar": 1} | Yes | Add 9 |

**2.4 Increment and Loop**

For each starting position $i$:
1. Initialize `seen = {}` to track words found in this substring.
2. For $j$ from 0 to `len(words) - 1`:
   - Extract word: `word = s[i + j * word_len : i + (j + 1) * word_len]`
   - If word not in `word_count`, break.
   - Increment `seen[word]`.
   - If `seen[word] > word_count[word]`, break (too many occurrences).
3. If we processed all words successfully, add $i$ to `res`.

**2.5 Return Result**

After checking all positions:
* Position 0: "barfoo" matches ["bar", "foo"] → Add 0
* Position 9: "foobar" matches ["foo", "bar"] → Add 9

Return `res = [0, 9]`.

