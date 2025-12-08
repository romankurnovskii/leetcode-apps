#!/usr/bin/env python3

"""
Reads a JSON file, sorts its top-level keys numerically,
and writes the sorted data to a new JSON file following Prettier style.

Prettier config: printWidth=150, tabWidth=2, useTabs=false, trailingComma=es5, bracketSpacing=false

python scripts/normalize_json.py data/leetcode-problems.json
"""

import json
import argparse
from collections import OrderedDict


def format_json_value(value, indent_level=0):
    """Format a JSON value with custom formatting following Prettier style."""
    indent = "  " * indent_level
    next_indent = "  " * (indent_level + 1)

    if isinstance(value, dict):
        if not value:
            return "{}"
        items = []
        for k, v in sorted(value.items()):
            formatted_key = json.dumps(k, ensure_ascii=False)
            formatted_value = format_json_value(v, indent_level + 1)
            items.append(f"{next_indent}{formatted_key}: {formatted_value}")
        return "{\n" + ",\n".join(items) + "\n" + indent + "}"
    elif isinstance(value, list):
        if not value:
            return "[]"
        # Check if it's a list of numbers (for problems arrays) - format one per line
        if value and isinstance(value[0], (int, float)):
            items = [f"{next_indent}{json.dumps(item, ensure_ascii=False)}" for item in value]
            return "[\n" + ",\n".join(items) + "\n" + indent + "]"
        else:
            # Format other arrays - check if they fit on one line
            formatted_items = [format_json_value(item, indent_level + 1) for item in value]
            total_length = sum(len(str(item)) for item in formatted_items)
            if total_length < 100 and len(value) <= 5:
                # Short arrays on one line
                return "[" + ", ".join(str(item).replace("\n", " ") for item in formatted_items) + "]"
            else:
                # Long arrays with line breaks
                items = [f"{next_indent}{item}" for item in formatted_items]
                return "[\n" + ",\n".join(items) + "\n" + indent + "]"
    else:
        return json.dumps(value, ensure_ascii=False)


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

        # Format the JSON with custom formatting following Prettier style
        lines = ["{"]
        items = []
        for key, value in sorted_data.items():
            formatted_key = json.dumps(key, ensure_ascii=False)
            formatted_value = format_json_value(value, 1)
            items.append(f'  {formatted_key}: {formatted_value}')
        lines.append(",\n".join(items))
        lines.append("}")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

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
