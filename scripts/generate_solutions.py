"""
Script to generate the English solutions book (books/solutions.en.md) from explanations and Python solutions.

- For each problem:
    - Read explanations/en.md
    - Read the first Python solution (e.g., 01.py)
    - Combine into a single markdown entry
- Write all entries to books/solutions.en.md

Future improvements:
- Handle missing files gracefully
- Support more languages or formats
"""

import os
import json
import re

SOLUTIONS_DIR = "solutions"
EXPLANATIONS_DIR = "explanations"
LEETCODE_JSON = os.path.join(SOLUTIONS_DIR, "leetcode-problems.json")
BOOK_SET_PATH = "books/book-sets.json"

SOLUTION_TEMPLATE = """# Solution for LeetCode problem {num}

def function_name(...):
    pass
"""

EXPLANATION_TEMPLATE = """# Explanation for LeetCode problem {num} (English)

## Explanation with Breakdown

_Describe the approach, logic, and steps to solve the problem._

## Hint

_Provide a helpful hint for solving the problem._

## Points

- _List key points, edge cases, or important notes for this problem._
"""


def load_leetcode_metadata():
    with open(LEETCODE_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def extract_canonical_function_name(solution_code):
    match = re.search(r"def (\w+)\s*\(", solution_code)
    if match:
        return match.group(1)
    return None


def extract_function_code(solution_code, canonical_name):
    pattern = rf"(def {re.escape(canonical_name)}\s*\(.*?\):[\s\S]*?)(?=^def |\Z)"
    match = re.search(pattern, solution_code, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def ensure_file(path, content):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.isfile(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)


def main():
    # Read book set
    with open(BOOK_SET_PATH, "r", encoding="utf-8") as f:
        book_set = json.load(f)
    problems = book_set["problems"]
    title = book_set.get("title", "LeetCode Book").replace(" ", "_")
    book_path = f"books/{title}.md"

    leetcode_meta = load_leetcode_metadata()
    entries = []
    for num in problems:
        num_str = str(num)
        solution_path = os.path.join(SOLUTIONS_DIR, num_str, "01.py")
        explanation_path = os.path.join(EXPLANATIONS_DIR, num_str, "en.md")
        # Ensure files exist
        ensure_file(solution_path, SOLUTION_TEMPLATE.format(num=num_str))
        ensure_file(explanation_path, EXPLANATION_TEMPLATE.format(num=num_str))
        # Proceed as before
        meta = leetcode_meta.get(num_str)
        if not meta:
            print(f"Warning: No metadata for problem {num_str}")
            continue
        solution_code = open(solution_path, encoding="utf-8").read()
        canonical_name = extract_canonical_function_name(solution_code)
        if not canonical_name:
            print(f"Warning: No function found in {solution_path}")
            continue
        func_code = extract_function_code(solution_code, canonical_name)
        if not func_code:
            print(
                f"Warning: Could not extract function {canonical_name} from {solution_path}"
            )
            continue
        explanation = None
        if os.path.isfile(explanation_path):
            with open(explanation_path, encoding="utf-8") as f:
                explanation = f.read().strip()
        entry = (
            f"## {num_str}. {meta['title']} [{meta['difficulty']}]\n{meta['link']}\n\n"
        )
        if explanation:
            entry += f"### Explanation\n\n{explanation}\n\n"
        entry += f"### Solution (Python)\n\n```python\n{func_code}\n```\n"
        entries.append(entry)
    book_content = (
        f"# {book_set.get('title', 'LeetCode Book')}\n\n{book_set.get('description', '')}\n\n"
        + "\n".join(entries)
    )
    os.makedirs(os.path.dirname(book_path), exist_ok=True)
    with open(book_path, "w", encoding="utf-8") as f:
        f.write(book_content)
    print(f"Generated {book_path} with {len(entries)} problems.")


if __name__ == "__main__":
    main()
