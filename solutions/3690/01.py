class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import deque

        # BFS to find minimum operations
        queue = deque([(tuple(nums1), 0)])
        visited = {tuple(nums1)}
        target = tuple(nums2)

        while queue:
            state, ops = queue.popleft()

            if state == target:
                return ops

            # Try all possible split-and-merge operations
            n = len(state)
            for l in range(n):
                for r in range(l, n):
                    # Remove subarray [l..r]
                    removed = state[l : r + 1]
                    prefix = state[:l]
                    suffix = state[r + 1 :]

                    # Try inserting at all possible positions
                    for pos in range(len(prefix) + len(suffix) + 1):
                        new_state = prefix[:pos] + removed + prefix[pos:] + suffix
                        new_state_tuple = tuple(new_state)

                        if new_state_tuple not in visited:
                            visited.add(new_state_tuple)
                            queue.append((new_state_tuple, ops + 1))

        return -1
