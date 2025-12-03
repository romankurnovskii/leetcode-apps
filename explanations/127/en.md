## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** `beginWord` and `endWord` have length $1 \leq L \leq 10$, and `wordList` has $1 \leq n \leq 5000$ words.
* **Time Complexity:** $O(L \times n)$ - In the worst case, we visit each word once, and for each word we try $L \times 26$ transformations.
* **Space Complexity:** $O(n)$ - The queue and visited set can contain at most $n$ words.
* **Edge Case:** If `endWord` is not in `wordList`, return 0 immediately.

**1.2 High-level approach**

The goal is to find the shortest transformation sequence from `beginWord` to `endWord` where each word differs by exactly one character. We use BFS to find the shortest path, trying all possible one-character transformations at each step.

![Word ladder BFS visualization showing how words transform level by level]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Try all possible sequences of transformations. This is exponential in complexity.
* **Optimized (BFS):** Use BFS to explore transformations level by level. The first time we reach `endWord`, we have the shortest path. This achieves $O(L \times n)$ time.

**1.4 Decomposition**

1. **Check Validity:** Verify `endWord` is in `wordList`.
2. **BFS Traversal:** Use a queue to process words level by level.
3. **Generate Transformations:** For each word, try changing each character to all 26 letters.
4. **Check and Enqueue:** If transformation is in `wordList` and not visited, add to queue.
5. **Return Length:** When `endWord` is found, return the sequence length.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $beginWord = "hit"$, $endWord = "cog"$, $wordList = ["hot","dot","dog","lot","log","cog"]$.

We initialize:
* `word_set = {"hot","dot","dog","lot","log","cog"}`
* `queue = deque([("hit", 1)])` (word and its level)
* `visited = {"hit"}`

**2.2 Start Processing**

We process level 1 (beginWord).

**2.3 Trace Walkthrough**

| Level | Queue | Word | Transformations | Valid Words | Queue (after) | visited |
|-------|-------|------|----------------|-------------|--------------|---------|
| 1 | [("hit",1)] | "hit" | "ait","bit",...,"hot",... | "hot" | [("hot",2)] | {"hit","hot"} |
| 2 | [("hot",2)] | "hot" | "aot","bot",...,"dot","lot" | "dot","lot" | [("dot",3),("lot",3)] | {"hit","hot","dot","lot"} |
| 3 | [("dot",3),("lot",3)] | "dot" | "aot","bot",...,"dog" | "dog" | [("lot",3),("dog",4)] | {"hit","hot","dot","lot","dog"} |
| 3 | [("lot",3),("dog",4)] | "lot" | "aot","bot",...,"log" | "log" | [("dog",4),("log",4)] | {"hit","hot","dot","lot","dog","log"} |
| 4 | [("dog",4),("log",4)] | "dog" | "aog","bog",...,"cog" | "cog" | **Found!** | - |

**2.4 BFS Processing**

For each word in queue:
1. If word equals `endWord`, return its level
2. For each position $i$ in the word:
   - For each letter $c$ in 'a'-'z':
     - Create `new_word` by replacing character at $i$ with $c$
     - If `new_word` in `word_set` and not visited:
       - Add to `visited`
       - Enqueue `(new_word, level + 1)`

**2.5 Return Result**

When "cog" is found at level 5, we return 5. The transformation sequence is: "hit" → "hot" → "dot" → "dog" → "cog" (5 words).

