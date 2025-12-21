def hIndex(citations):
    """
    Calculate the h-index for a researcher based on their paper citations.

    Args:
        citations: List[int] - Array of citation counts for each paper

    Returns:
        int - The researcher's h-index
    """
    # Handle edge cases
    if not citations:
        return 0

    # Sort citations in descending order
    citations.sort(reverse=True)

    # Check each position as a potential h-index
    for i in range(len(citations)):
        # h-index is i + 1 (1-indexed)
        h = i + 1

        # Check if citations[i] >= h
        # If not, we've found our answer
        if citations[i] < h:
            return i

        # If we reach the end, the h-index is the length of the array
        if i == len(citations) - 1:
            return h

    # This line should never be reached
    return 0
