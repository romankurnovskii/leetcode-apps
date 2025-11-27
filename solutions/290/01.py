def wordPattern(pattern, s):
    """
    Determine if the string s follows the given pattern.
    
    Args:
        pattern: str - The pattern string to match against
        s: str - The string of space-separated words
        
    Returns:
        bool - True if s follows the pattern, False otherwise
    """
    # Split the string into words
    words = s.split()
    
    # Check if pattern length matches word count
    if len(pattern) != len(words):
        return False
    
    # Create mapping dictionaries for both directions
    char_to_word = {}  # maps pattern characters to words
    word_to_char = {}  # maps words to pattern characters
    
    # Check each character-word pair
    for i in range(len(pattern)):
        char = pattern[i]
        word = words[i]
        
        # Check if char is already mapped
        if char in char_to_word:
            # Verify the mapping is consistent
            if char_to_word[char] != word:
                return False
        else:
            # Check if word is already mapped to by another character
            if word in word_to_char:
                return False
            
            # Add new mapping
            char_to_word[char] = word
            word_to_char[word] = char
    
    return True
