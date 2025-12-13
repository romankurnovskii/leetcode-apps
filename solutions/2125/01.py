from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Count devices in each row
        device_counts = []
        for row in bank:
            count = row.count('1')
            if count > 0:  # Only include rows with devices
                device_counts.append(count)
        
        # Calculate total beams
        res = 0
        for i in range(len(device_counts) - 1):
            # Beams between adjacent rows with devices
            res += device_counts[i] * device_counts[i + 1]
        
        return res

