## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Board size is up to 12x12, word length is 1 to 10, and there are up to 3*10^4 words.
- **Time Complexity:** O(M * N * 4^L) where M and N are board dimensions and L is the maximum word length. With trie optimization, we can prune early.
- **Space Complexity:** O(AL) where A is the alphabet size and L is the total length of all words for the trie, plus O(L) for recursion stack.
- **Edge Case:** If no words can be formed, return an empty list.

**1.2 High-level approach:**
The goal is to find all words from a list that can be formed on the board by moving to adjacent cells. We use a trie to store words and backtracking to explore the board.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each word, use DFS to search the board. This is O(W * M * N * 4^L) where W is the number of words.
- **Optimized Strategy:** Build a trie from all words, then use backtracking with the trie to search all words simultaneously. Prune branches when the current path doesn't match any word prefix.
- **Why optimized is better:** The trie allows us to search all words in parallel and prune early when no words match the current path.

**1.4 Decomposition:**
1. Build a trie from all words, storing the complete word at the end node.
2. For each cell on the board, start DFS if the cell's character matches a trie root child.
3. During DFS, mark the cell as visited, check if we found a word, explore neighbors, and restore the cell.
4. Prune the trie by removing nodes with no children after processing.
5. Collect all found words and return them.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Board: `[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]`
Words: `["oath","pea","eat","rain"]`

Build trie with all words.

**2.2 Start Checking:**
Start DFS from each cell that matches a trie root child.

**2.3 Trace Walkthrough:**

Starting from (0,0) with 'o':
- 'o' matches trie root child
- Mark (0,0) as '#'
- Explore neighbors: (0,1)='a', (1,0)='e'
- From (0,1): 'a' matches, continue to 't', then 'h'
- Found "oath", add to result
- Continue exploring...

**2.4 Increment and Loop:**
For each cell (i, j):
- If board[i][j] matches a trie child, start DFS
- During DFS: mark visited, check for word, explore neighbors, restore cell
- Prune trie nodes with no children

**2.5 Return Result:**
After processing all cells, `res = ["eat","oath"]`. Return this list.

