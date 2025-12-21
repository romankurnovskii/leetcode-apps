from typing import List

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:


class Solution:
    def read(self, buf: List[str], n: int) -> int:
        buf4 = [""] * 4
        total = 0

        while total < n:
            count = read4(buf4)
            if count == 0:
                break

            copy_count = min(count, n - total)
            buf[total : total + copy_count] = buf4[:copy_count]
            total += copy_count

        return total
