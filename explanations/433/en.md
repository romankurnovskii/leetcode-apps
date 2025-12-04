## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `0 <= bank.length <= 10`, gene strings are 8 characters.
- **Time Complexity:** O(bank.length * 8) - BFS through mutation space.
- **Space Complexity:** O(bank.length) - visited set and queue.
- **Edge Case:** startGene equals endGene returns 0, endGene not in bank returns -1.

**1.2 High-level approach:**
The goal is to find the minimum mutations from startGene to endGene. We use BFS to explore all valid mutations, where each mutation changes one character to A, C, G, or T.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all mutation sequences - exponential time.
- **Optimized Strategy:** BFS finds shortest path - polynomial time.

**1.4 Decomposition:**
1. Check if endGene is in bank.
2. Use BFS starting from startGene.
3. For each gene, try mutating each position to A, C, G, T.
4. If mutation is in bank and not visited, add to queue.
5. Return mutations count when endGene is reached.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `startGene = "AACCGGTT"`, `endGene = "AAACGGTA"`, `bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]`.
Initialize queue with (startGene, 0), visited = {startGene}.

**2.2 Start Checking:**
We perform BFS through valid mutations.

**2.3 Trace Walkthrough:**

| Level | Gene | Mutations | Next Valid |
|-------|------|-----------|------------|
| 0 | AACCGGTT | 0 | - |
| 1 | AACCGGTA | 1 | In bank |
| 1 | AACCGCTA | 1 | In bank |
| 2 | AAACGGTA | 2 | End gene! |

**2.4 Increment and Loop:**
After each level, we increment mutation count.

**2.5 Return Result:**
Return `res = 2`, the minimum mutations needed.

