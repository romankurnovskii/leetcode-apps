class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        left, right = 1, n

        for i in range(n):
            # For the first k-1 elements, alternate between left and right
            # to create k distinct differences
            if k > 1:
                # Alternate: if k is odd, take from left; if even, take from right
                if k % 2 == 1:
                    res.append(left)
                    left += 1
                else:
                    res.append(right)
                    right -= 1
                k -= 1
            else:
                # After creating k-1 distinct differences, fill rest with consecutive numbers
                res.append(left)
                left += 1

        return res
