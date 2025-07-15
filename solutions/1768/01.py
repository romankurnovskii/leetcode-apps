def mergeAlternately(word1, word2):
    res = []
    i = 0
    while i < len(word1) and i < len(word2):
        res.append(word1[i])
        res.append(word2[i])
        i += 1
    res.append(word1[i:])
    res.append(word2[i:])
    return "".join(res)
