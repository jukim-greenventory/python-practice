"""
optional arguments "--argument"

To show that the option is actually optional, there is no error when running the program without it. 
Note that by default, if an optional argument isn’t used, the relevant variable, in this case args.verbosity, 
is given None as a value (False when "store_true" is used)
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--verbosity", help="increase output verbosity", action="store_true"
)

args = parser.parse_args()
print(args)
if args.verbosity:
    print("verbosity turned on")
