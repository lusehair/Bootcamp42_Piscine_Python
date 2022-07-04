from string import punctuation
from collections import Counter

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
    print("The text contains " + str(len(_input)) + " characters: ")
    print("- " +  str(sum(1 for c in _input if c.isupper())) + " upper letters")
    print("- " + str(sum(1 for c in _input if c.islower())) + " lower letters")
    print("- " +  str(dott) + " punctuation marks")
    print("- " + str(_input.count(' ')) + " spaces")
