def isSubsequence(s: str, t: str) -> bool:
    s_ptr = 0
    t_ptr = 0

    # Iterate while both pointers are within their string bounds
    while s_ptr < len(s) and t_ptr < len(t):
        # If characters match, advance the pointer for s
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        # Always advance the pointer for t
        t_ptr += 1
    
    # If 's' pointer has reached the end of s, it means all characters of s were found in t
    res = s_ptr == len(s)
    return res