import sys 

arguments = sys.argv[1:]
arguments = arguments[::-1]

for x in range(len(arguments)):
    
    arguments[x] = arguments[x] [::-1] 
    print(arguments[x].swapcase(),end=' ')
