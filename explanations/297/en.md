# Problem 297: Serialize and Deserialize Binary Tree
**Difficulty:** Hard  
**Link:** https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

## Explanation

### Strategy (The "Why")

The problem asks us to design an algorithm to serialize a binary tree to a string and deserialize it back to the original tree structure.

**1.1 Constraints & Complexity:**

- **Input Constraints:** $0 \leq n \leq 10^4$ nodes with values in $[-1000, 1000]$.
- **Time Complexity:** $O(n)$ - We visit each node once during both serialization and deserialization.
- **Space Complexity:** $O(n)$ - The serialized string and queue both require $O(n)$ space.
- **Edge Case:** Empty tree serializes to empty string and deserializes to `None`.

**1.2 High-level approach:**

The goal is to convert a tree to a string representation and reconstruct it. We use level-order (BFS) traversal to serialize, then use the same order to deserialize.

![Serialize Deserialize](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Use preorder/inorder or postorder/inorder pairs. This requires two traversals and more complex deserialization.
- **Optimized (Level-Order BFS):** Use BFS to serialize level by level, including null nodes. Deserialize by processing nodes in the same order. This is straightforward and intuitive.
- **Emphasize the optimization:** Level-order serialization is easier to understand and implement, making it a practical choice despite similar complexity.

**1.4 Decomposition:**

1. **Serialize:** Use BFS to traverse tree level by level, adding node values (or "null") to result string.
2. **Deserialize:** Split string, use BFS to reconstruct tree level by level, creating nodes as we process the values.
3. **Handle Nulls:** Include null nodes in serialization to preserve tree structure.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `root = [1,2,3,null,null,4,5]`.

**2.2 Serialization:**

Start with queue containing root.

**2.3 Trace Walkthrough (Serialize):**

| Step | Queue | Process | Result So Far |
|------|-------|---------|---------------|
| 0 | [1] | 1 | "1" |
| 1 | [2, 3] | 2 | "1,2" |
| 2 | [3, null, null] | 3 | "1,2,3" |
| 3 | [null, null, 4, 5] | null | "1,2,3,null" |
| ... | ... | ... | "1,2,3,null,null,4,5" |

**2.4 Deserialization:**

Split string: `["1","2","3","null","null","4","5"]`

| Step | Queue | Value | Action | Tree State |
|------|-------|-------|--------|------------|
| 0 | [1] | "1" | Create root(1) | 1 |
| 1 | [2, 3] | "2" | Create left(2) | 1→2 |
| 2 | [3] | "3" | Create right(3) | 1→2,3 |
| 3 | [4, 5] | "null" | Skip | 1→2,3 |
| 4 | [5] | "null" | Skip | 1→2,3 |
| 5 | [] | "4" | Create left(4) | 1→2,3→4 |
| 6 | [] | "5" | Create right(5) | 1→2,3→4,5 |

**2.5 Return Result:**

Deserialization returns the original tree structure.

> **Note:** Level-order serialization preserves the tree structure naturally, making it easier to reconstruct than preorder/inorder approaches.

