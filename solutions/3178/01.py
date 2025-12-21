class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # The pattern repeats every 2 * (n - 1) seconds
        # After this period, we're back to child 0 going right
        period = 2 * (n - 1)
        k_mod = k % period

        # Simulate the movement
        pos = 0
        direction = 1  # 1 for right, -1 for left

        for _ in range(k_mod):
            pos += direction
            # Reverse direction at boundaries
            if pos == 0 or pos == n - 1:
                direction = -direction

        return pos
