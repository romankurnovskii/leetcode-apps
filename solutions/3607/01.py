from typing import List
from collections import defaultdict
import bisect


def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(parent, x, y):
    px, py = find(parent, x), find(parent, y)
    if px != py:
        parent[py] = px


def build_components(c, connections, parent):
    for u, v in connections:
        union(parent, u, v)
    comp_map = defaultdict(list)
    for i in range(1, c + 1):
        comp_map[find(parent, i)].append(i)
    return comp_map


def build_online(comp_map):
    online = {}
    for comp, nodes in comp_map.items():
        online[comp] = nodes[:]
    return online


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        parent = list(range(c + 1))
        comp_map = build_components(c, connections, parent)
        online = build_online(comp_map)
        is_online = [True] * (c + 1)
        station_to_comp = {i: find(parent, i) for i in range(1, c + 1)}
        res = []
        for qtype, x in queries:
            comp = station_to_comp[x]
            arr = online[comp]
            if qtype == 2:
                if is_online[x]:
                    idx = bisect.bisect_left(arr, x)
                    if idx < len(arr) and arr[idx] == x:
                        arr.pop(idx)
                    is_online[x] = False
            else:  # qtype == 1
                if is_online[x]:
                    res.append(x)
                elif arr:
                    res.append(arr[0])
                else:
                    res.append(-1)
        return res
