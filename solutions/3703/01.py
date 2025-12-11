class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        # Stack stores [character, count] pairs
        st = []

        for c in s:
            if st and st[-1][0] == c:
                # Same character, increment count
                st[-1][1] += 1
            else:
                # Different character, push new entry
                st.append([c, 1])

            # Check if the last two groups form a k-balanced substring
            n = len(st)
            if (
                n >= 2
                and st[n - 2][0] == "("
                and st[n - 2][1] >= k
                and st[n - 1][0] == ")"
                and st[n - 1][1] == k
            ):

                # Remove k opening parentheses
                st[n - 2][1] -= k

                # Remove the closing parentheses group
                st.pop()

                # Remove the opening parentheses group if its count is now 0
                if st[-1][1] == 0:
                    st.pop()

        # Reconstruct the result string from remaining groups
        result = ""
        for char, count in st:
            result += char * count

        return result
