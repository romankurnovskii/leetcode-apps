import pandas as pd


def find_books_with_polarized_opinions(
    books: pd.DataFrame, reading_sessions: pd.DataFrame
) -> pd.DataFrame:
    """
    Find books with polarized opinions:
    - At least 5 reading sessions
    - Has at least one rating >= 4 and one rating <= 2
    - Rating spread = highest_rating - lowest_rating
    - Polarization score = (extreme ratings) / total sessions >= 0.6
    """
    # Merge books with reading sessions
    merged = reading_sessions.merge(books, on="book_id", how="inner")

    # Group by book and calculate statistics
    df = (
        merged.groupby("book_id")
        .agg(
            total_sessions=("session_id", "count"),
            highest_rating=("session_rating", "max"),
            lowest_rating=("session_rating", "min"),
            has_high_rating=(
                "session_rating",
                lambda x: (x >= 4).any(),
            ),
            has_low_rating=(
                "session_rating",
                lambda x: (x <= 2).any(),
            ),
            extreme_ratings_count=(
                "session_rating",
                lambda x: ((x <= 2) | (x >= 4)).sum(),
            ),
            title=("title", "first"),
            author=("author", "first"),
            genre=("genre", "first"),
            pages=("pages", "first"),
        )
        .reset_index()
    )

    # Calculate rating spread and polarization score
    df["rating_spread"] = df["highest_rating"] - df["lowest_rating"]
    df["polarization_score"] = df["extreme_ratings_count"] / df["total_sessions"]

    # Apply all criteria
    result = df[
        (df["total_sessions"] >= 5)  # At least 5 sessions
        & (df["has_high_rating"] == True)  # Has rating >= 4
        & (df["has_low_rating"] == True)  # Has rating <= 2
        & (df["polarization_score"] >= 0.6)
    ]  # Polarization score >= 0.6

    # Select and order columns
    result = result[
        [
            "book_id",
            "title",
            "author",
            "genre",
            "pages",
            "rating_spread",
            "polarization_score",
        ]
    ].sort_values(
        ["polarization_score", "title"], ascending=[False, False]
    ).reset_index(drop=True)

    return result

