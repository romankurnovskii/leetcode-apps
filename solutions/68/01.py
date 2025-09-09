class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0

        for word in words:
            # Check if word fits in current line
            if current_length + len(word) + len(current_line) <= maxWidth:
                current_line.append(word)
                current_length += len(word)
            else:
                # Format current line
                result.append(self.formatLine(current_line, maxWidth, False))
                current_line = [word]
                current_length = len(word)

        # Format last line
        if current_line:
            result.append(self.formatLine(current_line, maxWidth, True))

        return result

    def formatLine(self, words: List[str], maxWidth: int, is_last: bool) -> str:
        if is_last or len(words) == 1:
            # Left-justify for last line or single word
            line = " ".join(words)
            return line + " " * (maxWidth - len(line))
        else:
            # Fully justify
            word_lengths = sum(len(word) for word in words)
            total_spaces = maxWidth - word_lengths
            spaces_between = total_spaces // (len(words) - 1)
            extra_spaces = total_spaces % (len(words) - 1)

            result = words[0]
            for i in range(1, len(words)):
                spaces = spaces_between + (1 if i <= extra_spaces else 0)
                result += " " * spaces + words[i]

            return result
