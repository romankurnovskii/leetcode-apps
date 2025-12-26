class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # Calculate total apples needed
        total_apples = sum(apple)

        # Sort boxes by capacity in descending order (greedy: use largest boxes first)
        capacity.sort(reverse=True)

        # Greedily select boxes until all apples are packed
        boxes_used = 0
        remaining_apples = total_apples

        for cap in capacity:
            if remaining_apples <= 0:
                break
            remaining_apples -= cap
            boxes_used += 1

        return boxes_used
