import os
import json
import re
import argparse

SOLUTIONS_DIR = "solutions"
EXPLANATIONS_DIR = "explanations"
LEETCODE_JSON = os.path.join("data/leetcode-problems.json")
BOOK_SET_PATH = os.path.join("data/book-sets.json")

SOLUTION_TEMPLATE = """# Solution for LeetCode problem {num}

def function_name(...):
    pass
"""

EXPLANATION_TEMPLATE = """# Explanation for LeetCode problem {num}

## Explanation

_Describe the approach, logic, and steps to solve the problem._

## Hint

_Provide a helpful hint for solving the problem._

## Points

- _List key points, edge cases, or important notes for this problem._
"""


def load_leetcode_metadata():
    with open(LEETCODE_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_canonical_function_name(solution_code):
    match = re.search(r"def (\w+)\s*\(", solution_code)
    return match.group(1) if match else None


def extract_function_code(solution_code, canonical_name):
    pattern = rf"(def {re.escape(canonical_name)}\s*\(.*?\):[\s\S]*?)(?=^def |\Z)"
    match = re.search(pattern, solution_code, re.MULTILINE)
    return match.group(1).strip() if match else None


def ensure_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main(create_missing=False):
    leetcode_meta = load_leetcode_metadata()

    with open(BOOK_SET_PATH, "r", encoding="utf-8") as f:
        books_set = json.load(f)

    for book_set in books_set:
        title = book_set.get("title", "LeetCode Book").replace(" ", "_")
        book_path = f"books/{title}.md"
        problems = book_set["problems"]

        entries = []
        for num in problems:
            num_str = str(num)
            solution_path = os.path.join(SOLUTIONS_DIR, num_str, "01.py")
            explanation_path = os.path.join(EXPLANATIONS_DIR, num_str, "en.md")

            # Check or create files
            if not os.path.isfile(solution_path):
                if create_missing:
                    ensure_file(solution_path, SOLUTION_TEMPLATE.format(num=num_str))
                    print(f"Created missing solution file for {num_str}")
                else:
                    print(f"Warning: Missing solution file for {num_str}, skipping.")
                    continue

            if not os.path.isfile(explanation_path):
                if create_missing:
                    ensure_file(
                        explanation_path, EXPLANATION_TEMPLATE.format(num=num_str)
                    )
                    print(f"Created missing explanation file for {num_str}")
                else:
                    print(f"Warning: Missing explanation file for {num_str}, skipping.")
                    continue

            meta = leetcode_meta.get(num_str)
            if not meta:
                print(f"Warning: No metadata for problem {num_str}")
                continue

            with open(solution_path, encoding="utf-8") as f:
                solution_code = f.read()
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

            with open(explanation_path, encoding="utf-8") as f:
                explanation = f.read().strip()

            entry = f"## {num_str}. {meta['title']} [{meta['difficulty']}]\n{meta['link']}\n\n"
            entry += f"### Explanation\n\n{explanation}\n\n"
            entry += f"### Solution\n\n```python\n{func_code}\n```\n"
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
    parser = argparse.ArgumentParser(
        description="Generate solutions book from explanations and solutions."
    )
    parser.add_argument(
        "--create-missing",
        action="store_true",
        help="Create missing solution/explanation templates",
    )
    args = parser.parse_args()
    main(create_missing=args.create_missing)
