class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        res = []
        rows, cols = len(board), len(board[0])

        def dfs(row, col, node):
            char = board[row][col]
            curr_node = node.children[char]

            # Check if we found a word
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None  # Avoid duplicates

            # Mark as visited
            board[row][col] = "#"

            # Explore neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and board[new_row][new_col] in curr_node.children
                ):
                    dfs(new_row, new_col, curr_node)

            # Restore character
            board[row][col] = char

            # Prune if node has no children
            if not curr_node.children:
                node.children.pop(char)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.children:
                    dfs(i, j, root)

        return res
