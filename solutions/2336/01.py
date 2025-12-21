import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.removed = set()
        self.added_back = []
        self.next_num = 1

    def popSmallest(self) -> int:
        if self.added_back:
            res = heapq.heappop(self.added_back)
            self.removed.add(res)
            return res
        else:
            res = self.next_num
            self.next_num += 1
            self.removed.add(res)
            return res

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
            heapq.heappush(self.added_back, num)
