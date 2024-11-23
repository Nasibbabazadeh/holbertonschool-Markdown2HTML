#!/usr/bin/python3
"""
markdown2html.py - A script to convert a Markdown file to an HTML file.
"""

import sys
import os

def main():
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input Markdown file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # If no issues, exit successfully (conversion logic not included in this task)
    sys.exit(0)

if __name__ == "__main__":
    main()
