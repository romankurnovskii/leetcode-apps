# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize matrix with -1
        res = [[-1] * n for _ in range(m)]
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        row, col = 0, 0
        
        current = head
        while current:
            res[row][col] = current.val
            current = current.next
            
            if not current:
                break
            
            # Try to move in current direction
            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]
            
            # Check if we need to change direction
            if (next_row < 0 or next_row >= m or 
                next_col < 0 or next_col >= n or 
                res[next_row][next_col] != -1):
                dir_idx = (dir_idx + 1) % 4
            
            row += directions[dir_idx][0]
            col += directions[dir_idx][1]
        
        return res
