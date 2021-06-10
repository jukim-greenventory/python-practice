"""
base form:
    - parse_args(['option','value'])
other forms:
    For long options (options with names longer than a single character), 
    the option and value can also be passed as a single command-line argument, using = to separate them:
        - parse_args(['--option=value'])
    For short options (options only one character long), 
    the option and its value can be concatenated:
        - parse_args(['-optionvalue'])

About dest:
    - dest allows a custom attribute name to be provided: (in our case "integers")
About metavar:
    - metavar only changes the displayed name - the name of the attribute on the parse_args() object is still 
    determined by the dest value.
About const:
    - 
About nargs:
    N (an integer). 
        - N arguments from the command line will be gathered together into a list. For example:
    '+'
        - Just like '*', all command-line args present are gathered into a list. 
        Additionally, an error message will be generated if there wasn’t at least one command-line argument present.
    '*'
        -
    '?'
        - One argument will be consumed from the command line if possible, and produced as a single item. 
        If no command-line argument is present, the value from default will be produced.
"""
import argparse

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "integers", metavar="N", type=int, nargs="+", help="an integer for the accumulator"
)
parser.add_argument(
    "--sum",
    dest="accumulate",
    action="store_const",
    const=sum,
    default=max,
    help="sum the integers (default: find the max)",
)

args = parser.parse_args()
print(args)
print(args.accumulate(args.integers))
