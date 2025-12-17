class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        # Initialize linked list: d[i] = i+1 for all i from 0 to n-2
        d = {i: i + 1 for i in range(n - 1)}
        res = []

        for i, j in queries:
            # If we have a link from i and it goes to a node before j
            if i in d and d[i] < j:
                # Remove all nodes between i and j
                v = i
                while v < j and v in d:
                    v = d.pop(v)
                # Add direct link from i to j
                d[i] = j

            # Shortest path length = number of edges = size of dictionary
            res.append(len(d))

        return res
