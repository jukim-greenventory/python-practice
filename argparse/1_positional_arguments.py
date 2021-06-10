"""
positional arguments "argument"

Typical work flow

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(...)
    ...
    ...
    args = parser.parse_args()

    python filename.py --argument --argument ...
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="display a square of a given number", type=int)
# parsing arguments creates a namespace (sort of dictionary?)
args = parser.parse_args()

print(type(args), args)
print(args.square ** 2)
