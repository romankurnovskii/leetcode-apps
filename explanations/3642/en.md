## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find books that have "polarized opinions" - books that receive both very high ratings (>= 4) and very low ratings (<= 2) from different readers, with at least 5 reading sessions and a polarization score >= 0.6.

**1.1 Constraints & Complexity:**

- **Input Size:** The reading_sessions table can have many rows per book, with multiple sessions and ratings.
- **Time Complexity:** O(n) where n is the number of reading sessions - we merge tables and group by book_id in a single pass.
- **Space Complexity:** O(m) where m is the number of distinct books - we store aggregated statistics per book.
- **Edge Case:** A book with all extreme ratings (all <= 2 or >= 4) will have a polarization score of 1.0.

**1.2 High-level approach:**

The goal is to merge books with reading sessions, group by book_id, compute rating statistics (highest, lowest, extreme ratings count), calculate polarization score, and filter books that meet all criteria.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Process each book separately, scanning all sessions multiple times to compute statistics. This would be O(n * m) in worst case.
- **Optimized Strategy:** Use pandas merge and groupby with aggregation functions to compute all statistics in a single pass, then filter in one step. This is O(n) time.
- **Optimization:** Pandas operations are vectorized and efficient, allowing us to compute multiple aggregates simultaneously without multiple scans.

**1.4 Decomposition:**

1. Merge books and reading_sessions tables on book_id.
2. Group by book_id and aggregate:
   - Count total sessions
   - Find highest and lowest ratings
   - Check if has rating >= 4
   - Check if has rating <= 2
   - Count extreme ratings (<= 2 or >= 4)
   - Get book details (title, author, genre, pages)
3. Calculate rating spread: highest_rating - lowest_rating
4. Calculate polarization score: extreme_ratings_count / total_sessions
5. Filter books based on all criteria.
6. Sort by polarization_score DESC, title DESC.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's consider book_id 1 (The Great Gatsby) with sessions:
- Session 1: rating 5
- Session 2: rating 1
- Session 3: rating 4
- Session 4: rating 2
- Session 5: rating 5

**2.2 Start Processing:**

We merge books with reading sessions and group by book_id to compute statistics.

**2.3 Trace Walkthrough:**

| Book | total_sessions | highest_rating | lowest_rating | has_high | has_low | extreme_count | rating_spread | polarization_score | Meets criteria? |
|------|----------------|----------------|--------------|----------|---------|---------------|---------------|-------------------|-----------------|
| 1 | 5 | 5 | 1 | Yes | Yes | 5 | 4 | 1.00 | Yes (all) |
| 2 | 5 | 5 | 4 | Yes | No | 5 | 1 | 1.00 | No (no low rating) |
| 3 | 6 | 5 | 1 | Yes | Yes | 6 | 4 | 1.00 | Yes (all) |
| 4 | 2 | 3 | 3 | No | No | 0 | 0 | 0.00 | No (< 5 sessions) |
| 5 | 2 | 2 | 1 | No | Yes | 2 | 1 | 1.00 | No (< 5 sessions) |

For book 1:
- Total sessions >= 5? Yes (5 >= 5) ✓
- Has rating >= 4? Yes ✓
- Has rating <= 2? Yes ✓
- Polarization score >= 0.6? Yes (1.00 >= 0.6) ✓

**2.4 Increment and Loop:**

The pandas merge and groupby operations process all sessions for all books simultaneously, computing aggregates efficiently. The filtering then applies all criteria in one step.

**2.5 Return Result:**

The result includes books 1 and 3 with their details, rating_spread, and polarization_score, ordered by polarization_score DESC, title DESC.

