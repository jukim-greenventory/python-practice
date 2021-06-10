"""
Do a search that will return a Match Object:
The Match object has properties and methods used to retrieve information about the search, and the result:
    - .span() returns a tuple containing the start-, and end positions of the match.
    - .string returns the string passed into the function
    - .group() returns the part of the string where there was a match
"""
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # this will print an object

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x)
print(x.span())


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
