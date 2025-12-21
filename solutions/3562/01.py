class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        from collections import defaultdict
        from functools import lru_cache

        # Build adjacency list (0-indexed)
        adj_list = defaultdict(list)
        for u, v in hierarchy:
            adj_list[u - 1].append(v - 1)

        @lru_cache(maxsize=None)
        def dfs(employee, has_discount):
            # Calculate cost and profit for current employee
            cost = present[employee] // 2 if has_discount else present[employee]
            profit = future[employee] - cost

            # Option 1: Buy current stock
            buy_current = {}
            if cost <= budget:
                buy_current[cost] = profit

            # Option 2: Skip current stock
            skip_current = {0: 0}

            # Process children using knapsack approach
            for child in adj_list[employee]:
                # Get child results with and without discount
                child_with_discount = dfs(
                    child, True
                )  # If we buy current, child gets discount
                child_no_discount = dfs(
                    child, False
                )  # If we skip current, child has no discount

                # Merge buy_current with child results
                new_buy = {}
                for spent, prof in buy_current.items():
                    for child_spent, child_prof in child_with_discount.items():
                        total_spent = spent + child_spent
                        if total_spent <= budget:
                            total_prof = prof + child_prof
                            if (
                                total_spent not in new_buy
                                or new_buy[total_spent] < total_prof
                            ):
                                new_buy[total_spent] = total_prof
                buy_current = new_buy

                # Merge skip_current with child results
                new_skip = {}
                for spent, prof in skip_current.items():
                    for child_spent, child_prof in child_no_discount.items():
                        total_spent = spent + child_spent
                        if total_spent <= budget:
                            total_prof = prof + child_prof
                            if (
                                total_spent not in new_skip
                                or new_skip[total_spent] < total_prof
                            ):
                                new_skip[total_spent] = total_prof
                skip_current = new_skip

            # Merge buy and skip results
            result = {}
            for spent, prof in buy_current.items():
                if spent not in result or result[spent] < prof:
                    result[spent] = prof
            for spent, prof in skip_current.items():
                if spent not in result or result[spent] < prof:
                    result[spent] = prof

            return result

        result = dfs(0, False)  # Root has no parent, so no discount
        return max(result.values()) if result else 0
