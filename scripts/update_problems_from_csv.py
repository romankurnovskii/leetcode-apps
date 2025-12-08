#!/usr/bin/env python3

"""
Script to update leetcode-problems.json from CSV file.
Fills in all missing problems from the CSV.
"""

import json
import csv
import re
import os
import sys
from collections import OrderedDict

# Paths
CSV_PATH = "data/LeetCode Questions - Last Updated 2025-11-24 04_04 CET - LeetCode Questions.csv"
JSON_PATH = "data/leetcode-problems.json"


def map_topics_to_category(topics_str):
    """Map Topics string to JSON category format."""
    if not topics_str or topics_str.strip() == "":
        return "Array & Hashing"

    topics = [t.strip() for t in topics_str.split(",")]
    topics_lower = [t.lower() for t in topics]

    # Priority mapping based on existing JSON structure
    if any("database" in t for t in topics_lower):
        return "Database"
    elif any("tree" in t or "binary tree" in t or "bst" in t for t in topics_lower):
        return "Tree"
    elif any(
        "graph" in t
        or "dfs" in t
        or "depth-first" in t
        or "bfs" in t
        or "breadth-first" in t
        or "union find" in t
        for t in topics_lower
    ):
        return "Graph Traversal"
    elif any(
        "dynamic programming" in t or "dp" in t or "memoization" in t
        for t in topics_lower
    ):
        return "Dynamic Programming"
    elif any("backtracking" in t for t in topics_lower):
        return "Backtracking"
    elif any("sliding window" in t for t in topics_lower):
        return "Sliding Window"
    elif any("binary search" in t for t in topics_lower):
        return "Binary Search"
    elif any("heap" in t or "priority queue" in t for t in topics_lower):
        return "Heap (Priority Queue)"
    elif any("stack" in t or "monotonic stack" in t for t in topics_lower):
        return "Stack"
    elif any("linked list" in t for t in topics_lower):
        return "Linked List"
    elif any("trie" in t or "prefix tree" in t for t in topics_lower):
        return "Trie"
    elif any("bit manipulation" in t or "bit" in t for t in topics_lower):
        return "Bit Manipulation"
    elif any("greedy" in t for t in topics_lower):
        return "Greedy"
    elif any(
        "math" in t or "geometry" in t or "number theory" in t or "combinatorics" in t
        for t in topics_lower
    ):
        return "Math & Geometry"
    elif any("two pointers" in t for t in topics_lower):
        return "Two Pointers"
    elif any("intervals" in t for t in topics_lower):
        return "Intervals"
    elif any("topological" in t for t in topics_lower):
        return "Topological Sort"
    elif any("array" in t or "hash table" in t or "hash" in t for t in topics_lower):
        return "Array & Hashing"
    elif any("string" in t for t in topics_lower):
        return "Array & Hashing"
    else:
        return "Array & Hashing"  # default


def title_to_slug(title):
    """Convert problem title to URL slug format."""
    slug = title.lower()
    # Remove special characters except spaces and hyphens
    slug = re.sub(r"[^\w\s-]", "", slug)
    # Replace spaces and multiple hyphens with single hyphen
    slug = re.sub(r"[-\s]+", "-", slug)
    # Remove leading/trailing hyphens
    slug = slug.strip("-")
    return slug


def load_csv_problems():
    """Load all problems from CSV file."""
    problems = {}

    if not os.path.exists(CSV_PATH):
        print(f"Error: CSV file not found at {CSV_PATH}")
        return problems

    try:
        with open(CSV_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    problem_id = int(row["ID"])
                    title = row["Problem Name"]
                    difficulty = row["Difficulty"]
                    topics = row["Topics"]

                    category = map_topics_to_category(topics)
                    slug = title_to_slug(title)
                    link = f"https://leetcode.com/problems/{slug}/"

                    problems[str(problem_id)] = {
                        "id": problem_id,
                        "category": category,
                        "title": title,
                        "difficulty": difficulty,
                        "link": link,
                    }
                except (ValueError, KeyError) as e:
                    print(f"Warning: Skipping row due to error: {e}")
                    continue
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return problems

    return problems


def load_existing_json():
    """Load existing JSON file."""
    if not os.path.exists(JSON_PATH):
        return {}

    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return {}


def save_json(data):
    """Save JSON file sorted by problem ID."""
    try:
        # Sort by problem ID (convert key to int for proper numeric sorting)
        sorted_items = sorted(
            data.items(),
            key=lambda item: int(item[0]) if item[0].isdigit() else float("inf"),
        )
        sorted_data = OrderedDict(sorted_items)

        # Write JSON (Prettier will format it via pre-commit hook)
        with open(JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(sorted_data, f, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return False


def main():
    """Main function to update JSON from CSV."""
    print("Loading CSV file...")
    csv_problems = load_csv_problems()
    print(f"Loaded {len(csv_problems)} problems from CSV")

    print("Loading existing JSON file...")
    existing_json = load_existing_json()
    print(f"Found {len(existing_json)} problems in existing JSON")

    # Find missing and updated problems
    missing = []
    updated = []

    for problem_id, problem_data in csv_problems.items():
        if problem_id not in existing_json:
            missing.append(problem_id)
            existing_json[problem_id] = problem_data
        else:
            # Update existing entry (in case data changed)
            existing_json[problem_id] = problem_data
            updated.append(problem_id)

    print("-" * 20)
    print(f"Found {len(missing)} missing problems")
    print(f"Updated {len(updated)} existing problems")

    if missing:
        print("\nMissing problems (first 20):")
        for pid in sorted(missing, key=int)[:20]:
            print(f"  {pid}: {csv_problems[pid]['title']}")
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more")

    # Save updated JSON
    print(f"\nSaving updated JSON to {JSON_PATH}...")
    if save_json(existing_json):
        print(f"Successfully saved {len(existing_json)} problems to JSON")
    else:
        print("Failed to save JSON")
        sys.exit(1)


if __name__ == "__main__":
    main()
