## Explanation

### Strategy (The "Why")

Given a directed acyclic graph (DAG) with $n$ nodes labeled from 0 to $n-1$ and a list of edges, we need to find the smallest set of vertices from which all nodes in the graph are reachable.

**1.1 Constraints & Complexity:**

- **Input Size:** $n$ can be between $2$ and $10^5$, and the number of edges can be up to $10^5$.
- **Value Range:** Node labels are between $0$ and $n-1$.
- **Time Complexity:** $O(n + e)$ where $e$ is the number of edges. We iterate through edges once, then through all nodes once.
- **Space Complexity:** $O(n)$ - We use an array of size $n$ to track incoming edges.
- **Edge Case:** If there are no edges, all nodes are sources (no incoming edges), so return all nodes. If the graph is a chain, only the first node is needed.

**1.2 High-level approach:**

The goal is to find all nodes that have no incoming edges (source nodes).

In a DAG, if a node has no incoming edges, it cannot be reached from any other node, so it must be in our set. Conversely, if a node has incoming edges, it can be reached from those sources.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each node, check if it's reachable from other nodes. This would be inefficient.
- **Optimized Strategy (Counting):** Count incoming edges for each node. Nodes with zero incoming edges are the answer. This takes $O(n + e)$ time.
- **Why it's better:** The counting approach is optimal and straightforward. We only need to identify nodes with no incoming edges, which can be done in one pass.

**1.4 Decomposition:**

1. Create an array to track which nodes have incoming edges.
2. Iterate through all edges, marking the destination node as having an incoming edge.
3. Collect all nodes that don't have incoming edges.
4. Return the list of source nodes.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $n = 6$, $edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]$

We initialize:
- `has_incoming = [False, False, False, False, False, False]`

**2.2 Start Processing:**

We iterate through all edges.

**2.3 Trace Walkthrough:**

| Edge | to_node | has_incoming[to_node] After |
|------|---------|----------------------------|
| [0,1] | 1 | True |
| [0,2] | 2 | True |
| [2,5] | 5 | True |
| [3,4] | 4 | True |
| [4,2] | 2 | True (already True) |

After processing: `has_incoming = [False, True, True, False, True, True]`

**2.4 Find Source Nodes:**

Nodes with `has_incoming[i] = False`: 0 and 3

**2.5 Return Result:**

We return `[0, 3]`, which are the nodes with no incoming edges. All other nodes can be reached from these nodes.

> **Note:** The key insight is that in a DAG, nodes with no incoming edges are the "sources" and must be included. All other nodes can be reached from these sources through the edges.

