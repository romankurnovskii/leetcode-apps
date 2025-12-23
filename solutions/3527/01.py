from collections import defaultdict

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = defaultdict(int)
        
        # Count each unique response from each day
        for daily in responses:
            # Use set to remove duplicates within each day
            for response in set(daily):
                count[response] += 1
        
        # Find maximum frequency
        max_count = max(count.values())
        
        # Return lexicographically smallest response with max frequency
        res = min(response for response, cnt in count.items() if cnt == max_count)
        
        return res

