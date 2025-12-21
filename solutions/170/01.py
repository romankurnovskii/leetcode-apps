from collections import defaultdict


class TwoSum:
    def __init__(self):
        self.num_counts = defaultdict(int)

    def add(self, number: int) -> None:
        self.num_counts[number] += 1

    def find(self, value: int) -> bool:
        for num in self.num_counts:
            complement = value - num
            if complement in self.num_counts:
                if complement != num or self.num_counts[num] > 1:
                    return True
        return False
