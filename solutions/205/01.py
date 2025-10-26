def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    # Create mapping dictionaries for both directions
    s_to_t = {}
    t_to_s = {}
    
    # Check each character pair
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        # Check if char_s is already mapped
        if char_s in s_to_t:
            # Verify the mapping is consistent
            if s_to_t[char_s] != char_t:
                return False
        else:
            # Check if char_t is already mapped to by another character
            if char_t in t_to_s:
                return False
            
            # Add new mapping
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
    
    return True
