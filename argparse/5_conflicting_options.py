"""
Let’s introduce a third one, add_mutually_exclusive_group(). 
It allows for us to specify options that conflict with each other. 
Let’s also change the rest of the program so that the new functionality makes more sense:
we’ll introduce the --quiet option, which will be the opposite of the --verbose one:
"""
import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")

group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x ** args.y

print("Running '{}'".format(__file__))

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))
