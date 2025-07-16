from collections import Counter


def closeStrings(word1, word2):
    if set(word1) != set(word2):
        return False
    return sorted(Counter(word1).values()) == sorted(Counter(word2).values())
