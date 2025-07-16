from typing import List


def count_components(n, edges_by_time, t):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px

    for u, v, time in edges_by_time:
        if time > t:
            union(u, v)
    comps = set(find(i) for i in range(n))
    return len(comps)


class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        if k == n:
            return 0
        if not edges:
            return 0 if k <= n else -1
        edges_by_time = sorted(edges, key=lambda x: x[2])
        lo, hi = 0, max(e[2] for e in edges)
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            comps = count_components(n, edges_by_time, mid)
            if comps >= k:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
