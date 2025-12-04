from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        queue = deque([(startGene, 0)])
        visited = {startGene}
        
        while queue:
            gene, mutations = queue.popleft()
            
            if gene == endGene:
                return mutations
            
            # Try all possible mutations
            for i in range(len(gene)):
                for char in ['A', 'C', 'G', 'T']:
                    if gene[i] != char:
                        new_gene = gene[:i] + char + gene[i+1:]
                        if new_gene in bank_set and new_gene not in visited:
                            visited.add(new_gene)
                            queue.append((new_gene, mutations + 1))
        
        return -1

