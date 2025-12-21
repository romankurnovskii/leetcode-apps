class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(b)] = find(a)

        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])

        # Initially, person 0 and firstPerson know the secret
        union(0, firstPerson)

        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            involved = []

            # Process all meetings at the same time
            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                union(x, y)
                involved.append(x)
                involved.append(y)
                i += 1

            # Reset connections that don't include person 0
            # Only people connected to person 0 keep the secret
            root0 = find(0)
            for p in involved:
                if find(p) != root0:
                    parent[p] = p

        # Return all people connected to person 0
        return [i for i in range(n) if find(i) == find(0)]
