from string import punctuation
from collections import Counter
import sys

def text_analyzer(*_input):
    dott = 0;
    if len(_input) == 0 :
       _input =  input("What is the text to analyze? ")
    elif len(_input) > 1 :
        print("ERROR")
        return
    else :
        _input = _input[0] 

    for i in _input :
        if i in punctuation :
            dott += 1
    print("The text contains " + str(len(_input)) + " character(s): ")
    print("- " +  str(sum(1 for c in _input if c.isupper())) + " upper letter(s)")
    print("- " + str(sum(1 for c in _input if c.islower())) + " lower letter(s)")
    print("- " +  str(dott) + " punctuation mark(s)")
    print("- " + str(_input.count(' ')) + " space(s)")


if __name__ == "__main__":

    if len(sys.argv) != 2 :
        print("AssertionError: more than one argument are provided")
    else :
        text_analyzer(sys.argv[1])

