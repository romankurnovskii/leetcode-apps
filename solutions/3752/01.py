class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> list[int]:
        # 1. Calculate the maximum possible sum (all positives)
        total_sum = n * (n + 1) // 2

        # 2. Check Feasibility (Bounds AND Parity)
        # BUG FIX: We must check if target is smaller than the minimum possible sum (-total_sum)
        if target < -total_sum or target > total_sum:
            return []

        diff = total_sum - target

        if diff % 2 != 0:
            return []

        # 3. Calculate "Negative Budget"
        # This is the sum of the subset of numbers we must flip to negative
        negative_budget = diff // 2

        is_negative = [False] * (n + 1)

        # 4. Greedy Selection: Pick largest numbers first
        for i in range(n, 0, -1):
            if i <= negative_budget:
                is_negative[i] = True
                negative_budget -= i

        # Safety check: If we couldn't spend the full budget, it's impossible
        # (Though with the bounds check above, this is mathematically guaranteed for 1..n)
        if negative_budget != 0:
            return []

        res = []
        for i in range(1, n + 1):
            if is_negative[i]:
                res.append(-i)
            else:
                res.append(i)

        # 5. Sort to ensure lexicographically smallest order
        res.sort()

        return res

