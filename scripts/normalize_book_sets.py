#!/usr/bin/env python3

"""
Normalizes book-sets.json by:
1. Removing problems from "All-TODO" that have both solution and explanation
2. Updating "All" to only include problems that have both solution and explanation
3. Generating a completion report for all other sets

Usage:
    python scripts/normalize_book_sets.py
"""

import json
import os
import argparse
import re
import subprocess
from pathlib import Path


def compact_json_arrays(json_str: str, max_line_length: int = 150) -> str:
    """
    Compact number arrays in JSON string to have multiple numbers per line.

    Args:
        json_str: JSON string with arrays formatted one number per line
        max_line_length: Maximum characters per line (default: 150)

    Returns:
        Compacted JSON string
    """
    lines = json_str.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this line starts an array of numbers
        # Pattern: some indentation, "key": [
        array_start_match = re.match(r'^(\s*)"[^"]+": \[$', line)

        if array_start_match:
            indent = array_start_match.group(1)
            result.append(line)
            i += 1

            # Collect all numbers from subsequent lines
            numbers = []
            while i < len(lines):
                num_line = lines[i].strip()

                # Check if it's a closing bracket
                if num_line == "]" or num_line == "],":
                    # Format numbers compactly
                    if numbers:
                        # Group numbers to fit within max_line_length
                        number_indent = indent + "    "
                        current_line = number_indent

                        for idx, num in enumerate(numbers):
                            num_str = str(num)
                            # Add comma if not the last number
                            if idx < len(numbers) - 1:
                                num_str += ", "

                            # Check if adding this number would exceed max length
                            if (
                                len(current_line + num_str) > max_line_length
                                and current_line != number_indent
                            ):
                                result.append(current_line.rstrip())
                                current_line = number_indent + num_str
                            else:
                                current_line += num_str

                        # Add the last line
                        if current_line.strip():
                            result.append(current_line.rstrip())

                    # Add closing bracket
                    result.append(indent + num_line)
                    i += 1
                    break

                # Check if it's a number (with optional comma)
                num_match = re.match(r"^(\d+),?$", num_line)
                if num_match:
                    numbers.append(int(num_match.group(1)))
                    i += 1
                else:
                    # Not a number array, just add the line as-is
                    result.append(lines[i])
                    i += 1
                    break
        else:
            result.append(line)
            i += 1

    return "\n".join(result)


def check_solution_exists(problem_number: int, solutions_dir: Path) -> bool:
    """Check if solution exists for a problem number."""
    solution_path = solutions_dir / str(problem_number) / "01.py"
    return solution_path.exists()


def check_explanation_exists(problem_number: int, explanations_dir: Path) -> bool:
    """Check if explanation exists for a problem number."""
    explanation_path = explanations_dir / str(problem_number) / "en.md"
    return explanation_path.exists()


def has_both_solution_and_explanation(
    problem_number: int, solutions_dir: Path, explanations_dir: Path
) -> bool:
    """Check if both solution and explanation exist for a problem number."""
    return check_solution_exists(
        problem_number, solutions_dir
    ) and check_explanation_exists(problem_number, explanations_dir)


def generate_set_report(
    set_obj: dict,
    solutions_dir: Path,
    explanations_dir: Path,
) -> dict:
    """
    Generate a completion report for a problem set.

    Args:
        set_obj: The set object from book-sets.json
        solutions_dir: Path to solutions directory
        explanations_dir: Path to explanations directory

    Returns:
        Dictionary with completion status and missing problems
    """
    title = set_obj.get("title", "Unknown")
    problems = set_obj.get("problems", [])

    if not problems:
        return {
            "title": title,
            "total": 0,
            "completed": 0,
            "missing": [],
            "is_complete": True,
        }

    missing = []
    completed = 0

    for problem_num in problems:
        if has_both_solution_and_explanation(
            problem_num, solutions_dir, explanations_dir
        ):
            completed += 1
        else:
            missing.append(problem_num)

    return {
        "title": title,
        "total": len(problems),
        "completed": completed,
        "missing": sorted(missing),
        "is_complete": len(missing) == 0,
    }


def normalize_book_sets(
    book_sets_file: str,
    solutions_dir: str,
    explanations_dir: str,
    dry_run: bool = False,
):
    """
    Normalize book-sets.json file.

    Args:
        book_sets_file: Path to book-sets.json file
        solutions_dir: Path to solutions directory
        explanations_dir: Path to explanations directory
        dry_run: If True, only print changes without writing to file
    """
    solutions_path = Path(solutions_dir)
    explanations_path = Path(explanations_dir)

    # Read the JSON file
    try:
        with open(book_sets_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{book_sets_file}' was not found.")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Could not decode JSON from '{book_sets_file}': {e}")
        return

    if not isinstance(data, list):
        print("Error: The root of the JSON file must be an array.")
        return

    # Find the "All-TODO" and "All" objects, and get premium list
    all_todo_obj = None
    all_obj = None
    premium_set = set()

    for obj in data:
        if obj.get("title") == "All-TODO":
            all_todo_obj = obj
        elif obj.get("title") == "All":
            all_obj = obj
        elif "premium" in obj:
            # Get premium problems list
            premium_set = set(obj.get("premium", []))

    changes_made = False

    # Process "All-TODO": Remove problems that have both solution and explanation
    if all_todo_obj:
        original_count = len(all_todo_obj.get("problems", []))
        problems = all_todo_obj.get("problems", [])
        removed = []

        new_problems = []
        for problem_num in problems:
            if has_both_solution_and_explanation(
                problem_num, solutions_path, explanations_path
            ):
                removed.append(problem_num)
            else:
                new_problems.append(problem_num)

        if removed:
            changes_made = True
            print(
                f"\n[All-TODO] Removing {len(removed)} problems with both solution and explanation:"
            )
            print(f"  Removed: {removed[:10]}{'...' if len(removed) > 10 else ''}")
            all_todo_obj["problems"] = sorted(new_problems)
            print(f"  Updated count: {original_count} -> {len(new_problems)}")
        else:
            print("\n[All-TODO] No changes needed")

    # Process "All": Update to only include problems with both solution and explanation
    if all_obj:
        # Get all problem numbers from solutions and explanations directories
        all_solution_dirs = {
            int(d.name)
            for d in solutions_path.iterdir()
            if d.is_dir() and d.name.isdigit()
        }
        all_explanation_dirs = {
            int(d.name)
            for d in explanations_path.iterdir()
            if d.is_dir() and d.name.isdigit() and not d.name.startswith("todo-")
        }

        # Find problems that have both (excluding premium)
        problems_with_both = sorted(
            [
                p
                for p in all_solution_dirs
                if p in all_explanation_dirs
                and has_both_solution_and_explanation(
                    p, solutions_path, explanations_path
                )
                and p not in premium_set  # Exclude premium problems
            ]
        )

        original_count = len(all_obj.get("problems", []))
        original_problems = set(all_obj.get("problems", []))
        problems_with_both_set = set(problems_with_both)

        # Remove premium problems from original_problems for comparison
        original_non_premium = original_problems - premium_set
        removed_premium = sorted(original_problems & premium_set)

        # Always update if there are premium problems to remove, or if sets differ
        if removed_premium or problems_with_both_set != original_non_premium:
            changes_made = True
            added = sorted(problems_with_both_set - original_non_premium)
            removed = sorted(original_non_premium - problems_with_both_set)

            print(f"\n[All] Updating problem list:")
            if removed_premium:
                print(
                    f"  Removed {len(removed_premium)} premium problems: {removed_premium[:10]}{'...' if len(removed_premium) > 10 else ''}"
                )
            if added:
                print(
                    f"  Added {len(added)} problems: {added[:10]}{'...' if len(added) > 10 else ''}"
                )
            if removed:
                print(
                    f"  Removed {len(removed)} problems: {removed[:10]}{'...' if len(removed) > 10 else ''}"
                )
            print(f"  Updated count: {original_count} -> {len(problems_with_both)}")

            all_obj["problems"] = problems_with_both
        else:
            print("\n[All] No changes needed")

    # Generate and print reports for all other sets
    print("\n" + "=" * 70)
    print("COMPLETION REPORT FOR ALL SETS")
    print("=" * 70)

    reports = []
    for obj in data:
        title = obj.get("title", "Unknown")
        # Skip "All-TODO" and "All" as they are handled separately
        if title in ["All-TODO", "All"]:
            continue

        report = generate_set_report(obj, solutions_path, explanations_path)
        reports.append(report)

    # Sort reports by completion percentage (completed sets first, then by title)
    reports.sort(
        key=lambda r: (
            not r["is_complete"],
            -r["completed"] / r["total"] if r["total"] > 0 else 0,
            r["title"],
        )
    )

    # Print reports
    for report in reports:
        title = report["title"]
        total = report["total"]
        completed = report["completed"]
        missing = report["missing"]
        is_complete = report["is_complete"]

        completion_pct = (completed / total * 100) if total > 0 else 100

        if is_complete:
            print(f"\n✓ {title}")
            print(f"  Status: COMPLETE ({completed}/{total} problems)")
        else:
            print(f"\n✗ {title}")
            print(
                f"  Status: INCOMPLETE ({completed}/{total} problems, {completion_pct:.1f}%)"
            )
            if missing:
                # Show first 20 missing problems, then count if more
                if len(missing) <= 20:
                    print(f"  Missing problems: {missing}")
                else:
                    print(f"  Missing problems ({len(missing)}): {missing[:20]}...")
                    print(f"    ... and {len(missing) - 20} more")

    # Summary statistics
    total_sets = len(reports)
    completed_sets = sum(1 for r in reports if r["is_complete"])
    total_problems = sum(r["total"] for r in reports)
    total_completed_problems = sum(r["completed"] for r in reports)

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total sets: {total_sets}")
    print(
        f"Completed sets: {completed_sets} ({completed_sets/total_sets*100:.1f}%)"
        if total_sets > 0
        else "Completed sets: 0"
    )
    print(f"Total problems across all sets: {total_problems}")
    print(
        f"Completed problems: {total_completed_problems} ({total_completed_problems/total_problems*100:.1f}%)"
        if total_problems > 0
        else "Completed problems: 0"
    )

    # Write the updated JSON file
    if changes_made:
        if dry_run:
            print("\n" + "=" * 70)
            print("[DRY RUN] Would write changes to file (use --write to apply)")
        else:
            try:
                # Write JSON file (prettier will format it)
                with open(book_sets_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False)

                # Format with prettier
                try:
                    subprocess.run(
                        ["npx", "prettier", "--write", book_sets_file],
                        check=True,
                        capture_output=True,
                    )
                except subprocess.CalledProcessError as e:
                    print(f"Warning: Prettier formatting failed: {e}")
                except FileNotFoundError:
                    print("Warning: npx/prettier not found, skipping formatting")

                print("\n" + "=" * 70)
                print(f"✓ Successfully updated '{book_sets_file}'")
            except Exception as e:
                print("\n" + "=" * 70)
                print(f"✗ Error writing to file: {e}")
    else:
        print("\n" + "=" * 70)
        print("✓ No changes needed - file is already normalized")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Normalize book-sets.json by updating All-TODO and All problem lists, and generate completion reports.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--book-sets",
        default="data/book-sets.json",
        help="Path to book-sets.json file (default: data/book-sets.json)",
    )
    parser.add_argument(
        "--solutions-dir",
        default="solutions",
        help="Path to solutions directory (default: solutions)",
    )
    parser.add_argument(
        "--explanations-dir",
        default="explanations",
        help="Path to explanations directory (default: explanations)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without writing to file",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write changes to file (overrides --dry-run)",
    )

    args = parser.parse_args()

    # Determine if we should write or do a dry run
    dry_run = args.dry_run and not args.write

    normalize_book_sets(
        args.book_sets,
        args.solutions_dir,
        args.explanations_dir,
        dry_run=dry_run,
    )
