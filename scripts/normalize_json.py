#!/usr/bin/env python3

"""
Reads a JSON file, sorts its top-level keys numerically,
and writes the sorted data to a new JSON file.
Prettier will format the output according to .prettierrc config.

python scripts/normalize_json.py data/leetcode-problems.json
"""

import json
import argparse
from collections import OrderedDict


def sort_json_by_numeric_keys(input_file, output_file):
    """
    Sort JSON file by numeric keys and format according to Prettier style.

    Args:
        input_file (str): The path to the input JSON file.
        output_file (str): The path to the output (sorted) JSON file.
    """
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            print("Error: The root of the JSON file must be an object/dictionary.")
            return

        sorted_items = sorted(data.items(), key=lambda item: int(item[0]))
        sorted_data = OrderedDict(sorted_items)

        # Write JSON (Prettier will format it via pre-commit hook)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(sorted_data, f, ensure_ascii=False)

        print(
            f"Successfully sorted '{input_file}' and saved the result to '{output_file}'."
        )

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except json.JSONDecodeError:
        print(
            f"Error: Could not decode JSON from '{input_file}'. Please check its format."
        )
    except ValueError:
        print(
            "Error: All top-level keys in the JSON must be strings that can be converted to integers."
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sorts a JSON file by its top-level keys numerically.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "input_file", help="The path to the input JSON file to be sorted."
    )
    parser.add_argument(
        "output_file",
        nargs="?",
        default=None,
        help="Optional. The path to save the sorted output JSON file. If not provided, the input file will be overwritten.",
    )

    args = parser.parse_args()

    output_path = args.output_file if args.output_file else args.input_file

    sort_json_by_numeric_keys(args.input_file, output_path)
