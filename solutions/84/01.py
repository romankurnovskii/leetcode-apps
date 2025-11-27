from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stack of indices
        max_area = 0
        
        for i, height in enumerate(heights):
            # While current height is less than stack top, calculate area
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)
        
        # Process remaining bars in stack
        while stack:
            h = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, h * width)
        
        return max_area

