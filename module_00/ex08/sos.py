import sys 

morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',    ' ': '/',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

def decode(humanstring) : 
    humanstring = humanstring.upper() 
    ret = ''
    for x in humanstring :
        if x in morse :
            ret = ret + morse[x]
            ret = ret + ' '
        else :
            print("ERROR")
            return
    print(ret, end='')


for x in sys.argv[1:] : 
    decode(x)
    if x != sys.argv[len(sys.argv) - 1] :
        print('/', end='')
