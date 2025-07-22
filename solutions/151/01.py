def reverseWords(s: str) -> str:
    words = s.split()
    words.reverse()
    return ' '.join(words)