from string import punctuation
from collections import Counter

# def text_analyzer:

input = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido va Rossum and first released in 1991, Pythons design philosophy emphasizes code readability with its notable use of significant whitespace."
spaces = input.count(' ') 
upper = sum(1 for c in input if c.isupper())
lower = sum(1 for c in input if c.islower())
dott = {k:v for k, v in input.iteritems() if k in punctuation}

print("spaces: ", spaces)
print("upper: ", upper)
print("lower: ", lower)
print("ponctuation: ", len(dott))
print("char: ", len(input))