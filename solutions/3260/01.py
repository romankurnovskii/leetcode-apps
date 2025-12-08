class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        # For very large n, use optimized construction
        # Build palindrome digit by digit, only keeping best per remainder
        
        # dp[rem] = tuple of digits (first half only)
        dp = {0: ()}
        
        half = (n + 1) // 2
        
        for pos in range(half):
            new_dp = {}
            
            for rem, digits in dp.items():
                # Try digits 9 down to 0, but stop early if we find a solution
                found_solution = False
                
                for digit in range(9, -1, -1):
                    if pos == 0 and digit == 0:
                        continue
                    
                    mirror_pos = n - 1 - pos
                    
                    # Calculate new remainder
                    if pos == mirror_pos:
                        power = pow(10, pos, k)
                        new_rem = (rem + digit * power) % k
                    else:
                        left_power = pow(10, pos, k)
                        right_power = pow(10, mirror_pos, k)
                        new_rem = (rem + digit * (left_power + right_power)) % k
                    
                    new_digits = digits + (digit,)
                    
                    # Keep best for this remainder
                    if new_rem not in new_dp or new_digits > new_dp[new_rem]:
                        new_dp[new_rem] = new_digits
                    
                    # Early check: if this is the last position and remainder is 0, we're done
                    if pos == half - 1 and new_rem == 0:
                        found_solution = True
                        # Reconstruct and return immediately
                        pal_list = [''] * n
                        for i, d in enumerate(new_digits):
                            pal_list[i] = str(d)
                            if i != n - 1 - i:
                                pal_list[n - 1 - i] = str(d)
                        res = ''.join(pal_list)
                        if len(res) == n and res[0] != '0':
                            return res
                
                # If we found a solution, we can break early
                if found_solution:
                    break
            
            dp = new_dp
            # Limit states: only keep best candidate per remainder
            # This prevents explosion of states
            
        # Final reconstruction
        if 0 in dp:
            digits = dp[0]
            pal_list = [''] * n
            for i, d in enumerate(digits):
                pal_list[i] = str(d)
                if i != n - 1 - i:
                    pal_list[n - 1 - i] = str(d)
            res = ''.join(pal_list)
            if len(res) == n and res[0] != '0':
                return res
        
        return str(k) * n
