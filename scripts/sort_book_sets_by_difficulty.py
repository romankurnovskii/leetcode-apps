#!/usr/bin/env python3
"""
Script to sort problems in book-sets.json by difficulty (Easy -> Medium -> Hard).

By default, sorts:
- "LeetCode 75"
- "LeetCode Top 150"
- "Top 100 Liked Questions"

Usage:
    python scripts/sort_book_sets_by_difficulty.py
    python scripts/sort_book_sets_by_difficulty.py --all  # Sort all sets
    python scripts/sort_book_sets_by_difficulty.py --set "LeetCode 75"  # Sort specific set
"""

import json
import os
import sys
import argparse
import subprocess
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
BOOK_SETS_PATH = ROOT_DIR / "data" / "book-sets.json"
LEETCODE_PROBLEMS_PATH = ROOT_DIR / "data" / "leetcode-problems.json"

# Default sets to sort
DEFAULT_SETS = ["LeetCode 75", "LeetCode Top 150", "Top 100 Liked Questions"]

# Difficulty order for sorting
DIFFICULTY_ORDER = {"Easy": 0, "Medium": 1, "Hard": 2, "Unknown": 3}


def load_json_file(file_path):
    """Load JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {file_path}: {e}")
        sys.exit(1)


def get_problem_difficulty(problem_id, problems_data):
    """Get difficulty for a problem ID."""
    problem_str = str(problem_id)
    if problem_str in problems_data:
        return problems_data[problem_str].get("difficulty", "Unknown")
    return "Unknown"


def sort_problems_by_difficulty(problem_ids, problems_data):
    """Sort problem IDs by difficulty (Easy -> Medium -> Hard)."""
    # Create list of (problem_id, difficulty_order)
    problems_with_order = []
    for pid in problem_ids:
        difficulty = get_problem_difficulty(pid, problems_data)
        order = DIFFICULTY_ORDER.get(difficulty, 3)
        problems_with_order.append((pid, order, difficulty))

    # Sort by difficulty order, then by problem ID (for stable sorting within same difficulty)
    problems_with_order.sort(key=lambda x: (x[1], x[0]))

    # Return sorted problem IDs
    return [pid for pid, _, _ in problems_with_order]


def sort_book_set(book_set, problems_data, verbose=False):
    """Sort problems in a book set by difficulty."""
    title = book_set.get("title", "Unknown")
    problems = book_set.get("problems", [])

    if not problems:
        if verbose:
            print(f"  {title}: No problems to sort")
        return False

    # Sort problems
    sorted_problems = sort_problems_by_difficulty(problems, problems_data)

    # Check if order changed
    if sorted_problems == problems:
        if verbose:
            print(f"  {title}: Already sorted ({len(problems)} problems)")
        return False

    # Update the set
    book_set["problems"] = sorted_problems

    if verbose:
        # Show difficulty breakdown
        easy = sum(
            1
            for pid in sorted_problems
            if get_problem_difficulty(pid, problems_data) == "Easy"
        )
        medium = sum(
            1
            for pid in sorted_problems
            if get_problem_difficulty(pid, problems_data) == "Medium"
        )
        hard = sum(
            1
            for pid in sorted_problems
            if get_problem_difficulty(pid, problems_data) == "Hard"
        )
        unknown = len(sorted_problems) - easy - medium - hard

        print(f"  {title}: Sorted {len(sorted_problems)} problems")
        print(
            f"    Easy: {easy}, Medium: {medium}, Hard: {hard}"
            + (f", Unknown: {unknown}" if unknown > 0 else "")
        )
        print(f"    First: {sorted_problems[0]}, Last: {sorted_problems[-1]}")

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Sort problems in book-sets.json by difficulty (Easy -> Medium -> Hard)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Sort all book sets (default: only LeetCode 75, Top 150, and Top 100 Liked)",
    )
    parser.add_argument("--set", type=str, help="Sort a specific book set by title")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be sorted without making changes",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show detailed output"
    )

    args = parser.parse_args()

    # Load data
    print("Loading data files...")
    book_sets = load_json_file(BOOK_SETS_PATH)
    problems_data = load_json_file(LEETCODE_PROBLEMS_PATH)

    # Determine which sets to sort
    if args.set:
        sets_to_sort = [args.set]
    elif args.all:
        sets_to_sort = [
            book_set["title"] for book_set in book_sets if "problems" in book_set
        ]
    else:
        sets_to_sort = DEFAULT_SETS

    print(f"\nSorting {len(sets_to_sort)} book set(s)...")
    if args.verbose:
        print(f"Sets to sort: {', '.join(sets_to_sort)}")
    print()

    # Sort each set
    updated_count = 0
    for book_set in book_sets:
        title = book_set.get("title", "Unknown")

        if title not in sets_to_sort:
            continue

        if args.verbose or args.dry_run:
            print(f"Processing: {title}")

        if sort_book_set(book_set, problems_data, verbose=args.verbose or args.dry_run):
            updated_count += 1

        if args.verbose or args.dry_run:
            print()

    # Save if not dry run
    if args.dry_run:
        print(f"Dry run complete. Would update {updated_count} set(s).")
    else:
        if updated_count > 0:
            # Save updated book-sets.json
            with open(BOOK_SETS_PATH, "w", encoding="utf-8") as f:
                json.dump(book_sets, f, ensure_ascii=False)
            
            # Format with prettier
            try:
                subprocess.run(
                    ["npx", "prettier", "--write", str(BOOK_SETS_PATH)],
                    check=True,
                    capture_output=True,
                )
            except subprocess.CalledProcessError as e:
                print(f"Warning: Prettier formatting failed: {e}")
            except FileNotFoundError:
                print("Warning: npx/prettier not found, skipping formatting")
            
            print(f"✓ Updated {updated_count} book set(s) in {BOOK_SETS_PATH}")
        else:
            print("No changes needed. All sets are already sorted.")


if __name__ == "__main__":
    main()
