class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        # Edge case: no items needed
        if need1 == 0 and need2 == 0:
            return 0

        # Strategy 1: Buy all individual items
        res = need1 * cost1 + need2 * cost2

        # Strategy 2: Buy min(need1, need2) "both" items for overlap,
        # then buy individual items for the remaining needs
        overlap = min(need1, need2)
        res = min(
            res,
            overlap * costBoth + (need1 - overlap) * cost1 + (need2 - overlap) * cost2,
        )

        # Strategy 3: Buy max(need1, need2) "both" items
        # This over-satisfies one requirement but might be cheaper
        max_need = max(need1, need2)
        res = min(res, max_need * costBoth)

        return res
