class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        size = k * 2 + 1
        x = (n + size - 1) // size  # ceil(n / size)
        y = (m + size - 1) // size  # ceil(m / size)
        return x * y

