#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file."""

import sys
from typing import List
from json import dump, load


def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file."""
    with open(filename, 'w') as f:
        dump(my_obj, f)


def load_from_json_file(filename):
    """Load an object from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return load(f)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    # Load existing data from the JSON file
    try:
        loaded_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        loaded_data = []

    # Add command-line arguments to the data
    argc = len(sys.argv)
    for idx in range(1, argc):
        loaded_data.append(sys.argv[idx])

    # Save the updated data back to the JSON file
    save_to_json_file(loaded_data, "add_item.json")
