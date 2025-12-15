## Explanation

### Strategy

**Restate the problem**  
Recover a contaminated binary tree where original root was 0 and children follow `left = 2*x+1`, `right = 2*x+2`. Support queries to check if a target value exists.

**1.1 Constraints & Complexity**  
- **Input Size:** Up to `1e4` nodes, height <= 20.  
- **Time Complexity:** O(n) to recover; O(1) average for `find` via set lookup.  
- **Space Complexity:** O(n) to store recovered values.  
- **Edge Case:** Single-node tree.

**1.2 High-level approach**  
DFS from root, assign values by the given formulas, store all in a hash set for O(1) membership.  
![Tree recovery with value formulas](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Recover on every `find`, re-walking the tree — repeated O(n).  
- **Optimized:** Recover once, store in a set — O(n) build, O(1) queries.

**1.4 Decomposition**  
1. DFS from root with value parameter.  
2. Assign `val`, insert into set.  
3. Recurse to children with `2*val+1` and `2*val+2`.  
4. `find` checks membership in the set.

### Steps

**2.1 Initialization & Example Setup**  
Start at root with value 0, empty set.

**2.2 Start Processing**  
DFS visits each node, computing and storing values.

**2.3 Trace Walkthrough**  
| Node | Assigned val | Action        |
|------|--------------|---------------|
| root | 0            | add to set    |
| left | 1            | add to set    |
| right| 2            | add to set    |

**2.4 Increment and Loop**  
Continue recursively; each node’s children follow the formula.

**2.5 Return Result**  
`find(target)` returns `target in set`.

