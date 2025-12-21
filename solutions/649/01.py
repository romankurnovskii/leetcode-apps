class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = []
        d_queue = []

        for i, party in enumerate(senate):
            if party == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        n = len(senate)

        while r_queue and d_queue:
            r_idx = r_queue.pop(0)
            d_idx = d_queue.pop(0)

            if r_idx < d_idx:
                r_queue.append(r_idx + n)
            else:
                d_queue.append(d_idx + n)

        return "Radiant" if r_queue else "Dire"
