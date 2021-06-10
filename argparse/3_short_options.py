"""
ex) "-v", "--verbose", here we add short version of optional arguments by putting -v
"""
import argparse

parser = argparse.ArgumentParser(description="This is 3rd file about argument parsing")
parser.add_argument(
    "-v", "--verbose", help="increase output verbosity", action="store_true"
)

args = parser.parse_args()

if args.verbose:
    print("verbosity turned on")
