def makeFancyString(s: str) -> str:
    res = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == res[-1]:
            count += 1
            if count < 3:
                res += s[i]
        else:
            count = 1
            res += s[i]
    return res
