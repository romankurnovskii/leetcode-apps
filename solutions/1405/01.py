from typing import List
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b > 0:
            heapq.heappush(heap, (-b, "b"))
        if c > 0:
            heapq.heappush(heap, (-c, "c"))

        res = []
        while heap:
            count1, char1 = heapq.heappop(heap)
            count1 = -count1

            # Use two of char1 if possible and no conflict
            if len(res) >= 2 and res[-1] == res[-2] == char1:
                if not heap:
                    break
                count2, char2 = heapq.heappop(heap)
                count2 = -count2
                res.append(char2)
                count2 -= 1
                if count2 > 0:
                    heapq.heappush(heap, (-count2, char2))
                heapq.heappush(heap, (-count1, char1))
            else:
                use = min(2, count1)
                res.append(char1 * use)
                count1 -= use
                if count1 > 0:
                    heapq.heappush(heap, (-count1, char1))

        return "".join(res)
