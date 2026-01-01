class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
        }

        res = text
        for entity, char in entities.items():
            res = res.replace(entity, char)

        return res
