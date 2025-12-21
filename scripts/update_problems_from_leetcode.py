#!/usr/bin/env python3

"""
Script to update leetcode-problems.json from LeetCode API.
Fetches problems from LeetCode GraphQL API and adds missing problems.
Uses the frontend problem number (questionFrontendId) as the ID.

Requirements:
    pip install requests
"""

import json
import os
import sys
import time
import requests
from collections import OrderedDict
from typing import Dict, List, Optional

# Paths
JSON_PATH = "data/leetcode-problems.json"

# LeetCode GraphQL API endpoint
LEETCODE_API_URL = "https://leetcode.com/graphql/"

# GraphQL query to fetch problems
PROBLEMS_QUERY = """
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    total: totalNum
    questions: data {
      acRate
      difficulty
      freqBar
      frontendQuestionId: questionFrontendId
      isFavor
      paidOnly: isPaidOnly
      status
      title
      titleSlug
      topicTags {
        name
        slug
      }
      hasSolution
      hasVideoSolution
    }
  }
}
"""


def map_tags_to_category(tags: List[Dict[str, str]]) -> str:
    """Map LeetCode topic tags to JSON category format."""
    if not tags:
        return "Array & Hashing"

    tag_names = [tag.get("name", "").lower() for tag in tags]
    tag_slugs = [tag.get("slug", "").lower() for tag in tags]
    all_tags = tag_names + tag_slugs

    # Priority mapping based on existing JSON structure
    if any("database" in t for t in all_tags):
        return "Database"
    elif any("tree" in t or "binary-tree" in t or "bst" in t for t in all_tags):
        return "Tree"
    elif any(
        "graph" in t
        or "dfs" in t
        or "depth-first" in t
        or "bfs" in t
        or "breadth-first" in t
        or "union-find" in t
        for t in all_tags
    ):
        return "Graph Traversal"
    elif any(
        "dynamic-programming" in t or "dp" in t or "memoization" in t for t in all_tags
    ):
        return "Dynamic Programming"
    elif any("backtracking" in t for t in all_tags):
        return "Backtracking"
    elif any("sliding-window" in t for t in all_tags):
        return "Sliding Window"
    elif any("binary-search" in t for t in all_tags):
        return "Binary Search"
    elif any("heap" in t or "priority-queue" in t for t in all_tags):
        return "Heap (Priority Queue)"
    elif any("stack" in t or "monotonic-stack" in t for t in all_tags):
        return "Stack"
    elif any("linked-list" in t for t in all_tags):
        return "Linked List"
    elif any("trie" in t or "prefix-tree" in t for t in all_tags):
        return "Trie"
    elif any("bit-manipulation" in t or "bitmask" in t for t in all_tags):
        return "Bit Manipulation"
    elif any("greedy" in t for t in all_tags):
        return "Greedy"
    elif any(
        "math" in t or "geometry" in t or "number-theory" in t or "combinatorics" in t
        for t in all_tags
    ):
        return "Math & Geometry"
    elif any("two-pointers" in t for t in all_tags):
        return "Two Pointers"
    elif any("intervals" in t for t in all_tags):
        return "Intervals"
    elif any("topological" in t for t in all_tags):
        return "Topological Sort"
    elif any("array" in t or "hash-table" in t or "hash" in t for t in all_tags):
        return "Array & Hashing"
    elif any("string" in t for t in all_tags):
        return "Array & Hashing"
    else:
        return "Array & Hashing"  # default


def map_difficulty(difficulty: str) -> str:
    """Map LeetCode difficulty to JSON format."""
    difficulty_map = {
        "Easy": "Easy",
        "Medium": "Medium",
        "Hard": "Hard",
    }
    return difficulty_map.get(difficulty, "Easy")


def fetch_problems_batch(limit: int = 50, skip: int = 0) -> Optional[Dict]:
    """Fetch a batch of problems from LeetCode GraphQL API."""
    variables = {
        "categorySlug": "",
        "skip": skip,
        "limit": limit,
        "filters": {},
    }

    payload = {"query": PROBLEMS_QUERY, "variables": variables}

    try:
        response = requests.post(
            LEETCODE_API_URL,
            json=payload,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            },
            timeout=30,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching problems (skip={skip}, limit={limit}): {e}")
        return None


def fetch_all_problems() -> Dict[str, Dict]:
    """Fetch all problems from LeetCode API."""
    problems = {}
    skip = 0
    limit = 50  # LeetCode API limit per request
    batch_delay = 2  # Delay between requests to avoid rate limiting

    print("Fetching problems from LeetCode API...")
    print("This may take a while due to rate limiting...")

    while True:
        print(f"Fetching batch: skip={skip}, limit={limit}...", end=" ", flush=True)
        data = fetch_problems_batch(limit=limit, skip=skip)

        if not data:
            print("Failed")
            break

        try:
            question_list = data.get("data", {}).get("problemsetQuestionList", {})
            questions = question_list.get("questions", [])
            total = question_list.get("total", 0)

            if not questions:
                print("No more questions")
                break

            for question in questions:
                frontend_id = question.get("frontendQuestionId")
                if not frontend_id:
                    continue

                # Skip premium problems if needed (optional)
                # if question.get("paidOnly"):
                #     continue

                problem_id = str(frontend_id)
                title = question.get("title", "")
                title_slug = question.get("titleSlug", "")
                difficulty = map_difficulty(question.get("difficulty", "Easy"))
                tags = question.get("topicTags", [])

                category = map_tags_to_category(tags)
                link = f"https://leetcode.com/problems/{title_slug}/"

                problems[problem_id] = {
                    "id": int(frontend_id),
                    "category": category,
                    "title": title,
                    "difficulty": difficulty,
                    "link": link,
                }

            print(f"Got {len(questions)} problems (total so far: {len(problems)})")

            # Check if we've fetched all problems
            if skip + len(questions) >= total:
                print(f"Fetched all {total} problems")
                break

            skip += limit
            time.sleep(batch_delay)  # Rate limiting

        except KeyError as e:
            print(f"Error parsing response: {e}")
            print(f"Response: {json.dumps(data, indent=2)[:500]}")
            break

    return problems


def load_existing_json() -> Dict:
    """Load existing JSON file."""
    if not os.path.exists(JSON_PATH):
        return {}

    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return {}


def save_json(data: Dict):
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
            json.dump(sorted_data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return False


def main():
    """Main function to update JSON from LeetCode API."""
    print("=" * 60)
    print("LeetCode Problems Updater")
    print("=" * 60)

    print("\nLoading existing JSON file...")
    existing_json = load_existing_json()
    print(f"Found {len(existing_json)} problems in existing JSON")

    print("\nFetching problems from LeetCode API...")
    print("Note: This will take several minutes due to rate limiting.")
    print("The script will fetch in batches with delays between requests.\n")

    leetcode_problems = fetch_all_problems()
    print(f"\nFetched {len(leetcode_problems)} problems from LeetCode")

    if not leetcode_problems:
        print("No problems fetched. Exiting.")
        sys.exit(1)

    # Find missing and updated problems
    missing = []
    updated = []

    for problem_id, problem_data in leetcode_problems.items():
        if problem_id not in existing_json:
            missing.append(problem_id)
            existing_json[problem_id] = problem_data
        else:
            # Update existing entry (in case data changed)
            existing_json[problem_id] = problem_data
            updated.append(problem_id)

    print("-" * 60)
    print(f"Found {len(missing)} missing problems")
    print(f"Updated {len(updated)} existing problems")

    if missing:
        print("\nMissing problems (first 20):")
        for pid in sorted(missing, key=int)[:20]:
            print(f"  {pid}: {leetcode_problems[pid]['title']}")
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more")

    # Save updated JSON
    print(f"\nSaving updated JSON to {JSON_PATH}...")
    if save_json(existing_json):
        print(f"Successfully saved {len(existing_json)} problems to JSON")
    else:
        print("Failed to save JSON")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("Update complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
