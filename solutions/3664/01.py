class Solution:
    def score(self, cards: List[str], x: str) -> int:
        # Count cards by type:
        # - both: cards where both chars are x (e.g., "xx")
        # - first: cards where first char is x (e.g., "xa", "xb")
        # - second: cards where second char is x (e.g., "ax", "bx")
        from collections import defaultdict

        both = 0
        first = defaultdict(int)  # first[x] = count of cards like "xc"
        second = defaultdict(int)  # second[x] = count of cards like "cx"

        for card in cards:
            if card[0] == x and card[1] == x:
                both += 1
            elif card[0] == x:
                first[card[1]] += 1
            elif card[1] == x:
                second[card[0]] += 1

        # Count pairs from first and second groups
        # Cards are compatible if they differ in exactly 1 position
        # So "xa" and "ax" are compatible (differ at position 0)
        # "xa" and "xb" are compatible (differ at position 1)
        res = 0

        # Pair cards from first group with same second char
        for count in first.values():
            res += count // 2

        # Pair cards from second group with same first char
        for count in second.values():
            res += count // 2

        # Pair cards from first and second groups
        # "xa" pairs with "ax" (compatible - differ at position 0)
        for char in first:
            if char in second:
                pairs = min(first[char], second[char])
                res += pairs
                first[char] -= pairs
                second[char] -= pairs

        # Use "both" cards to pair with remaining first or second
        # "xx" can pair with "xa" or "ax"
        remaining_first = sum(first.values())
        remaining_second = sum(second.values())

        # Try different distributions of "both" cards
        max_pairs = res
        for i in range(both + 1):
            # Use i "both" cards with first group, (both - i) with second group
            first_pairs = (remaining_first + i) // 2
            second_pairs = (remaining_second + (both - i)) // 2
            max_pairs = max(max_pairs, res + first_pairs + second_pairs)

        return max_pairs
