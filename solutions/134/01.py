class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        current_tank = 0
        start = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_tank += gas[i] - cost[i]

            # If current_tank < 0, we can't start from any station
            # in the range [start, i], so try starting from i+1
            if current_tank < 0:
                start = i + 1
                current_tank = 0

        # If total gas < total cost, it's impossible
        if total_gas < total_cost:
            return -1

        return start
