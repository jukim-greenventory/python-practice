"""
Refer to:
    - https://www.w3schools.com/python/python_regex.asp
    - https://docs.python.org/3/library/re.html
"""
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:  # match object
    print("Yes we have a match")
    print(x)
    print(x.start())
    print(x.end())
else:  # None
    print("No match")
print("".center(20, "-"))

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, maxsplit=1)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, count=2)
print(x)
