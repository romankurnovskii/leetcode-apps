from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # Valid business lines in priority order
        valid_business_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        priority = {line: i for i, line in enumerate(valid_business_lines)}
        
        res = []
        
        for i in range(len(code)):
            # Check if coupon is active
            if not isActive[i]:
                continue
            
            # Check if code is non-empty and contains only alphanumeric and underscore
            if not code[i] or not all(c.isalnum() or c == '_' for c in code[i]):
                continue
            
            # Check if business line is valid
            if businessLine[i] not in priority:
                continue
            
            # Coupon is valid, add to result with priority info for sorting
            res.append((priority[businessLine[i]], code[i]))
        
        # Sort by business line priority, then by code lexicographically
        res.sort()
        
        # Return only the codes
        return [code for _, code in res]
