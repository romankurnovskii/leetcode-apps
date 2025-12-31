from typing import List


class Solution:
    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        from collections import defaultdict, deque

        # Assign groups to items without groups
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        # Build graphs for items and groups
        item_graph = defaultdict(list)
        item_indegree = [0] * n
        group_graph = defaultdict(set)
        group_indegree = defaultdict(int)

        for i in range(n):
            for prev in beforeItems[i]:
                item_graph[prev].append(i)
                item_indegree[i] += 1

                if group[prev] != group[i]:
                    if group[i] not in group_graph[group[prev]]:
                        group_graph[group[prev]].add(group[i])
                        group_indegree[group[i]] += 1

        # Topological sort for groups
        group_queue = deque([g for g in range(group_id) if group_indegree[g] == 0])
        group_order = []

        while group_queue:
            g = group_queue.popleft()
            group_order.append(g)
            for next_group in group_graph[g]:
                group_indegree[next_group] -= 1
                if group_indegree[next_group] == 0:
                    group_queue.append(next_group)

        if len(group_order) != group_id:
            return []

        # Topological sort for items within each group
        items_in_group = defaultdict(list)
        for i in range(n):
            items_in_group[group[i]].append(i)

        res = []
        for g in group_order:
            items = items_in_group[g]
            item_queue = deque([item for item in items if item_indegree[item] == 0])
            count = 0

            while item_queue:
                item = item_queue.popleft()
                res.append(item)
                count += 1

                for next_item in item_graph[item]:
                    item_indegree[next_item] -= 1
                    if group[next_item] == g and item_indegree[next_item] == 0:
                        item_queue.append(next_item)

            if count != len(items):
                return []

        return res
