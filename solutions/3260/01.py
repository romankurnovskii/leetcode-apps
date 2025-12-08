class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        # Build palindrome from outside to inside
        # Use DP: track remainder as we build
        
        def build(pos, rem, pal_list):
            if pos >= (n + 1) // 2:
                if rem == 0:
                    return ''.join(pal_list)
                return None
            
            mirror_pos = n - 1 - pos
            best = None
            
            for digit in range(9, -1, -1):
                if pos == 0 and digit == 0:
                    continue
                
                # Calculate remainder contribution
                if pos == mirror_pos:
                    # Center position (odd n)
                    power = pow(10, pos, k)
                    new_rem = (rem + digit * power) % k
                    new_pal = pal_list[:]
                    new_pal[pos] = str(digit)
                else:
                    # Symmetric positions
                    left_power = pow(10, pos, k)
                    right_power = pow(10, mirror_pos, k)
                    new_rem = (rem + digit * (left_power + right_power)) % k
                    new_pal = pal_list[:]
                    new_pal[pos] = str(digit)
                    new_pal[mirror_pos] = str(digit)
                
                result = build(pos + 1, new_rem, new_pal)
                if result and (not best or result > best):
                    best = result
                if best:
                    break  # Found largest, no need to try smaller digits
            
            return best
        
        pal_list = [''] * n
        res = build(0, 0, pal_list)
        return res if res else str(k) * n
