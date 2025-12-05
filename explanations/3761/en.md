## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count valid paths in a tree where exactly one prime number appears on the path. A path (a,b) is valid if there is exactly one prime in the node labels along the path from a to b.

**1.1 Constraints & Complexity:**
- Input size: `1 <= n <= 10^5`
- **Time Complexity:** O(n) for sieve + O(n) for DFS = O(n)
- **Space Complexity:** O(n) for the tree and DP arrays
- **Edge Case:** If a path contains no primes or more than one prime, it's not valid

**1.2 High-level approach:**
We use tree DP where dp[node][0] counts paths with 0 primes and dp[node][1] counts paths with 1 prime, starting from that node going downward. We count valid paths by combining paths from different subtrees.

![Tree DP visualization](https://assets.leetcode.com/static_assets/others/tree-dp.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Check all O(n²) pairs of nodes and count primes on each path, which is O(n³).
- **Optimized Strategy:** Use tree DP to count paths in O(n) time. For each node, we combine paths from its children, counting how many paths pass through the current node.

**1.4 Decomposition:**
1. Use Sieve of Eratosthenes to identify prime numbers
2. Build the tree from edges
3. Perform DFS with DP: dp[node][0] = paths with 0 primes, dp[node][1] = paths with 1 prime
4. When processing a node, count valid paths by combining: (node has 1 prime, child has 0) or (node has 0, child has 1)
5. Update DP values based on whether current node is prime

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `n = 5`, `edges = [[1,2],[1,3],[2,4],[2,5]]`
- Primes: 2, 3, 5 (1 is not prime)
- Build tree: 1 connected to 2,3; 2 connected to 4,5
- Initialize dp arrays for all nodes

**2.2 Start DFS:**
We perform DFS starting from node 1 (root).

**2.3 Trace Walkthrough:**
Processing the tree with DFS:

| Node | Is Prime? | dp[node] Before | Children | Valid Paths Found | dp[node] After |
|------|-----------|-----------------|----------|-------------------|----------------|
| 4 | No | [1,0] | None | 0 | [1,0] |
| 5 | Yes | [0,1] | None | 0 | [0,1] |
| 2 | Yes | [0,1] | 4,5 | 1*1 + 0*0 = 1 | [1,1] |
| 3 | Yes | [0,1] | None | 0 | [0,1] |
| 1 | No | [1,0] | 2,3 | 0*1 + 1*1 + 1*0 + 0*1 = 2 | [3,2] |

Valid paths:
- (1,2): path contains prime 2 → valid
- (1,3): path contains prime 3 → valid  
- (1,4): path contains prime 2 → valid
- (2,4): path contains prime 2 → valid

Total: 4 valid paths

**2.4 Increment and Loop:**
During DFS, when we process a child, we count valid paths passing through the current node by combining dp values, then update the current node's dp values.

**2.5 Return Result:**
After DFS completes, `res = 4`, which is the number of valid paths with exactly one prime number.
